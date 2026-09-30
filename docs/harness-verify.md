# 하네스 검증과 리뷰 (R8)

> 게이트: `harness-gates.md` / 규칙 값 SSOT: `harness/rules.json`

## 1. selftest

- 실행: `python3 harness/scripts/selftest.py`
- 샘플 위치: `harness/tests/fixtures/`
- 게이트마다 통과 샘플 1개 + 규칙별 위반 샘플
- 통과 조건: 통과 샘플은 exit 0, 위반 샘플은 exit 1 + 예상한 규칙 id. 하나라도 어긋나면 selftest 실패.
- ★ 위반 샘플에 반드시 포함: A(`송금` 버튼), B(`transaction.amount`에 연결된 입력)

## 2. 동기화 검사 (selftest에 포함)

| id | 검사 |
|---|---|
| SYNC-COLOR | rules.json 색 15개 ⊆ design.md, design.md 색 ⊆ rules.json |
| SYNC-COMP | rules.json 컴포넌트 이름 = design.md Components 섹션 이름 |

## 3. 추적표 (규칙 → 잡는 곳)

| 규칙 (출처) | 규칙 id | 잡는 곳 |
|---|---|---|
| 레퍼런스 3~5개 (gates G1) | G1-COUNT | gate_g1.py |
| 레퍼런스 필드 비어 있지 않음 (gates G1) | G1-FIELDS | gate_g1.py |
| 화면 2~3개 (gates G2) | G2-COUNT | gate_g2.py |
| 화면마다 유저스토리 요소 1개 이상 (gates G2) | G2-STORY | gate_g2.py |
| design.md 컴포넌트 이름만 (gates G2) | G2-COMP | gate_g2.py |
| ★ A 조회 전용 금지어 (story-service A) | A-FORBIDDEN | gate_g2.py, gate_g3.py |
| ★ B 원본 필드 입력 금지 (story-service B) | B-TXN-INPUT | gate_g2.py |
| 프레임 390×844 (gates G3) | G3-FRAME-SIZE | gate_g3.py |
| 프레임 2~3개 (gates G3) | G3-FRAME-COUNT | gate_g3.py |
| 허용 색 15개 (gates G3) | G3-COLOR | gate_g3.py |
| 모서리 0/10/16/24/9999 (gates G3) | G3-RADIUS | gate_g3.py |
| Pretendard만 (gates G3) | G3-FONT-FAMILY | gate_g3.py |
| 글자 크기 허용 목록 (gates G3) | G3-FONT-SIZE | gate_g3.py |
| 글자 굵기 허용 목록 (gates G3) | G3-FONT-WEIGHT | gate_g3.py |
| 그림자 허용 요소만 (gates G3) | G3-SHADOW | gate_g3.py |
| button-primary 프레임당 1개 (gates G3) | G3-PRIMARY-BTN | gate_g3.py |
| 금액 색 (+ 파랑 / - 검정) (gates G3) | G3-AMOUNT-COLOR | gate_g3.py |
| 같은 단계 2회 실패 시 중단 (pipeline) | — | 오케스트레이터 (`state.json`) |
| docs/, harness/ 편집 금지 (roles) | — | `.claude/settings.json` deny |
| judge 읽기 전용 (roles) | — | `.claude/agents/judge.md` 도구 제한 |

## 4. 스크립트로 못 잡는 것 → 사람 승인에서 확인

- 레퍼런스가 유저스토리와 실제로 관련 있는가
- 화면 설계가 유저스토리를 제대로 풀었는가
- 전체적인 인상 (깔끔하고 모던한가)

## 5. 검증 범위

- 하네스를 만든 뒤 selftest까지만 실행해 결과를 보고한다.
- uibowl·Figma를 쓰는 실제 실행은 사용자가 트리거로 시작한다.
