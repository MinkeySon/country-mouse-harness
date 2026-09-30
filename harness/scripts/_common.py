"""게이트 스크립트 공통 함수. 규칙 값은 harness/rules.json 에서만 읽는다."""
import json
import sys
from pathlib import Path

HARNESS_DIR = Path(__file__).resolve().parent.parent
RULES_PATH = HARNESS_DIR / "rules.json"


def load_rules():
    return json.loads(RULES_PATH.read_text(encoding="utf-8"))


def load_json(path):
    path = Path(path)
    if not path.exists():
        return None, f"파일이 없습니다: {path}"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as e:
        return None, f"JSON 형식 오류: {path}: {e}"


def violation(rule_id, message, where=""):
    return {"rule": rule_id, "where": where, "message": message}


def all_strings(value):
    """JSON 값 안의 모든 문자열을 꺼낸다."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from all_strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from all_strings(v)


def forbidden_hits(text, words):
    return [w for w in words if w in text]


def emit(gate, violations, extra=None):
    """결과를 stdout 에 JSON 으로 출력하고 exit code 를 돌려준다."""
    result = {"gate": gate, "passed": not violations, "violations": violations}
    if extra:
        result.update(extra)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not violations else 1


def run_dir_arg():
    if len(sys.argv) != 2:
        print(f"사용법: python3 {sys.argv[0]} runs/<run>", file=sys.stderr)
        sys.exit(2)
    return Path(sys.argv[1])
