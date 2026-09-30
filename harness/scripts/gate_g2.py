"""G2 화면 설계서 게이트: runs/<run>/02-spec/02-screen-spec.json 을 검사한다.
★ A(조회 전용), B(원본 수정 금지) 검사를 포함한다."""
import sys

from _common import all_strings, emit, forbidden_hits, load_json, load_rules, run_dir_arg, violation


def check(data, rules):
    v = []
    screens = data.get("screens") if isinstance(data, dict) else None
    if not isinstance(screens, list):
        return [violation("G2-COUNT", "screens 배열이 없습니다")]

    lo, hi = rules["screens_per_run"]
    if not lo <= len(screens) <= hi:
        v.append(violation("G2-COUNT", f"화면 {len(screens)}개 (허용 {lo}~{hi}개)"))

    allowed = set(rules["components"])
    input_components = set(rules["input_components"])
    prefix = rules["original_field_prefix"]

    for i, screen in enumerate(screens):
        where = f"screens[{i}]"
        if not isinstance(screen, dict):
            v.append(violation("G2-STORY", "화면 항목이 객체가 아닙니다", where))
            continue
        where = f"screens[{i}] {screen.get('id', '')}".strip()

        elements = screen.get("story_elements")
        if not isinstance(elements, list) or not [e for e in elements if isinstance(e, str) and e.strip()]:
            v.append(violation("G2-STORY", "story_elements가 1개 이상 필요합니다", where))

        for comp in screen.get("components") or []:
            if comp not in allowed:
                v.append(violation("G2-COMP", f"design.md에 없는 컴포넌트: {comp}", where))

        for j, inp in enumerate(screen.get("inputs") or []):
            comp = inp.get("component") if isinstance(inp, dict) else None
            if comp not in allowed:
                v.append(violation("G2-COMP", f"design.md에 없는 컴포넌트: {comp}", f"{where} inputs[{j}]"))
            if comp in input_components:
                bind = inp.get("binds_to")
                if not isinstance(bind, str) or not bind.strip():
                    v.append(violation("B-TXN-INPUT", "입력 요소에 binds_to가 없어 원본 수정 여부를 알 수 없습니다", f"{where} inputs[{j}]"))
                elif bind.startswith(prefix):
                    v.append(violation("B-TXN-INPUT", f"원본 거래 필드를 수정하는 입력: {bind}", f"{where} inputs[{j}]"))

    for text in all_strings(data):
        for word in forbidden_hits(text, rules["readonly_forbidden_words"]):
            v.append(violation("A-FORBIDDEN", f"조회 전용 위반 금지어 '{word}': {text}"))
    return v


def main():
    run = run_dir_arg()
    data, err = load_json(run / "02-spec" / "02-screen-spec.json")
    if err:
        return emit("G2", [violation("G2-FILE", err)])
    return emit("G2", check(data, load_rules()))


if __name__ == "__main__":
    sys.exit(main())
