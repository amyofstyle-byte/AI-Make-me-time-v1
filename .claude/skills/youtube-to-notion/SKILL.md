---
name: youtube-to-notion
description: 자막 있는 유튜브 영상 주소를 주면 자막을 분석해 핵심 인사이트를 1000자 이내로 요약하고, 제목·채널·썸네일·카테고리와 함께 "YouTube 인사이트" Notion DB에 한 행으로 저장. "유튜브 정리", "이 영상 노션에 저장", "유튜브 인사이트", "영상 요약해서 노션에", "youtube 저장", youtube.com/youtu.be 링크와 함께 "노션에 넣어줘/요약해줘" 등을 언급하면 자동 실행.
context: fork
allowed-tools:
  - Bash
  - Read
---

# YouTube → Notion 인사이트 저장 스킬

자막 있는 유튜브 영상 → 인사이트 1000자 요약 → "YouTube 인사이트" Notion DB에 저장.

- **대상 DB**: `config.json` 의 `database_id` (처음 쓸 때 본인 Notion DB id를 넣으세요. DB는 "이 노션 페이지에 유튜브 인사이트 DB 만들어줘"로 먼저 생성 → 그 id를 config.json에 입력)
- **DB 속성**: 영상 제목(title) · 채널 · URL · 썸네일(파일) · 인사이트 요약(≤1000자) · 카테고리(다중선택) · 저장일
- **카테고리 선택지**: 마케팅 · 브랜딩 · AI/기술 · 크리에이티브 · 트렌드 · 비즈니스 · 기타

## 전제 조건

- `NOTION_TOKEN` 환경변수 (settings.local.json 에 설정됨 — 자동 주입)
- venv 파이썬 사용: `.venv/bin/python3` (requests, youtube-transcript-api 설치됨)
- 미설치 시: `.venv/bin/python3 -m pip install youtube-transcript-api`

## 실행 절차 (반드시 이 순서)

### 1단계 — 자막·메타데이터 수집 (fetch)

```bash
.venv/bin/python3 .claude/skills/youtube-to-notion/scripts/yt_notion.py fetch --url "<유튜브URL>"
```

- stdout 으로 `ok / title / channel / thumbnail / transcript_language / transcript_chars / cache_path` 출력.
- 자막 본문은 길어서 stdout에 싣지 않음 → **`cache_path` 파일을 Read 도구로 읽어** `transcript` 필드를 확인.
- `ok: false` (자막 없음)이면 사용자에게 알리고 중단. 자막 없는 영상은 이 스킬로 처리 불가.
- 한국어 자막 우선, 없으면 영어/기타. 자동생성(`is_generated:true`) 자막이면 오탈자 가능성 감안해 요약.

### 2단계 — 인사이트 요약 (Claude가 직접)

캐시 파일의 `transcript` 를 읽고 다음을 작성:

- **인사이트 요약 (≤1000자, 한국어)**: 단순 줄거리 요약이 아니라 **이 영상에서 건질 핵심 인사이트**. 본인 업무 맥락에 맞춰 실무에 적용 가능한 관점 위주로 정리. 핵심 주장 → 근거/사례 → 적용 포인트 순으로 압축. 1000자를 넘기지 말 것 (스크립트가 잘라내지만 의미가 끊기지 않게 처음부터 1000자 내로).
- **카테고리 1~3개**: 위 7개 선택지 중에서만 선택 (정의 외 값은 자동으로 '기타' 처리됨).

### 3단계 — Notion DB에 저장 (save)

```bash
.venv/bin/python3 .claude/skills/youtube-to-notion/scripts/yt_notion.py save \
  --url "<URL>" \
  --title "<영상 제목>" \
  --channel "<채널명>" \
  --thumbnail "<thumbnail URL>" \
  --summary "<1000자 이내 인사이트 요약>" \
  --categories "마케팅,트렌드"
```

- `--title`/`--channel`/`--thumbnail`/`--url` 은 1단계 fetch 결과를 그대로 사용.
- `--date` 생략 시 오늘 날짜 자동.
- 성공 시 `page_url` 출력 → 사용자에게 링크 전달.

## 완료 보고

사용자에게: 저장된 **영상 제목**, 선택한 **카테고리**, **요약 글자수**, **Notion 페이지 링크**를 간단히 보고.

## 여러 영상 한 번에

여러 URL을 주면 각각 1~3단계를 반복. 영상마다 개별 행으로 저장.

## 주의

- 자막 없는 영상은 처리 불가 → 사용자에게 명확히 안내.
- 썸네일은 외부 링크(파일 속성)로 연결됨. maxres가 없으면 hqdefault로 자동 fallback.
- 요약은 반드시 한국어, 실무 적용 관점. 영상이 영어여도 요약은 한국어로.
