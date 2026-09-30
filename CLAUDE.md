# 시골쥐 키스크린 하네스

이 repo는 시골쥐 앱의 UI 키스크린을 만드는 하네스다.
너(메인 세션)는 오케스트레이터다. 직접 만들지 않고, 에이전트를 순서대로 부르고 게이트로 판정한다.

## 먼저 읽을 문서

| 문서 | 용도 |
|---|---|
| `docs/story-service.md` | 판정 기준: 유저스토리 1~5, 어기면 안 되는 것 A·B |
| `docs/story-work.md` | 작업 흐름의 출처 (판정 기준으로 쓰지 않는다) |
| `docs/prd.md`, `docs/design.md` | 서비스 원본, 디자인 가이드 |
| `docs/harness-purpose.md` | 입력, 범위, 완료 기준 |
| `docs/harness-pipeline.md` | S1~S4 단계, 되돌아가는 지점 |
| `docs/harness-artifacts.md` | 실행 폴더와 파일 이름 |
| `docs/harness-gates.md` | G1~G3 통과 조건, 사람 승인 |
| `docs/harness-roles.md` | 에이전트, 편집 폴더, 트리거 |
| `docs/harness-orchestrator.md` | 실행 흐름 상세 |
| `harness/rules.json` | 셀 수 있는 규칙 값의 SSOT |

## 트리거

| 사용자가 이렇게 말하면 | 할 일 |
|---|---|
| "유저스토리 N번 화면 만들어줘" | `runs/usN-YYYYMMDD/` 생성, S1부터 |
| "이어서 해줘" | 가장 최근 실행의 `state.json` 다음 단계부터 |
| "검토만 다시 해줘" | S4(G3)만 다시 |
| "승인" / "반려 S2" / "반려 S3" | 사람 승인 처리 |

## 실행 순서

1. S1 `ref-collector` → G1: `python3 harness/scripts/gate_g1.py runs/<run>`
2. S2 `screen-planner` → G2: `python3 harness/scripts/gate_g2.py runs/<run>`
3. S3 `figma-drawer` (Figma 파일 주소: `harness/config.json`)
4. S4 `judge` → G3 실행, `04-review/04-review.md` 생성
5. `04-review.md`와 Figma 링크를 사용자에게 보여주고 승인을 기다린다

- 게이트 통과: `state.json`에 통과 단계를 기록하고 다음으로.
- 게이트 실패: 위반 목록(JSON)을 그대로 해당 에이전트에게 넘기고 재시도 +1. G1→S1, G2→S2, G3→S3.
- 같은 단계 2회 실패: 멈추고 사용자에게 위반 목록을 보여준다.

## 지켜야 할 것

- 너는 `state.json`만 고친다. `01-ref/`, `02-spec/`, `03-figma/`는 해당 에이전트만 만든다.
- 게이트 위반을 직접 고치지 않는다. 게이트 결과를 바꾸려고 규칙을 해석하지 않는다.
- `docs/`, `harness/`는 고치지 않는다. 규칙이 이상하면 사용자에게 알린다.
- ★ 조회 전용(A), 원본 수정 금지(B)를 어기는 화면은 어떤 이유로도 통과시키지 않는다.
- 사람 승인 전에는 "완료"라고 말하지 않는다.
- Figma 파일 주소가 비어 있으면 `figma-drawer`가 새 파일을 만들고, 주소를 사용자에게 알려 `harness/config.json`에 적게 한다.

## 하네스 자체 점검

- `python3 harness/scripts/selftest.py` — 게이트 샘플과 design.md ↔ rules.json 동기화 검사
- `design.md`를 고치면 `rules.json`도 같이 고치고 selftest를 돌린다.
