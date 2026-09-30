# 하네스 산출물 (R4)

> 파이프라인: `harness-pipeline.md`

## 실행 폴더

실행 1번 = 폴더 1개: `runs/us{스토리번호}-{YYYYMMDD}/` (예: `runs/us3-20260930/`)

| 파일 | 단계 | 내용 |
|---|---|---|
| `01-ref/01-references.json` | S1 | 선별한 레퍼런스 3~5개 (유저스토리 요소, 반영할 점) |
| `02-spec/02-screen-spec.json` | S2 | 화면 설계서 (키스크린 2~3개, 화면별 유저스토리 요소, 사용 컴포넌트) |
| `03-figma/03-figma-frames.json` | S3 | Figma 파일 키, 프레임 id, 크기, 요소 정보 |
| `04-review/04-review.json` | S4 | 위반 목록 (판정 스크립트 출력) |
| `04-review/04-review.md` | S4 | 사람이 읽을 요약 (스크립트 출력) |
| `state.json` | 전체 | 마지막 통과 단계, 단계별 재시도 횟수 (오케스트레이터만 수정) |

- 형식: `04-review.md`를 뺀 나머지는 모두 JSON.

## 규칙 SSOT

- 파일: `harness/rules.json` 하나. 모든 판정 스크립트는 이 파일만 읽는다.
- `design.md`에서 셀 수 있는 규칙만 뽑아 담는다. 구체적인 값은 R5에서 정한다.
- `design.md`를 고치면 `rules.json`도 같이 고친다. 둘이 다르면 `rules.json`이 판정 기준이다.

## 재개

- `state.json`에 마지막으로 통과한 단계를 기록한다.
- 다시 실행하면 그다음 단계부터 시작한다.
- 되돌아가서 다시 할 때는 그 단계 이후의 파일만 새로 만든다.
