# 하네스 게이트 (R5)

> 규칙 값의 SSOT: `harness/rules.json` / 판정 기준: `design.md`, `story-service.md`
> 모든 판정 스크립트: Python 3 표준 라이브러리, 통과 exit 0 / 실패 exit 1, 위반 목록은 JSON으로 남김.
> 스크립트는 Figma에 직접 접속하지 않고 repo 안의 JSON 파일만 읽는다.

## 게이트 요약

| 게이트 | 위치 | 검사 대상 | 실패 시 |
|---|---|---|---|
| G1 | S1 뒤 | `01-references.json` | S1 |
| G2 | S2 뒤 (그리기 전) | `02-screen-spec.json` | S2 |
| G3 | S4 | `03-figma-frames.json` | S3 |
| 사람 승인 | G3 통과 뒤 | `04-review.md` + Figma 링크 | 사용자가 S2 또는 S3 선택 |

같은 단계에서 2회 실패하면 중단하고 사람에게 넘긴다.

## G1 레퍼런스 (story-work 1번 멈칫)
- 레퍼런스 개수 3~5
- 각 레퍼런스에 `ui_url`, `story_element`(유저스토리 요소), `takeaway`(반영할 점 1줄)가 비어 있지 않음

## G2 화면 설계서 (story-work 4번 멈칫)
- 화면 개수 2~3
- 화면마다 `story_elements` 1개 이상
- 사용 컴포넌트는 design.md Components 섹션에 있는 이름만
- ★ A, B 검사 (아래)

## G3 Figma 프레임
- 프레임 390×844, 개수 2~3
- 색: 15개 값만 허용
  #141414 #FDFDFD #0055FF #EAF0FF #FFFFFF #F3F3F3 #F0F0F0 #E0E0E0
  #EEEEEE #CFCFCF #707070 #ADADAD #C77A1E #FFF3E3 #D64545
- 모서리: 0 / 10 / 16 / 24 / 9999
- 폰트: Pretendard만 / 크기 11·12·13·15·16·17·18·22·28·32 / 굵기 300·400·500·600·700
- 그림자: 이름이 `amount-bubble`, `transaction-sheet`인 요소에만
- `button-primary`: 프레임당 최대 1개
- 금액 글자: `-`로 시작하면 #141414, `+`로 시작하면 #0055FF
- ★ A 검사 (아래)

## ★ 어기면 안 되는 것 (story-service.md A·B)

| 규칙 | 검사 | 게이트 |
|---|---|---|
| A 조회 전용 | 모든 글자에 `송금` `이체하기` `결제하기` `보내기` `충전하기` `출금하기` 중 하나라도 있으면 위반 ("이체" 단독은 허용) | G2, G3 |
| B 원본 수정 금지 | 입력 요소(`text-input`, `memo-box`)가 `transaction.`으로 시작하는 필드에 연결되면 위반 | G2 |

## 사람 승인 (1곳)
- G3 통과 뒤 `04-review.md`와 Figma 링크를 보고 승인 → 완료
- 반려 시 되돌아갈 곳을 사용자가 S2(설계부터) / S3(그림만) 중 선택
