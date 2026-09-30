# 하네스 역할 (R6)

> 파이프라인: `harness-pipeline.md` / 산출물: `harness-artifacts.md` / 게이트: `harness-gates.md`

## 에이전트

| 에이전트 | 단계 | 편집 가능 폴더 (이 하나만) | 쓰는 도구 |
|---|---|---|---|
| `ref-collector` | S1 | `runs/<run>/01-ref/` | uibowl |
| `screen-planner` | S2 | `runs/<run>/02-spec/` | 없음 (문서 읽기) |
| `figma-drawer` | S3 | `runs/<run>/03-figma/` | Figma |
| `judge` | S4 | 없음 (읽기 전용) | 판정 스크립트 실행 |

- `state.json`은 오케스트레이터(CLAUDE.md)만 고친다.

## 판정자 (judge)
- 도구: Read, Bash만. Edit/Write 없음.
- Bash는 `python3 harness/scripts/` 아래 스크립트 실행만.
- `04-review/`의 결과 파일은 스크립트가 쓴다. judge는 결과를 고칠 수 없다.

## 읽기 전용 폴더
- `docs/`, `harness/`는 모든 에이전트에게 읽기 전용. 고치는 건 사람만.
- `.claude/settings.json` deny 규칙으로 막는다.

## 자연어 트리거

| 이렇게 말하면 | 동작 |
|---|---|
| "유저스토리 3번 화면 만들어줘" | 새 실행 `runs/us3-날짜/`, S1부터 시작 |
| "이어서 해줘" | 가장 최근 실행의 `state.json`을 보고 다음 단계부터 |
| "검토만 다시 해줘" | G3와 S4만 다시 |
| "승인" / "반려 S2" / "반려 S3" | 사람 승인 처리 |
