## Overview

꿀꺽하우스의 비주얼 표면은 따뜻한 미색 캔버스(`{colors.canvas}` — #F4EFE6) 위에 **비취색(jade)**을 주연으로 세운다. 비취색은 구리가 시간을 거쳐 산화하며 얻는 청록빛, 청자 유약의 깊은 푸른빛에서 온 색이다 — 우리술이 발효를 거쳐 색과 맛을 얻는 과정과 같은 맥락의 색이다. 캔버스는 거친 콘크리트의 회색기와 따뜻한 목재의 베이지를 섞은 톤으로, 광안리 양조장 겸 브루펍의 물성(거친 콘크리트 · 따뜻한 목재 · 산화 구리)을 그대로 옮긴다.

브랜드 에너지는 **곡선**에서 나온다. "꿀꺽-" 하고 삼키는 순간의 목젖, 파도처럼 거친 물결, 그리고 바를 감싸는 곡선형 테이블 — 이 세 곡선이 하나의 모티프로 묶인다. 시스템 곳곳의 구획은 직각이 아니라 **물결 곡선(`{component.wave-divider}`)**과 **아치(`{component.arch-frame}`)**로 끊긴다. 아치는 병의 어깨선, 잔의 곡면, 양조장 입구의 곡면 천장을 환기한다. 직선 박스는 최소화하고, 모서리는 넉넉히 굴린다(`{rounded.lg}` 이상이 기본).

타입 보이스는 **한글 세리프(본명조 계열)**를 디스플레이로, **고딕 산세리프(본고딕 계열)**를 본문으로 쓴다. 디스플레이 세리프는 가양주의 손맛·정성을, 본문 고딕은 현대적 또렷함을 맡는다. 영문 표기는 'G'를 살린 부드러운 어감(`GGULGGEOK`)을 소문자 위주로 둔다. 헤드라인은 과하게 키우지 않고, 비취색 한 줄과 물결 곡선 하나로 무게를 잡는다.

**Key Characteristics:**
- 따뜻한 미색 캔버스(`{colors.canvas}` — #F4EFE6)에 비취색(`{colors.jade}` — #1F7A6D) 주연. 어두운 표면은 산화 구리 톤(`{colors.copper-oxide}`)으로만 가끔 등장한다.
- 디스플레이는 한글 세리프(본명조 계열), 본문은 고딕(본고딕 계열). 손맛 세리프 + 또렷한 고딕의 대비가 편집 시그니처.
- 곡선이 브랜드 전압. 구획은 직선 대신 **물결 곡선 디바이더**와 **아치 프레임**으로 끊는다.
- 모서리는 넉넉히 굴린다. `{rounded.lg}`(20px)가 카드 기본, 버튼은 `{rounded.full}`(알약형)이 기본.
- 비취색은 강조·CTA·핵심 수치에만. 면 전체를 비취로 칠하지 않는다 — 미색 위에 비취 한 줄이 원칙.
- 산화 구리(`{colors.copper-oxide}`)는 비취의 보조 강조. 펍 이벤트·시즈널 배지처럼 "따뜻함"이 필요한 자리.
- 여백은 발효처럼 느긋하게. 주요 밴드 사이 `{spacing.section}`(80px), 카드 내부 `{spacing.lg}`(24px).
- 사진은 술의 색(유자빛·복분자빛)과 잔의 곡면을 살린 근접 샷. 아치 프레임 안에 담아 곡선을 강화.

## Colors

### Brand & Accent
- **Jade** (`{colors.jade}` — #1F7A6D): 시스템 주연색. 디스플레이 헤드라인 강조, 핵심 수치(매출·순마진), 1차 버튼 면, 물결 디바이더에 쓴다. 비취색은 꿀꺽하우스의 정체성 그 자체다.
- **Jade Deep** (`{colors.jade-deep}` — #145A50): 비취의 짙은 변주. 버튼 눌림 상태, 헤더 바, 깊이가 필요한 강조에.
- **Jade Soft** (`{colors.jade-soft}` — #D7E8E3): 비취의 옅은 틴트. 표·KPI 카드의 강조 배경, 선택 상태에.
- **Copper Oxide** (`{colors.copper-oxide}` — #B5703A): 산화 구리에서 온 따뜻한 보조 강조. 펍 이벤트·시즈널 배지, 발주 주의 같은 "온기"가 필요한 자리. CTA 색 아님.
- **Yuja** (`{colors.yuja}` — #E8B23A): 욕망의 거친 물결(유자·스피어민트)을 환기하는 제품 액센트. 차트의 시그니처 SKU 계열, 하이라이트 점에만 소량.

### Surface
- **Canvas** (`{colors.canvas}` — #F4EFE6): 모든 표면의 바닥. 거친 콘크리트 + 목재를 섞은 따뜻한 미색.
- **Surface Soft** (`{colors.surface-soft}` — #EDE6D8): 캔버스보다 한 단계 짙은 톤. 표 셀·푸터 인접 스트립.
- **Surface Card** (`{colors.surface-card}` — #FBF8F1): 카드·패널 배경. 캔버스보다 밝아 카드가 떠 보인다.
- **Surface Dark** (`{colors.surface-dark}` — #2A2723): 산화 구리·목재가 짙게 깔린 어두운 밴드. CTA 밴드·푸터에 가끔.
- **Concrete** (`{colors.concrete}` — #C9C1B3): 거친 콘크리트 톤. 비활성 표면·플레이스홀더.

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` — #D8CEBE): 미색 표면 위 1px 구분선. 표 행·카드 외곽·섹션 사이.
- **Hairline Strong** (`{colors.hairline-strong}` — #B9AD98): 강조 구분선. 표 헤더 하단·중요 구획.

### Text
- **Ink** (`{colors.ink}` — #2A2723): 모든 헤드라인·본문 기본 잉크. 순흑이 아닌 짙은 목재 갈색.
- **Body** (`{colors.body}` — #5A5348): 본문 running-text. 잉크보다 부드럽다.
- **Muted** (`{colors.muted}` — #8C8475): 캡션·메타·푸터 링크.
- **On Jade** (`{colors.on-jade}` — #F4EFE6): 비취색 면 위에 얹는 글자(미색).

### Semantic
- **Warning** (`{colors.warning}` — #C0552E): 발주 필요·마진 누수 경보. 산화 구리 계열의 따뜻한 경고.
- **Caution** (`{colors.caution}` — #C98A2B): 발주 임박·주의. 경보보다 한 단계 약한 신호.
- **Success** (`{colors.success}` — #2E8B6B): 정상 재고·목표 달성. 비취 계열로 자연스럽게.

## Typography

### Font Family
디스플레이는 **한글 세리프(본명조 / Nanum Myeongjo 계열)**, 본문은 **고딕 산세리프(본고딕 / Pretendard·Noto Sans KR 계열)**. 영문은 본문 고딕과 같은 스택을 공유한다. fallback 스택은 `"Nanum Myeongjo", "Apple SD Gothic Neo", serif`(디스플레이) / `"Pretendard", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif`(본문).

세리프 디스플레이는 가양주의 손맛·정성을, 고딕 본문은 현대적 또렷함을 맡는다 — 이 대비가 편집 시그니처다. 디스플레이를 고딕으로, 본문을 세리프로 바꾸면 브랜드 보이스가 흐려진다.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 56px | 700 (세리프) | 1.1 | -0.5px | 표지 h1 ("이번 격주, 무엇이 팔렸나") |
| `{typography.display-lg}` | 40px | 700 (세리프) | 1.15 | -0.5px | 섹션 헤드 |
| `{typography.display-md}` | 30px | 700 (세리프) | 1.2 | -0.3px | 서브섹션·제품명 |
| `{typography.title-lg}` | 22px | 600 (고딕) | 1.35 | 0 | 카드 제목·KPI 라벨 |
| `{typography.title-md}` | 18px | 600 (고딕) | 1.4 | 0 | 표 헤더·리드 문장 |
| `{typography.metric}` | 34px | 700 (고딕) | 1.1 | -0.3px | KPI 수치(매출·순마진·재고일수) |
| `{typography.label-uppercase}` | 13px | 600 (고딕) | 1.3 | 1.2px | 카테고리 라벨·탭 ("시그니처 · 시즈널") |
| `{typography.body-md}` | 16px | 400 (고딕) | 1.65 | 0 | 기본 본문 |
| `{typography.body-sm}` | 14px | 400 (고딕) | 1.6 | 0 | 표 본문·푸터·각주 |
| `{typography.caption}` | 12px | 400 (고딕) | 1.4 | 0.3px | 사진 캡션·출처 |
| `{typography.button}` | 15px | 600 (고딕) | 1.0 | 0.3px | 버튼 라벨 |

### Principles
디스플레이 세리프(700)와 본문 고딕(400)의 대비를 항상 유지한다 — 손맛과 또렷함의 거리가 시그니처다. 본문 행간은 넉넉히(1.6~1.65) 두어 발효처럼 여유 있는 호흡을 만든다. KPI 수치만은 고딕 700(`{typography.metric}`)으로 또렷하게 — 숫자는 손맛보다 정확함이 먼저다. 카테고리 라벨은 1.2px 자간으로 살짝 벌려 "라벨"임을 표시한다.

### Note on Font Substitutes
본명조가 없으면 **Noto Serif KR** 700이 가장 가깝다. 본고딕이 없으면 **Pretendard**(없으면 Noto Sans KR)로 대체한다. 디스플레이 세리프 대체 시 자간을 -0.5px로 좁혀 본명조의 또렷한 글자폭을 맞춘다.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 40px · `{spacing.xxl}` 56px · `{spacing.section}` 80px.
- **Section padding (vertical):** `{spacing.section}`(80px) 주요 밴드 사이.
- **Hero/표지 밴드:** `{spacing.xxl}`(56px) 내부 상하 패딩.
- **Card internal padding:** `{spacing.lg}`(24px) 콘텐츠·KPI 카드 / `{spacing.xl}`(40px) 표 셀 묶음.
- **Gutters:** `{spacing.lg}`(24px) 카드 그리드 / `{spacing.md}`(16px) 푸터 컬럼.

### Grid & Container
- **Max content width:** ~960px 중앙 정렬(A4 보고서 PDF 기준). 대시보드 HTML은 ~1200px.
- **편집 본문:** 단일 12컬럼 그리드. 물결 디바이더는 풀블리드(여백 없이 가로 전체).
- **카드 그리드:** 데스크탑 3-up, 태블릿 2-up, 모바일 1-up.
- **푸터:** 데스크탑 3컬럼, 모바일 1컬럼.

### Whitespace Philosophy
꿀꺽하우스는 여백을 발효 시간처럼 다룬다 — 채우기보다 비워서 술의 색과 곡선이 숨 쉬게 한다. 여백이 등장하는 자리(섹션 사이·CTA 둘레)는 항상 균일한 `{spacing.section}`(80px). 그라데이션이나 장식 배경은 깔지 않는다 — 빈 자리는 따뜻한 미색 캔버스로 둔다. 단, 구획을 끊을 때만은 직선 대신 물결 곡선을 쓴다.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | 그림자 없음, 테두리 없음 | 본문 섹션·상단 바·푸터 |
| Soft hairline | 1px `{colors.hairline}` 테두리 | 섹션 구분·카드 외곽·표 행 |
| Card surface | `{colors.surface-card}` 배경 + 아주 옅은 그림자 (0 2px 8px rgba(42,39,35,0.06)) | KPI 카드·콘텐츠 카드 |
| Arch frame | 아치형 상단을 가진 사진/콘텐츠 프레임 | 제품 근접 샷·표지 비주얼 |

깊이는 두꺼운 그림자가 아니라 **곡선과 색의 따뜻함**에서 온다. 카드는 미색 캔버스 위에 한 톤 밝은 `{colors.surface-card}`로 살짝 떠 있고, 그림자는 거의 보이지 않을 만큼 옅게만 둔다.

### Decorative Depth
- **Wave Divider** (`{component.wave-divider}`): 가로 풀블리드 물결 곡선 SVG. 높이 24~40px, 선/면 모두 비취색(`{colors.jade}`) 또는 옅은 비취(`{colors.jade-soft}`). 섹션을 끊는 시스템의 시그니처 장식. 파도처럼 거친 물결을 환기한다.
- **Arch Frame** (`{component.arch-frame}`): 상단이 아치(반원/완만한 곡선)로 마감된 프레임. 제품 사진·표지 비주얼을 담는다. 병의 어깨선과 잔의 곡면을 환기.
- **Jade Underline**: 디스플레이 헤드라인 아래 깔리는 짧은 비취색 곡선 밑줄(직선 밑줄 아님). 무게를 잡는 최소 장식.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | 거의 안 씀 — 풀블리드 사진 가장자리 한정 |
| `{rounded.sm}` | 8px | 배지·작은 태그·인풋 |
| `{rounded.md}` | 14px | 표 컨테이너·작은 카드 |
| `{rounded.lg}` | 20px | 카드·패널 기본 반경 |
| `{rounded.xl}` | 32px | 큰 패널·표지 비주얼 컨테이너 |
| `{rounded.full}` | 9999px | 버튼(알약형)·아이콘 버튼·KPI 칩 |

반경 위계는 "기본적으로 넉넉히, 버튼은 알약형". 직각은 사진 가장자리에만 허용한다. 굴린 모서리와 곡선이 "삼킴·물결·아치"의 부드러움을 만든다 — 직각 박스는 이 브랜드의 보이스가 아니다.

### Photography Geometry
제품 근접 샷은 아치 프레임(`{component.arch-frame}`) 안에 담아 곡선을 강화한다. 술의 색(유자빛·복분자빛)과 잔의 곡면이 주제. 펍 이벤트 사진은 3:2 가로, 제품 단품 샷은 4:5 세로 아치. 풀블리드가 필요한 표지 비주얼은 상단만 아치로 마감하고 좌우는 가장자리까지 채운다.

## Components

### Top Navigation / Header
**`top-bar`** — 보고서/대시보드 상단 바. 높이 60px, 배경 `{colors.surface-card}`, 하단에 `{component.wave-divider}` 한 줄. 좌측에 'GGULGGEOK' 워드마크(소문자 + 삼킴 심볼), 우측에 기간·격주 회차 라벨(`{typography.label-uppercase}`). 글자는 잉크색.

### Buttons
**`button-primary`** — 1차 CTA. 배경 `{colors.jade}`, 글자 `{colors.on-jade}`(미색), 반경 `{rounded.full}`(알약형), 패딩 14px × 28px, 높이 48px. 타입 `{typography.button}`. 눌림 상태는 배경 `{colors.jade-deep}`.

**`button-secondary`** — 2차 버튼. 배경 투명, 1px `{colors.jade}` 테두리, 글자 `{colors.jade}`, 반경 `{rounded.full}`. 비취 위가 아닌 미색 면에서.

**`button-icon`** — 원형 아이콘 버튼. 44 × 44px, 배경 `{colors.surface-soft}`, 비취색 아이콘, 반경 `{rounded.full}`.

**`text-link`** — 인라인 링크("전체 보기 →"). `{typography.label-uppercase}`, 비취색, 밑줄 없음. 화살표 → 글리프 동반.

### Cards & Containers
**`kpi-card`** — 대시보드/보고서 상단 핵심 지표 카드. 배경 `{colors.surface-card}`, 반경 `{rounded.lg}`, 패딩 `{spacing.lg}`. 상단에 라벨(`{typography.label-uppercase}`, 뮤트색), 가운데 수치(`{typography.metric}`, 비취색), 하단에 **"그래서 무슨 의미" 한 줄**(`{typography.body-sm}`, 본문색) — 수치만 있는 카드는 미완성으로 본다. 강조가 필요하면 배경을 `{colors.jade-soft}`로.

**`content-card`** — 3-up 그리드의 콘텐츠/제품 카드. 배경 `{colors.surface-card}`, 반경 `{rounded.lg}`, 내부 패딩 `{spacing.lg}`. 상단에 아치 프레임 사진(`{component.arch-frame}`), 아래 카테고리 배지(`{component.badge-category}`) + 제목(`{typography.title-lg}`) + 짧은 본문.

**`arch-frame`** — 상단이 아치로 마감된 사진/콘텐츠 프레임. 제품 근접 샷·표지 비주얼을 담는다. 좌우·하단은 직선, 상단만 반원/완만한 곡선. 반경 `{rounded.xl}` 상단 한정.

**`data-table`** — 분석 보고서의 핵심. 컨테이너 반경 `{rounded.md}`, 배경 `{colors.surface-card}`. 헤더 행은 배경 `{colors.jade-soft}` + 하단 `{colors.hairline-strong}` 1px. 본문 행은 `{colors.hairline}` 1px로 구분. 숫자 셀은 우측 정렬. 강조 행(시그니처 SKU·경보)은 좌측에 비취색 또는 산화 구리 4px 막대.

**`alert-row`** — 발주 경보 행. 배경 옅은 경고 틴트, 좌측 4px `{colors.warning}`(발주필요) 또는 `{colors.caution}`(발주임박) 막대. 상태 배지를 행 우측에.

### Badges
**`badge-category`** — 제품 카테고리 배지("시그니처 · 시즈널 · 협업"). 배경 `{colors.jade-soft}`, 글자 `{colors.jade-deep}`, 반경 `{rounded.sm}`, 타입 `{typography.label-uppercase}`.

**`badge-event`** — 펍 이벤트·시즌 배지. 배경 옅은 산화 구리 틴트, 글자 `{colors.copper-oxide}`, 반경 `{rounded.full}`(알약형).

### Inputs & Forms
**`text-input`** — 텍스트 인풋. 배경 `{colors.surface-card}`, 글자 잉크색, 반경 `{rounded.sm}`, 패딩 12px × 16px, 높이 46px, 1px `{colors.hairline}` 테두리. 포커스 시 테두리가 `{colors.jade}`로.

### Signature Components
**`wave-divider`** — 가로 풀블리드 물결 곡선. 섹션을 끊는 시스템의 가장 distinctive한 장식. 비취색 또는 옅은 비취. 직선 구분선 대신 이걸 쓴다.

**`cta-band`** — 보고서/대시보드 하단 행동 유도 밴드. 배경 `{colors.surface-dark}`(산화 구리 짙은 톤), 글자 미색, 중앙 헤드라인(`{typography.display-md}`) + `{component.button-primary}`. 상단을 `{component.wave-divider}`로 마감.

### Footer
**`footer`** — 보고서/페이지를 닫는 푸터. 배경 `{colors.surface-soft}`, 글자 뮤트색. 좌측 'GGULGGEOK · 부산 광안리' 워드마크, 우측 격주 회의 회차·작성일. 상단에 `{component.wave-divider}`.

## Do's and Don'ts

### Do
- 미색 캔버스 위에 비취색 한 줄. 비취는 강조·CTA·핵심 수치에만.
- 구획은 직선 대신 물결 곡선(`{component.wave-divider}`)으로 끊는다.
- 제품 사진은 아치 프레임(`{component.arch-frame}`) 안에. 곡선이 브랜드 보이스다.
- 디스플레이는 세리프(700), 본문은 고딕(400). 손맛 + 또렷함의 대비를 유지.
- KPI 카드의 수치 아래 "그래서 무슨 의미" 한 줄을 항상 붙인다.
- 모서리는 넉넉히(`{rounded.lg}` 이상). 버튼은 알약형(`{rounded.full}`).
- 산화 구리(`{colors.copper-oxide}`)는 펍 이벤트·시즌의 "온기" 자리에만.

### Don't
- 비취색·산화 구리·유자빛 밖의 브랜드 색을 새로 들이지 않는다.
- 면 전체를 비취색으로 칠하지 않는다. 미색 위 비취 한 줄이 원칙.
- 직각 박스를 기본으로 쓰지 않는다. 굴린 모서리와 곡선이 "삼킴·물결·아치"의 보이스.
- 디스플레이를 고딕으로, 본문을 세리프로 바꾸지 않는다 — 대비가 무너진다.
- 그라데이션·장식 배경을 깔지 않는다. 빈 자리는 미색으로 둔다.
- 수치만 있는 KPI 카드를 두지 않는다 — 의미 한 줄이 없으면 미완성.
- 산화 구리를 CTA 색으로 쓰지 않는다. CTA는 비취색.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | 햄버거 없음(보고서형); 표지 h1 56→34px; 카드 1-up; 표 가로 스크롤; 푸터 3 → 1컬럼 |
| Tablet | 768–1024px | 카드 2-up; KPI 카드 2-up; 표 전체 표시 |
| Desktop | 1024–1200px | 카드 3-up; KPI 카드 4-up; 표 전체 |
| Wide | > 1200px | 데스크탑과 동일, 여백만 넉넉. max 1200px(대시보드) / 960px(보고서) |

### Touch Targets
- `{component.button-primary}`는 최소 48 × 48px.
- `{component.button-icon}`는 44 × 44px.
- `{component.text-input}` 높이 46px.
- 표 행 탭 영역은 주변 패딩 포함 44px 이상.

### Collapsing Strategy
- 물결 디바이더는 모든 브레이크포인트에서 풀블리드 유지 — 여백 안으로 들어가지 않는다.
- 카드 그리드는 카드를 줄이기보다 컬럼 수를 줄인다. 아치 프레임 사진은 native 비율 유지.
- 데이터 표는 데스크탑에서 전체, 모바일에서 가로 스크롤(핵심 컬럼 고정).
- KPI 카드는 4-up → 2-up → 1-up. 수치는 `{typography.metric}` 크기 유지.
- 아치 곡선의 곡률은 폭에 비례해 완만해진다.

### Image Behavior
- 제품 근접 샷은 아치 프레임 안에서 비율 유지. 잘림은 상단 아치 마스크로만.
- 펍 이벤트 사진은 native 비율 유지, 레터박스/필러박스 금지.
- 워드마크는 뷰포트 폭에 비례해 스케일.

## Iteration Guide

1. 한 번에 한 컴포넌트만. YAML 키로 참조(`{component.kpi-card}`, `{component.wave-divider}`).
2. 새 컴포넌트는 `{rounded.lg}`(20px)를 기본으로. 버튼·칩은 `{rounded.full}`.
3. variant(`-active`, `-alert`)는 `components:`의 별도 항목으로.
4. 모든 참조는 `{token.refs}`로 — 인라인 hex 금지.
5. hover 상태는 문서화하지 않는다. default와 active/pressed만.
6. 디스플레이는 세리프 700, 본문은 고딕 400. 대비를 흐리지 않는다.
7. 비취색은 강조·CTA·핵심 수치 전용. 면 전체 칠하기로 확장하지 않는다.
8. 강조가 고민되면: 더 큰 글자보다 물결 곡선/아치 프레임을 먼저 쓴다.

## Known Gaps

- 비취색 정확한 hex(#1F7A6D)는 청자 유약·산화 구리의 일반 톤에서 도출한 값이다. 꿀꺽하우스 공식 브랜드 가이드의 PANTONE/hex 원본은 미확인 — 자사몰·인스타에서 확인된 "비취색(jade)" 표현과 산화 구리·청자 유약 레퍼런스 기반의 합리적 추정값이다.
- 본명조/본고딕은 한글 전통주 브랜드의 일반적 조합으로 지정했다. 꿀꺽하우스 실제 사용 서체(패키지·간판)는 미확인.
- 물결 곡선·아치의 정확한 곡률 곡선(SVG path)은 디자인 article의 "곡선형 바 테이블 = 꿀꺽 모양" 묘사에서 환기한 것으로, 픽셀 단위 원본은 미확인.
- 로고 'G'·삼킴(목젖) 심볼은 design.co.kr 기사에서 확인했으나 벡터 원본은 미확보 — 워드마크는 텍스트로 대체.
- 애니메이션·전환 타이밍은 범위 밖.
