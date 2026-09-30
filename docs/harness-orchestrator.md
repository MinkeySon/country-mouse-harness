# 하네스 오케스트레이터 (R7)

> 오케스트레이터 = `CLAUDE.md`를 읽고 동작하는 메인 Claude Code 세션.
> 역할: `harness-roles.md` / 게이트: `harness-gates.md` / 산출물: `harness-artifacts.md`

## 실행 흐름

1. 트리거를 받는다 (`harness-roles.md` 자연어 트리거 표)
2. 실행 폴더 `runs/us{N}-{YYYYMMDD}/`와 `state.json`을 만든다 (재개면 `state.json`을 읽는다)
3. S1 `ref-collector` 호출 → 오케스트레이터가 G1 실행
4. S2 `screen-planner` 호출 → 오케스트레이터가 G2 실행
5. S3 `figma-drawer` 호출
6. S4 `judge` 호출 → judge가 G3 실행, `04-review.md` 생성
7. 사용자에게 `04-review.md`와 Figma 링크를 보여주고 승인을 기다린다
8. "승인" → 완료 / "반려 S2" 또는 "반려 S3" → 해당 단계로

각 게이트 통과 시 `state.json`에 통과 단계를 기록한다.
실패 시 위반 목록을 그대로 되돌아갈 에이전트에게 넘기고 재시도 횟수를 +1 한다.
같은 단계 2회 실패 시 중단하고 사용자에게 넘긴다.

## 게이트 실행 주체

| 게이트 | 실행 주체 |
|---|---|
| G1, G2 | 오케스트레이터 (스크립트 직접 실행) |
| G3 | `judge` (S4) |

## 오케스트레이터가 하지 않는 일
- `state.json` 외의 파일을 고치지 않는다. `01-ref/`, `02-spec/`, `03-figma/`는 해당 에이전트만 만든다.
- 게이트 위반을 직접 고치지 않는다.
- 사람 승인 전에는 "완료"라고 말하지 않는다.

## Figma 파일
- 파일 1개 고정, 실행마다 페이지 1개 (예: `us3-20260930`)
- 파일 주소는 `harness/config.json`에 사람이 적는다.
- 파일이 없으면 첫 실행 때 `figma-drawer`가 만들고, 사용자가 주소를 `config.json`에 적는다.

## CLAUDE.md 작성 원칙
- 한국어, 100줄 이내
- 규칙을 복사하지 않고 `docs/harness-*.md`, `harness/rules.json`을 가리킨다.
