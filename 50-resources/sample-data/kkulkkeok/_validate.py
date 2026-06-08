#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
꿀꺽하우스 더미데이터 정합성 검증.
1) 채널 단가가 product_master 채널별 가격과 일치하는가 (불일치 0)
2) 주문 단위 일관성(같은 주문번호의 배송지/상태/시간 단일)
3) 가격 구조 정가>자사몰>펍/스토어>B2B
4) 콘텐츠 연동일이 일 총매출 +30%↑ & 대상 SKU 중앙값 대비 2배+로 검출되는가
실행: python3 _validate.py   (모두 PASS여야 데모 가능)
"""
import csv, statistics, sys
from collections import defaultdict

D = __file__.rsplit("/", 1)[0]
CH_PRICE_COL = {"브루펍포스":"브루펍판매가","자사몰":"자사몰판매가",
                "스마트스토어":"스마트스토어판매가","B2B유통":"B2B공급가"}

prices = {}
master = {}
with open(f"{D}/product_master.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        master[r["SKU"]] = r
        prices[r["SKU"]] = {ch: int(r[col]) for ch, col in CH_PRICE_COL.items()}

# 콘텐츠 연동일 (content.csv의 연동SKU 비어있지 않은 행에서 도출)
spikes = {}
with open(f"{D}/content.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        if r["연동SKU"]:
            spikes[r["게시일"]] = r["연동SKU"]

day_total = defaultdict(int)
day_sku = defaultdict(lambda: defaultdict(int))
order_attr = defaultdict(set)
mismatch = 0
with open(f"{D}/sales.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        d, sku, ch = r["주문일"], r["SKU"], r["채널"]
        day_total[d] += int(r["합계"])
        day_sku[d][sku] += int(r["수량"])
        order_attr[r["주문번호"]].add((r["배송지역"], r["주문상태"], r["주문시간"]))
        if prices[sku][ch] != int(r["단가"]):
            mismatch += 1

fails = []

# 1) 단가 정합
print(f"[1] 채널 단가 불일치 라인: {mismatch}", "PASS" if mismatch==0 else "FAIL")
if mismatch: fails.append("price-mismatch")

# 2) 주문 단위 일관성
bad_order = [o for o, v in order_attr.items() if len(v) > 1]
print(f"[2] 주문 단위 일관성 위반: {len(bad_order)}", "PASS" if not bad_order else "FAIL")
if bad_order: fails.append("order-unit")

# 3) 가격 구조
struct_ok = True
for sku, m in master.items():
    msrp, mall, pub, sst, b2b = (int(m["정가"]), int(m["자사몰판매가"]),
        int(m["브루펍판매가"]), int(m["스마트스토어판매가"]), int(m["B2B공급가"]))
    if not (msrp > mall >= pub and pub > b2b and msrp > sst):
        struct_ok = False
        print(f"    구조 위반 {m['상품명']}: 정가{msrp} 자사몰{mall} 펍{pub} 스토어{sst} B2B{b2b}")
print(f"[3] 가격 구조(정가>자사몰>펍/스토어>B2B):", "PASS" if struct_ok else "FAIL")
if not struct_ok: fails.append("price-structure")

# 4) 콘텐츠 연동일 급등 검출
avg = statistics.mean(day_total.values())
sku_daily = defaultdict(list)
for d in sorted(day_total):
    for s in prices:
        sku_daily[s].append(day_sku[d].get(s, 0))
sku_med = {s: statistics.median(v) for s, v in sku_daily.items()}
print(f"[4] 콘텐츠 연동일 검출 (일평균매출 {avg:,.0f}):")
detect_ok = True
for d, sku in sorted(spikes.items()):
    ratio = day_total[d] / avg
    med = sku_med[sku] or 1
    skux = day_sku[d][sku] / med
    fd, fs = ratio >= 1.30, skux >= 2.0
    detect_ok = detect_ok and fd and fs
    print(f"    {d} {sku}: 일매출 {ratio:.2f}x[{'OK' if fd else 'NO'}] "
          f"SKU {day_sku[d][sku]}병 vs중앙 {med:.0f} = {skux:.1f}x[{'OK' if fs else 'NO'}]")
print(f"    => 연동일 전수 검출:", "PASS" if detect_ok else "FAIL")
if not detect_ok: fails.append("spike-detection")

print()
if fails:
    print("검증 실패:", ", ".join(fails)); sys.exit(1)
print("모든 검증 통과. 데모 사용 가능.")
