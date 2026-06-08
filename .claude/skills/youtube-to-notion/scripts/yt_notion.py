#!/usr/bin/env python3
"""
YouTube -> Notion 인사이트 DB 헬퍼.

subcommands:
  fetch  --url URL [--lang ko]      영상 ID/제목/채널/썸네일/자막을 수집해 캐시 파일로 저장하고
                                    메타데이터(JSON)를 stdout에 출력. transcript 본문은 캐시 파일에 있음.
  save   --url URL --title ... --channel ... --thumbnail ...
         --summary "..." [--categories "마케팅,트렌드"] [--date YYYY-MM-DD]
                                    수집·요약된 내용을 Notion DB에 한 행으로 추가.

환경변수: NOTION_TOKEN 필요 (save 시).
config.json 에서 database_id 를 읽음. --db 로 override 가능.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
CACHE_DIR = os.path.join(SKILL_DIR, ".cache")
CONFIG_PATH = os.path.join(SKILL_DIR, "config.json")
NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


def load_config():
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def extract_video_id(url):
    """다양한 유튜브 URL 형태에서 11자리 video id 추출."""
    url = url.strip()
    # 이미 11자리 ID만 준 경우
    if re.fullmatch(r"[0-9A-Za-z_-]{11}", url):
        return url
    patterns = [
        r"(?:v=|/v/|youtu\.be/|/embed/|/shorts/|/live/)([0-9A-Za-z_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    # query 파싱 fallback
    try:
        q = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(q.query)
        if "v" in params and len(params["v"][0]) == 11:
            return params["v"][0]
    except Exception:
        pass
    return None


def http_get(url, headers=None, timeout=20):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read()


def fetch_oembed(video_id):
    """제목/채널/채널URL 가져오기 (키 불필요)."""
    watch = f"https://www.youtube.com/watch?v={video_id}"
    url = "https://www.youtube.com/oembed?" + urllib.parse.urlencode(
        {"url": watch, "format": "json"}
    )
    try:
        status, body = http_get(url)
        if status == 200:
            d = json.loads(body)
            return {
                "title": d.get("title"),
                "channel": d.get("author_name"),
                "channel_url": d.get("author_url"),
            }
    except Exception as e:
        print(f"[warn] oembed 실패: {e}", file=sys.stderr)
    return {"title": None, "channel": None, "channel_url": None}


def best_thumbnail(video_id):
    """maxres가 있으면 maxres, 없으면 hqdefault(항상 존재)."""
    maxres = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    try:
        req = urllib.request.Request(maxres, method="HEAD")
        with urllib.request.urlopen(req, timeout=10) as r:
            if r.status == 200:
                return maxres
    except Exception:
        pass
    return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"


def fetch_transcript(video_id, prefer="ko"):
    """
    언어 우선순위: 수동 prefer > 자동 prefer > 수동 en > 자동 en > 수동 any > 자동 any.
    반환: (text, language_code, is_generated) 또는 (None, None, None).
    """
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("[error] youtube-transcript-api 미설치: pip install youtube-transcript-api",
              file=sys.stderr)
        return None, None, None

    api = YouTubeTranscriptApi()
    try:
        listing = list(api.list(video_id))
    except Exception as e:
        print(f"[error] 자막 목록 조회 실패: {e}", file=sys.stderr)
        return None, None, None

    def score(t):
        lc = t.language_code.lower()
        gen = t.is_generated
        if lc.startswith(prefer):
            base = 0
        elif lc.startswith("en"):
            base = 2
        else:
            base = 4
        return base + (1 if gen else 0)

    if not listing:
        return None, None, None
    chosen = sorted(listing, key=score)[0]
    try:
        data = chosen.fetch()
        raw = data.to_raw_data() if hasattr(data, "to_raw_data") else data
        text = " ".join(s["text"].replace("\n", " ").strip() for s in raw if s.get("text"))
        text = re.sub(r"\s+", " ", text).strip()
        return text, chosen.language_code, chosen.is_generated
    except Exception as e:
        print(f"[error] 자막 다운로드 실패: {e}", file=sys.stderr)
        return None, None, None


def cmd_fetch(args):
    video_id = extract_video_id(args.url)
    if not video_id:
        print(json.dumps({"ok": False, "error": "video_id 추출 실패", "url": args.url},
                         ensure_ascii=False))
        sys.exit(1)

    meta = fetch_oembed(video_id)
    thumb = best_thumbnail(video_id)
    text, lang, generated = fetch_transcript(video_id, prefer=args.lang)

    os.makedirs(CACHE_DIR, exist_ok=True)
    cache_path = os.path.join(CACHE_DIR, f"{video_id}.json")
    payload = {
        "video_id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "title": meta["title"],
        "channel": meta["channel"],
        "channel_url": meta["channel_url"],
        "thumbnail": thumb,
        "transcript_language": lang,
        "transcript_is_generated": generated,
        "transcript": text,
    }
    with open(cache_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    header = {
        "ok": text is not None,
        "video_id": video_id,
        "url": payload["url"],
        "title": meta["title"],
        "channel": meta["channel"],
        "thumbnail": thumb,
        "transcript_language": lang,
        "transcript_is_generated": generated,
        "transcript_chars": len(text) if text else 0,
        "cache_path": cache_path,
    }
    if text is None:
        header["error"] = "자막을 찾지 못했습니다 (자막 없는 영상이거나 비공개)."
    print(json.dumps(header, ensure_ascii=False, indent=2))


def notion_post(path, token, body):
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        f"{NOTION_API}{path}",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": NOTION_VERSION,
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, json.loads(r.read())


def cmd_save(args):
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print(json.dumps({"ok": False, "error": "NOTION_TOKEN 미설정"}, ensure_ascii=False))
        sys.exit(1)
    cfg = load_config()
    db_id = args.db or cfg["database_id"]
    max_chars = cfg.get("summary_max_chars", 1000)
    valid_cats = set(cfg.get("categories", []))

    summary = args.summary or ""
    if len(summary) > max_chars:
        summary = summary[:max_chars].rstrip()

    cats = []
    if args.categories:
        for c in args.categories.split(","):
            c = c.strip()
            if not c:
                continue
            if valid_cats and c not in valid_cats:
                print(f"[warn] '{c}' 는 정의된 카테고리가 아니라 '기타'로 대체", file=sys.stderr)
                c = "기타"
            cats.append(c)

    the_date = args.date or date.today().isoformat()

    props = {
        "영상 제목": {"title": [{"text": {"content": (args.title or "(제목 없음)")[:2000]}}]},
    }
    if args.channel:
        props["채널"] = {"rich_text": [{"text": {"content": args.channel[:2000]}}]}
    if args.url:
        props["URL"] = {"url": args.url}
    if args.thumbnail:
        props["썸네일"] = {
            "files": [
                {
                    "type": "external",
                    "name": "thumbnail.jpg",
                    "external": {"url": args.thumbnail},
                }
            ]
        }
    if summary:
        props["인사이트 요약"] = {"rich_text": [{"text": {"content": summary}}]}
    if cats:
        props["카테고리"] = {"multi_select": [{"name": c} for c in cats]}
    if the_date:
        props["저장일"] = {"date": {"start": the_date}}

    body = {"parent": {"database_id": db_id}, "properties": props}
    try:
        status, resp = notion_post("/pages", token, body)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        print(json.dumps({"ok": False, "error": f"HTTP {e.code}", "detail": detail},
                         ensure_ascii=False))
        sys.exit(1)

    print(json.dumps({
        "ok": True,
        "page_id": resp.get("id"),
        "page_url": resp.get("url"),
        "title": args.title,
        "summary_chars": len(summary),
        "categories": cats,
        "date": the_date,
    }, ensure_ascii=False, indent=2))


def main():
    p = argparse.ArgumentParser(description="YouTube -> Notion 인사이트 DB")
    sub = p.add_subparsers(dest="cmd", required=True)

    pf = sub.add_parser("fetch", help="영상 메타+자막 수집")
    pf.add_argument("--url", required=True)
    pf.add_argument("--lang", default="ko", help="선호 자막 언어 prefix (기본 ko)")
    pf.set_defaults(func=cmd_fetch)

    ps = sub.add_parser("save", help="Notion DB에 행 추가")
    ps.add_argument("--url")
    ps.add_argument("--title", required=True)
    ps.add_argument("--channel")
    ps.add_argument("--thumbnail")
    ps.add_argument("--summary", required=True)
    ps.add_argument("--categories", help="콤마 구분")
    ps.add_argument("--date", help="YYYY-MM-DD (기본 오늘)")
    ps.add_argument("--db", help="DB ID override")
    ps.set_defaults(func=cmd_save)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
