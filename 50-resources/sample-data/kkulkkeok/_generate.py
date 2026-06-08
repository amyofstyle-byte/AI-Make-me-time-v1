#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
꿀꺽하우스(부산 광안리 전통주 양조장+브루펍) AX 데모 더미데이터 생성기.
4종 CSV: sales / product_master / inventory / content
- 채널: 브루펍 직접판매(토스 포스), 자사몰, 스마트스토어, B2B 유통
- 콘텐츠 연동일을 일·SKU 양쪽에서 급등으로 검출되게 설계
재현 가능: random.seed 고정.
"""
import csv, random, datetime as dt

random.seed(20260606)

OUT = __file__.rsplit("/", 1)[0]
YEAR, MONTH = 2026, 5          # 2026년 5월 한 달
DAYS = 31

# ── 제품 마스터 (실제 제품명, 도수/용량은 리서치 확인값) ──────────────
# 가격은 더미(크래프트 전통주 통상가 범위). 정가 > 자사몰가 > 채널가.
# 채널 단가는 product_master 정의값을 sales가 그대로 참조 → 정합성 보장.
PRODUCTS = [
    # sku, 카테고리, 상품명, 도수, 용량ml, 원가, 정가, 자사몰가, 펍가, 스토어가, B2B가, 안전재고, 시즌
    ("YOK-750", "시그니처", "욕망의 거친 물결", 12.0, 750, 5200, 16000, 15000, 14000, 14500, 11000, 60, "연중"),
    ("DAE-375", "시즈널",  "대추걸렸네",       10.0, 375, 3100,  9500,  8800,  8000,  8500,  6200, 40, "가을겨울"),
    ("SAN-750", "시그니처", "산뜻",             11.0, 750, 4900, 15000, 14000, 13000, 13500, 10300, 50, "여름"),
    ("TEO-750", "시그니처", "텃밭",             11.5, 750, 5400, 16500, 15500, 14500, 15000, 11400, 35, "연중"),
    ("ACH-500", "협업",     "아침에쌀",         8.0,  500, 3600, 11000, 10000,  9500,  9800,  7300, 45, "연중"),
    ("GWA-375", "시즈널",   "광안밤",           9.0,  375, 3300, 10000,  9300,  8500,  9000,  6600, 30, "가을"),
]

CH = {  # 채널코드: (이름, 단가키 인덱스, 가중치)
    "PUB": ("브루펍포스", 9,  0.42),   # 토스 포스, 펍가
    "MAL": ("자사몰",     8,  0.20),   # 자사몰가
    "SST": ("스마트스토어", 10, 0.23),  # 스토어가
    "B2B": ("B2B유통",    11, 0.15),   # B2B가
}
PRICE_IDX = {"PUB": 8, "MAL": 7, "SST": 9, "B2B": 10}  # PRODUCTS 튜플 인덱스(펍8/자사몰7/스토어9/B2B10)

REGION = [("부산",40),("서울",18),("경기",14),("경남",10),("울산",6),("대구",5),("인천",4),("기타",3)]
STATUS = [("배송완료",78),("배송중",9),("교환완료",7),("취소완료",6)]
HOURW  = [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,3,5,9,11,12,10,7,4]  # 펍은 저녁 집중

# 콘텐츠 연동 급등일: 그날 주문 수 + 대상 SKU를 강하게 끌어올림
# (게시일, 대상SKU, 대상채널, day_factor, sku_boost)
# day_factor: 그날 해당 채널 주문 수 배수 / force_ratio: 그날 그 채널 주문 중 대상 SKU 강제 비율
# 펍 채널 스파이크는 영업일(수목금토일)에만 배치(월화 휴무).
SPIKES = {
    "2026-05-08": ("YOK-750", "PUB", 2.6, 0.82),   # 금요일 펍 페어링 나이트 + 릴스
    "2026-05-13": ("SAN-750", "MAL", 5.0, 0.92),   # 산뜻 여름 신상 자사몰 런칭 캐러셀(수요일, 소채널→배수↑)
    "2026-05-17": ("ACH-500", "SST", 4.5, 0.92),   # 청년농부 협업 스토리 → 스마트스토어
    "2026-05-23": ("TEO-750", "PUB", 2.6, 0.82),   # 토요일 텃밭 페어링 모임 + 피드
}

def weighted(pairs):
    pool = []
    for k, w in pairs: pool += [k]*w
    return random.choice(pool)

def price_of(sku_tuple, ch):
    return sku_tuple[PRICE_IDX[ch]]

# ── 1) product_master.csv ─────────────────────────────────────────────
with open(f"{OUT}/product_master.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["SKU","카테고리","상품명","도수","용량ml","원가",
                "정가","자사몰판매가","브루펍판매가","스마트스토어판매가","B2B공급가",
                "자사몰수수료율","스마트스토어수수료율","B2B수수료율","안전재고","시즌"])
    for p in PRODUCTS:
        sku,cat,name,abv,vol,cost,msrp,mall,pub,sst,b2b,safety,season = p
        # 채널 수수료율: 자사몰 PG 3.3%, 스마트스토어 5.8%, B2B(도매마진형) 0%
        w.writerow([sku,cat,name,abv,vol,cost,msrp,mall,pub,sst,b2b,
                    0.033, 0.058, 0.0, safety, season])

# ── 2) sales.csv ──────────────────────────────────────────────────────
rows = []
order_seq = {c:0 for c in CH}
base_orders = {  # 채널별 평일 기본 주문 수
    "PUB": 22, "MAL": 9, "SST": 11, "B2B": 3,
}

def make_order(date_str, ch, sku_force=None):
    """한 주문(1~3개 라인). 배송지/상태/시간은 주문단위 1회 결정."""
    order_seq[ch]+=1
    ymd = date_str.replace("-","")[2:]
    oid = f"{ch}-{ymd}-{order_seq[ch]:04d}"
    hour = weighted([(h, HOURW[h]) for h in range(24)])
    minute = random.randint(0,59)
    region = "B2B거래처" if ch=="B2B" else weighted(REGION)
    status = "배송완료" if ch=="PUB" else weighted(STATUS)
    if ch=="PUB": status="현장판매"
    n_lines = 1 if ch!="B2B" else random.randint(2,4)
    if random.random()<0.35 and ch!="B2B": n_lines=2
    if sku_force: n_lines = 1   # 콘텐츠 연동 주문은 대상 SKU 단일 라인(희석 방지)
    chosen = set()
    out=[]
    for _ in range(n_lines):
        if sku_force and not out:
            p = next(x for x in PRODUCTS if x[0]==sku_force)
        else:
            p = random.choice(PRODUCTS)
        if p[0] in chosen and len(chosen)<len(PRODUCTS):
            p = random.choice([x for x in PRODUCTS if x[0] not in chosen])
        chosen.add(p[0])
        qty = random.randint(1,2) if ch!="B2B" else random.randint(6,30)
        unit = price_of(p, ch)
        out.append([oid, date_str, f"{hour:02d}:{minute:02d}", CH[ch][0],
                    p[1], p[2], p[0], qty, unit, qty*unit, region, status])
    return out

for d in range(1, DAYS+1):
    date = dt.date(YEAR, MONTH, d)
    date_str = date.isoformat()
    wd = date.weekday()  # 0=월
    # 펍은 월(0)·화(1) 휴무
    weekend_boost = 1.45 if wd in (4,5) else (1.15 if wd==6 else 1.0)
    spike = SPIKES.get(date_str)
    for ch in CH:
        n = base_orders[ch]
        if ch=="PUB":
            if wd in (0,1):       # 월화 휴무
                continue
            n = int(n*weekend_boost)
        else:
            n = int(n*(1.1 if wd in (4,5,6) else 1.0))
        # 콘텐츠 급등일: 대상 채널은 강하게 + 대상 SKU 집중, 그 외 채널은 후광(halo)으로 소폭 상승
        # (실제 런칭/이벤트는 그날 전체 트래픽을 끌어올린다 → 일 총매출이 검출 임계 +30%를 분명히 넘게)
        day_factor, force_ratio, force_sku = 1.0, 0.0, None
        if spike:
            if spike[1]==ch:
                day_factor = spike[2]; force_ratio = spike[3]; force_sku = spike[0]
            else:
                day_factor = 1.35   # 후광 효과
        n = max(1, int(round(n*day_factor + random.uniform(-1,1))))
        for _ in range(n):
            force = force_sku if (force_sku and random.random() < force_ratio) else None
            rows += make_order(date_str, ch, sku_force=force)

with open(f"{OUT}/sales.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["주문번호","주문일","주문시간","채널","카테고리","상품명","SKU","수량","단가","합계","배송지역","주문상태"])
    w.writerows(rows)

# ── 3) inventory.csv ──────────────────────────────────────────────────
# 5월 판매량 집계 후 잔여재고/안전재고 비교
sold = {}
for r in rows:
    sold[r[6]] = sold.get(r[6],0) + r[7]
with open(f"{OUT}/inventory.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["SKU","상품명","현재재고병수","안전재고","월판매량","일평균출고","재고소진일수","발주리드타임일","발주상태"])
    for p in PRODUCTS:
        sku=p[0]; name=p[2]; safety=p[11]
        monthly = sold.get(sku,0)
        daily = round(monthly/26, 1) if monthly else 0.1   # 펍 영업일 기준 약 26일
        # 잔여재고: 의도적으로 1~2종은 안전재고 근접/이하(발주 경보)
        if sku=="TEO-750":   cur = int(safety*0.7)     # 경보
        elif sku=="SAN-750": cur = int(safety*0.9)     # 주의
        elif sku=="DAE-375": cur = int(safety*2.6)
        else:                cur = int(safety*random.uniform(1.6,3.2))
        days_left = round(cur/daily,1) if daily else 999
        lead = 14  # 양조 리드타임(발효 포함) 길다
        if cur<=safety: st="발주필요"
        elif days_left<=lead: st="발주임박"
        else: st="정상"
        w.writerow([sku,name,cur,safety,monthly,daily,days_left,lead,st])

# ── 4) content.csv (SNS + 펍 이벤트) ──────────────────────────────────
# 급등일과 게시일을 겹치게(콘텐츠가 매출 0일 선행) → 데모 "아하"
content_rows = [
    # 게시일, 채널, 유형, 주제, 연동SKU, 도달, 좋아요, 댓글, 저장, 펍예약, 비고
    ("2026-05-08","인스타","릴스","금요일 펍 페어링 나이트 - 욕망의 거친 물결","YOK-750", 24800, 1820, 96, 410, 38, "펍 이벤트 연동"),
    ("2026-05-13","인스타","캐러셀","여름 신상 산뜻 출시 (자사몰 단독)","SAN-750", 17600, 1410, 72, 520, 0, "자사몰 런칭"),
    ("2026-05-17","인스타","스토리","청년농부 협업 아침에쌀 비하인드","ACH-500", 9200, 640, 31, 180, 0, "스마트스토어 유도"),
    ("2026-05-23","인스타","피드","텃밭 페어링 모임 모집 (토요일)","TEO-750", 14300, 1180, 88, 360, 30, "펍 이벤트 연동"),
    # 평상시 콘텐츠(저성과·비연동)
    ("2026-05-02","인스타","피드","주말 영업 안내",        "", 4200, 210, 8, 22, 0, ""),
    ("2026-05-06","인스타","스토리","오늘의 탭 리스트",      "", 3100, 0, 0, 0, 0, ""),
    ("2026-05-15","인스타","피드","비취색 브랜드 이야기",   "", 6800, 540, 24, 130, 0, ""),
    ("2026-05-20","인스타","릴스","양조 과정 타임랩스",     "", 11200, 880, 41, 240, 0, ""),
    ("2026-05-27","인스타","스토리","주중 한산한 시간 추천", "", 2700, 0, 0, 0, 0, ""),
    ("2026-05-30","인스타","피드","6월 클래스 예고",        "", 5600, 430, 19, 95, 12, "펍 클래스 모집"),
]
with open(f"{OUT}/content.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.writer(f)
    w.writerow(["게시일","채널","유형","주제","연동SKU","도달","좋아요","댓글","저장","펍예약","비고"])
    w.writerows(content_rows)

print(f"sales rows: {len(rows)}")
print(f"products: {len(PRODUCTS)}  content: {len(content_rows)}")
