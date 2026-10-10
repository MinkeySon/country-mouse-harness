## Overview

Sigolzwi (시골쥐) is a bank-agnostic money diary — it gathers deposits and withdrawals from many banks into one calendar, shows where each expense happened on a map, and lets the user annotate transactions (splits, unpaid shares). Its interface is engineered to be calm, modern, and easy to read at a glance: near-black ink (`{colors.ink}` — #141414) on a clean off-white canvas (`{colors.canvas}` — #FDFDFD), with structure carried by a ladder of barely-perceptible neutral tints rather than by shadows or decoration. Numbers are the hero. Everything else stays quiet so amounts, dates, and places read instantly.

Color does exactly one job: **blue means money coming in, or "this is selected."** One electric blue (`{colors.accent}` — #0055FF) marks deposit amounts, the selected day, the active segment, and map pins. Withdrawals are never red — they are set in plain ink with a minus sign, so spending feels like a calm record instead of an alarm. Because blue is scarce, a blue element always tells the user something meaningful.

The geometry carries the friendly, rustic-but-modern personality (the "country mouse" — small, frugal, unfussy). Every interactive element is a stadium pill (`{rounded.full}`): buttons, chips, the floating tab bar, the year/month/day switcher. Containers sit at a soft `{rounded.md}` (24px) and rows at `{rounded.sm}` (16px). Bank marks render as iOS-style squircles at 30% radius with a single-letter monogram, standing in for real bank logos. Type is Noto Sans KR with strong weight contrast — Bold 700 for headings and big totals, Regular 400 for text — with tabular numerals so amounts align vertically.

A small line-drawn country mouse appears only in onboarding and empty states, in muted ink, never in the working screens.

**Key Characteristics:**

- Clean off-white monochrome — `{colors.ink}` on `{colors.canvas}`, with `{colors.accent}` blue as the only brand chroma
- Blue = deposit / selected / map pin. Ink = withdrawal and everything else. Red is never used for money
- Stadium-pill interaction language: buttons, chips, segmented switcher, floating tab bar
- Shadow-free elevation — hierarchy from a neutral tint ladder (`{colors.canvas-soft}`, `{colors.field}`, `{colors.hairline}`) and 1px hairlines
- Noto Sans KR with weight contrast and tabular numerals; large totals, small quiet labels
- Squircle bank monograms (30% radius) as the recurring motif in day view and account lists
- Progressive detail: year → month → day → bank → transaction → map, each step a calm zoom, never a jump
- Warm and short Korean copy (해요체), never alarming

## Colors

Source screens: month calendar, year calendar, day detail, transaction + map, settlement, accounts, settings.

### Brand & Accent

- **Ink Black** (`{colors.primary}` — #141414): The brand color. Fills every primary CTA pill and all display typography, including withdrawal amounts.
- **Electric Blue** (`{colors.accent}` — #0055FF): The single chromatic accent. Used for deposit amounts (`+1,250,000원`), the selected calendar day, the active segment, the "today" dot, and map pins. Never used as a button fill.
- **Blue Wash** (`{colors.accent-soft}` — #EAF0FF): Pale tint behind the selected day, and behind deposit-heavy cells.

### Surface

- **Canvas** (`{colors.canvas}` — #FDFDFD): Default app background.
- **Paper** (`{colors.paper}` — #FFFFFF): Cards, bottom sheets, and map bubbles that sit on the canvas.
- **Soft Canvas** (`{colors.canvas-soft}` — #F3F3F3): The workhorse tint. Calendar day cells, the floating tab bar, chips, segmented-control tracks.
- **Field** (`{colors.field}` — #F0F0F0): Fill for text inputs and the memo box, no border.
- **Soft Hairline** (`{colors.hairline-soft}` — #F0F0F0): 1px outline on white cards (bank group cards, settlement cards).
- **Hairline** (`{colors.hairline}` — #E0E0E0): Stronger 1px border on outlined pill buttons and list dividers.
- **Spend Ladder** (`{colors.spend-1}` #EEEEEE → `{colors.spend-2}` #E0E0E0 → `{colors.spend-3}` #CFCFCF): Three neutral steps used to shade calendar cells by how much was spent that day. Heat is shown by gray depth, never by hue.

### Text

- **Ink** (`{colors.ink}` — #141414): Headings, body copy, withdrawal amounts.
- **Muted** (`{colors.text-muted}` — #707070): Secondary copy — times, account names, labels.
- **Faint** (`{colors.text-faint}` — #ADADAD): Placeholders, disabled, days outside the current month, settled participants.
- **On Primary** (`{colors.on-primary}` — #FFFFFF): Text on ink or blue fills.

### Semantic

Kept deliberately small. State stays inside the monochrome ladder wherever possible.

- **Warn Amber** (`{colors.warn}` — #C77A1E on `{colors.warn-soft}` #FFF3E3): Only for "needs attention" that is not an error — unsettled amounts (`미정산`), unmatched place (`위치 미확인`), sync stale.
- **Error Red** (`{colors.error}` — #D64545): System failures only — sync failed, re-authentication required, destructive confirm. **Never applied to a transaction amount.**
- Settled/done states use `{colors.text-faint}` plus a check icon, not green.

## Typography

### Font Family

**Noto Sans KR** — a Korean–Latin sans-serif used exclusively, across every screen and role (available in Figma by default). In Figma use static weights (Light 300 · Regular 400 · Medium 500 · Bold 700). Fallback stack: `-apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", sans-serif`.

Sizes are set for the mobile baseline frame (390×844). Korean glyphs need more vertical room than Latin, so headings sit at 1.3–1.35 and body at 1.5.

### Hierarchy

| Token                    | Size | Weight | Line Height | Letter Spacing | Use                                                          |
| ------------------------ | ---- | ------ | ----------- | -------------- | ------------------------------------------------------------ |
| `{typography.display}`   | 32px | 700    | 1.3         | 0              | Month/year totals ("-1,240,000원"), transaction amount       |
| `{typography.heading-1}` | 28px | 700    | 1.3         | 0              | Screen titles ("9월", "9월 30일")                            |
| `{typography.heading-2}` | 22px | 700    | 1.35        | 0              | Section headings ("은행별 내역")                             |
| `{typography.heading-3}` | 18px | 700    | 1.35        | 0              | Bank name, merchant name in sheet                            |
| `{typography.title}`     | 17px | 500    | 1.4         | 0              | Emphasized rows, group totals                                |
| `{typography.body-lg}`   | 17px | 300    | 1.5         | 0              | Light lead lines under a display number                      |
| `{typography.body}`      | 15px | 400    | 1.5         | 0              | Default body, transaction merchant names                     |
| `{typography.amount}`    | 16px | 500    | 1.4         | 0              | Amounts in lists (tabular numerals)                          |
| `{typography.body-sm}`   | 13px | 400    | 1.5         | 0              | Supporting copy, account masks, times                        |
| `{typography.label}`     | 12px | 500    | 1.4         | 0              | Badge and chip labels                                        |
| `{typography.cell}`      | 11px | 500    | 1.2         | 0              | Amounts inside calendar cells (abbreviated: `125만`, `3.2만`)|
| `{typography.caption}`   | 12px | 400    | 1.4         | 0              | Captions, metadata, form fine print                          |

### Principles

- **Numbers are the hero.** Totals are set at display size in Bold; everything around them is small and muted. Pair a 32px 700 total over a 17px 300 lead line for hierarchy without color.
- **Tabular numerals always** (`font-variant-numeric: tabular-nums`) so digits align in columns.
- **Amount format is fixed.** Full form: thousands separators + `원`, sign first — `+1,250,000원` (blue) / `-12,800원` (ink). Inside calendar cells only, abbreviate: `125만`, `3.2만`, `8,500`.
- **Zero letter-spacing everywhere.** No all-caps; sentence case only.

## Layout

### Spacing System

- **Base unit**: 8px, with 4px half-steps
- **Tokens**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.section}` 40px
- Screen side padding is `{spacing.md}` (16px). Card inner padding `{spacing.md}`; gap between cards `{spacing.sm}`; sections separated by `{spacing.lg}`–`{spacing.section}`
- Buttons are fixed-height (52px) pills; inputs pad `{spacing.sm} {spacing.md}`

### Grid & Container

- Single-column, vertical scroll. One main idea per screen: a calendar, a day's banks, or a place.
- **Month grid**: 7 columns, cells with `{spacing.xxs}` gaps, full width inside 16px side padding. Cell aspect ≈ 1 : 1.25 to fit two amount lines.
- **Year grid**: 3 × 4 month tiles.
- **Floating tab bar** is detached from the screen edge and horizontally centered at the bottom (`{spacing.md}` above the safe area); the canvas visibly wraps around it.
- **Map screen**: the map fills the top ~60% of the screen; a bottom sheet holds the details.

### Whitespace Philosophy

Whitespace is the primary grouping device. Sections are separated by empty canvas with no divider rules; inside cards, `{spacing.md}` padding keeps content off the edges. Density is allowed in exactly one place — the month grid — and everywhere else the screen gives one number room to breathe.

### Responsive Strategy

#### Screen Size

Mobile-first on a single baseline.

| Name             | Width × Height | Notes                                                         |
| ---------------- | -------------- | ------------------------------------------------------------- |
| Baseline         | 390 × 844      | Default design frame for all key screens (Figma)              |
| Minimum          | 360px width    | Month grid must hold without horizontal scroll; amounts abbreviate further |
| Tablet / Desktop | —              | Out of MVP scope                                              |

- Side padding stays 16px at every width.
- At 360px, calendar cells drop the withdrawal line to the abbreviated form first.

#### Touch Targets

- Minimum 44 × 44px. Calendar cells, bank group headers, transaction rows (min 56px tall), chips, and pill buttons all meet this.
- The year/month/day switcher uses full pill segments, not tiny tabs.

#### Collapsing Strategy

- Bank groups in day view are collapsed by default and expand in place on tap.
- The floating tab bar persists on scroll; it hides when the map bottom sheet is expanded to full height.

#### Image Behavior

- Maps use a desaturated grayscale base style so blue pins and amount bubbles are the only color.
- Bank monograms are vector squircles; no raster bank logos until usage terms are confirmed.

## Elevation & Depth

| Level   | Treatment                                       | Use                                                     |
| ------- | ----------------------------------------------- | ------------------------------------------------------- |
| 0       | Flat on `{colors.canvas}`                       | Default — most of every screen                          |
| 1       | `{colors.canvas-soft}` fill, no border          | Calendar cells, tab bar, chips, segmented track         |
| 2       | 1px `{colors.hairline-soft}` outline on white   | Bank group cards, settlement cards                      |
| 3       | `{colors.paper}` sheet with 24px top corners    | Bottom sheets over the map                              |
| Inverse | `{colors.ink}` fill, `{colors.on-primary}` text | Primary CTAs                                            |

The system is essentially shadow-free. Elevation is communicated by fill difference and hairlines. Two exceptions, both because the element floats over a busy map or moving content: the **amount bubble on the map** and the **bottom sheet** may use a very soft shadow (`0 4px 16px rgba(20,20,20,0.08)`); the active segment of the segmented control lifts off its track as a white pill.

### Decorative Depth

- **Zoom transitions** — year → month → day are shown as a 220ms scale-and-fade from the tapped tile/cell into the new view, so the user feels they are "zooming in" on time. No bounce, no spring.
- **Map as depth** — the muted grayscale map is the only textured surface in the app.
- No gradients, no glass/blur on any UI chrome.

## Shapes

### Border Radius Scale

| Token            | Value  | Use                                                                   |
| ---------------- | ------ | --------------------------------------------------------------------- |
| `{rounded.none}` | 0px    | Map, full-bleed                                                       |
| `{rounded.xs}`   | 10px   | Calendar day cells                                                    |
| `{rounded.sm}`   | 16px   | Inputs, transaction rows on a card, month tiles                       |
| `{rounded.md}`   | 24px   | Bank group cards, bottom sheet top corners, settlement cards          |
| `{rounded.full}` | 9999px | Every pill: buttons, chips, badges, segmented switcher, tab bar, amount bubble |

### Icon & Mark Geometry

- **Bank monogram** (`bank-squircle`): 30% radius squircle, 40px in day view, 32px in lists, filled `{colors.canvas-soft}` with the bank's first letter in `{typography.heading-3}` ink.
- **Map pin**: a solid `{colors.accent}` circle (16px) with a 2px white ring; the selected pin scales to 24px.
- **Icons**: 1.5px line style, 24px, `{colors.text-muted}`; the active tab uses the filled variant in ink. Blue is not used for icons except the map pin.
- **Mascot**: single-weight line drawing of a small country mouse in `{colors.text-faint}`, 96–120px, in onboarding and empty states only.

## Components

### Buttons

**`button-primary`** — "은행 연결하기", "저장", "정산 완료"

- Fill `{colors.primary}`, label `{colors.on-primary}` in `{typography.title}`, shape `{rounded.full}`, height 52px, full width at the bottom of a task screen
- One primary button per screen

**`button-outline`** — "나중에 하기", secondary actions

- Fill `{colors.canvas}`, label `{colors.ink}`, 1px `{colors.hairline}` border, `{rounded.full}`

**`button-pill-soft`** — "직접 지정", "다시 연결하기", "오늘"

- Fill `{colors.canvas-soft}`, label `{colors.ink}`, `{rounded.full}`, no border
- Utility pill used inline in rows and headers

### Calendar

**`segmented-control`** + **`segmented-control-active`** — 연 / 월 / 일 switcher

- A `{colors.canvas-soft}` stadium track with three pill segments; the active segment is a `{colors.paper}` white pill with ink label, inactive labels in `{colors.text-muted}`

**`summary-header`** — totals at the top of year/month/day

- No background. Line 1: `{typography.display}` withdrawal total in ink (`-1,240,000원`). Line 2: `{typography.body-lg}` in muted — "입금 +2,300,000원 · 차액 +1,060,000원" with the deposit part in `{colors.accent}`.

**`day-cell`** — a date in the month grid

- Fill `{colors.canvas-soft}` (or a `{colors.spend-1..3}` step by spend size), `{rounded.xs}`
- Top: date number in `{typography.caption}`. Below: deposit total in `{colors.accent}` `{typography.cell}`, withdrawal total in ink `{typography.cell}`. No transactions → leave both lines empty (never "0").
- Today: small `{colors.accent}` dot under the date number. Selected: `{colors.accent-soft}` fill + 1.5px `{colors.accent}` inset ring. Has a memo or split: 4px `{colors.warn}` dot at top-right. Outside current month: numbers in `{colors.text-faint}`, no amounts.

**`month-tile`** — a month in the year grid

- `{colors.canvas-soft}`, `{rounded.sm}`; month name in `{typography.title}`, withdrawal total in ink and deposit total in `{colors.accent}` below.

### Cards & Rows

**`bank-group-card`** — a bank inside day view

- `{colors.paper}` fill, 1px `{colors.hairline-soft}`, `{rounded.md}`
- Header row: `bank-squircle`, bank name in `{typography.heading-3}`, "3건" in muted, right-aligned net amounts (deposit blue / withdrawal ink), chevron. Tapping expands `transaction-row`s inside the card. Collapsed by default.

**`transaction-row`** — one transaction

- Min height 56px, 1px `{colors.hairline}` divider between rows inside a card
- Left: merchant in `{typography.body}`, below it time + account alias in `{typography.body-sm}` muted
- Right: amount in `{typography.amount}` (blue with `+` for deposits, ink with `-` for withdrawals); below it, optional badges (`미정산`, `메모`, `위치 미확인`)

**`settlement-card`** — a split on a transaction

- `{colors.paper}`, 1px `{colors.hairline-soft}`, `{rounded.md}`. Header: "받을 돈 45,000원" in `{typography.title}` on `{colors.warn-soft}` pill. Body: `participant-row`s.

**`participant-row`**

- Name, share amount in `{typography.amount}`, trailing round check toggle ("받음"). Once paid, the whole row fades to `{colors.text-faint}` and the toggle shows a filled ink check.

### Map

**`map-view`**

- Grayscale base map with no extra controls; it shows only the pins for the selected day or bank, never the user's live location.

**`map-pin`** + **`amount-bubble`**

- Pin: solid `{colors.accent}` circle with white ring. Bubble: `{colors.paper}` pill above the pin with the amount in `{typography.amount}` ink, soft shadow allowed. Selected pin is larger and its bubble is `{colors.primary}` fill with `{colors.on-primary}` text.

**`transaction-sheet`** — bottom sheet

- `{colors.paper}`, `{rounded.md}` top corners, 36×4px `{colors.hairline}` grabber. Contents: merchant `{typography.heading-3}`, amount `{typography.display}`, time · bank · account in muted, then memo and split sections.
- Unmatched place: sheet shows a `{colors.warn-soft}` chip "위치 미확인" with a `button-pill-soft` "직접 지정" instead of a pin.
- No-location transaction (transfer, online): a muted note "위치가 없는 거래예요" — not an error.

### Inputs & Forms

**`text-input`**

- `{colors.field}` fill, no border, `{colors.ink}` text with `{colors.text-faint}` placeholder, `{rounded.sm}`, height 48px

**`text-input-focused`**

- Same chrome plus a 2px `{colors.ink}` ring

**`memo-box`**

- Multi-line `text-input`, min height 96px, tag chips below in `{colors.canvas-soft}` pills (`#회식`).

### Navigation

**`tab-bar`** — floating bottom bar

- A stadium pill in `{colors.canvas-soft}`, detached from the edge, three items: `캘린더` · `미정산` · `설정`. Active item is a `{colors.paper}` pill with ink label and filled icon; inactive items are muted line icons.

**`screen-header`**

- Left: `{typography.heading-1}` title (e.g. "9월"), with prev/next as round `button-pill-soft` icons. Right: "오늘" `button-pill-soft`. In deeper screens, a round back button on the left.

### Status & Feedback

**`badge`** — pill, `{typography.label}`

- `미정산` — `{colors.warn}` on `{colors.warn-soft}`; `메모` — muted on `{colors.canvas-soft}`; `위치 미확인` — `{colors.warn}` on `{colors.warn-soft}`; `정산 완료` — muted with a check.

**`sync-banner`**

- Thin full-width strip under the header. Stale: `{colors.warn-soft}` "마지막 동기화 3시간 전". Failed / re-auth: `{colors.error}` text on a pale red tint with a `button-pill-soft` "다시 연결하기". Never covers content.

**`skeleton`**

- Loading is shown as `{colors.canvas-soft}` shapes matching the final layout (cells, rows), never a blank screen or spinner-only.

**`empty-state`**

- Centered mascot line drawing + one short line + at most one button. Examples: "이날은 조용했어요", "아직 연결된 은행이 없어요 · 은행 연결하기".

### Signature Components

**`bank-squircle`** — the recurring 30%-radius monogram tile used for every bank; the app's replacement for logos.

**`amount-text`** — the single component every amount uses: sign, tabular numerals, blue for deposits, ink for withdrawals, full or abbreviated form by context.

**`zoom-transition`** — the 220ms scale-and-fade that links year → month → day and returns to the same scroll position on back.

## Do's and Don'ts

### Do

- Keep the canvas `{colors.canvas}` and let numbers and the map carry the visual interest.
- Use `{colors.accent}` blue only for deposits, selection, and map pins — one or two blue moments per screen.
- Show every amount through `amount-text`: deposits `+` blue, withdrawals `-` ink.
- Use `{rounded.full}` for every tappable control; use `{rounded.md}` for cards and sheets.
- Build depth with tint fills and hairlines; shade busy days with the gray `{colors.spend-1..3}` ladder.
- Show every state: loading skeletons, empty days, unmatched places, no-location transactions, sync failure, re-auth.
- Keep copy warm and short in 해요체: "이날은 조용했어요", "위치를 찾지 못했어요".
- Reveal detail progressively: year → month → day → bank → transaction → map.

### Don't

- Don't color withdrawals red or any warning hue. `{colors.error}` is for system failures only.
- Don't use `{colors.accent}` as a button fill; primary actions are `{colors.primary}` ink pills.
- Don't add more accent hues, gradients, blur, or colored section bands.
- Don't add drop shadows beyond the amount bubble and bottom sheet.
- Don't put more than one primary button on a screen.
- Don't show "0원" in empty calendar cells — leave them empty.
- Don't put unabbreviated amounts in calendar cells; use `125만` / `3.2만`.
- Don't use real bank logos or bank brand colors until usage terms are confirmed; use `bank-squircle`.
- Don't show the mascot on working screens — onboarding and empty states only.
- Don't apply letter-spacing, all-caps, or a second typeface.
- Don't square off pill geometry at small sizes; badges, chips, and toggles stay stadium-shaped.
- Don't put borders on form fields at rest; the ink ring appears only on focus.
