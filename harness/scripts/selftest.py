"""하네스 자체 점검.
1) 게이트 샘플: 통과 샘플은 exit 0, 위반 샘플은 exit 1 + 예상한 규칙 id 만 나와야 한다.
2) 동기화: rules.json 의 색·컴포넌트가 design.md 와 일치해야 한다.
사용법: python3 harness/scripts/selftest.py"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from _common import HARNESS_DIR, load_rules

SCRIPTS = HARNESS_DIR / "scripts"
FIXTURES = HARNESS_DIR / "tests" / "fixtures"
DESIGN_MD = HARNESS_DIR.parent / "docs" / "design.md"

GATES = {
    "g1": ("gate_g1.py", "01-ref/01-references.json"),
    "g2": ("gate_g2.py", "02-spec/02-screen-spec.json"),
    "g3": ("gate_g3.py", "03-figma/03-figma-frames.json"),
}

# (샘플 파일, 예상 규칙 id 집합). 빈 집합 = 통과해야 함.
CASES = [
    ("g1_pass.json", set()),
    ("g1_fail_count.json", {"G1-COUNT"}),
    ("g1_fail_fields.json", {"G1-FIELDS"}),
    ("g2_pass.json", set()),
    ("g2_fail_count.json", {"G2-COUNT"}),
    ("g2_fail_story.json", {"G2-STORY"}),
    ("g2_fail_comp.json", {"G2-COMP"}),
    ("g2_fail_a.json", {"A-FORBIDDEN"}),
    ("g2_fail_b.json", {"B-TXN-INPUT"}),
    ("g3_pass.json", set()),
    ("g3_fail_frame_size.json", {"G3-FRAME-SIZE"}),
    ("g3_fail_frame_count.json", {"G3-FRAME-COUNT"}),
    ("g3_fail_color.json", {"G3-COLOR"}),
    ("g3_fail_radius.json", {"G3-RADIUS"}),
    ("g3_fail_font_family.json", {"G3-FONT-FAMILY"}),
    ("g3_fail_font_size.json", {"G3-FONT-SIZE"}),
    ("g3_fail_font_weight.json", {"G3-FONT-WEIGHT"}),
    ("g3_fail_shadow.json", {"G3-SHADOW"}),
    ("g3_fail_primary_btn.json", {"G3-PRIMARY-BTN"}),
    ("g3_fail_amount_color.json", {"G3-AMOUNT-COLOR"}),
    ("g3_fail_a.json", {"A-FORBIDDEN"}),
]


def run_case(fixture, expected):
    script, rel = GATES[fixture[:2]]
    with tempfile.TemporaryDirectory() as tmp:
        run = Path(tmp) / "us0-selftest"
        target = run / rel
        target.parent.mkdir(parents=True)
        shutil.copy(FIXTURES / fixture, target)
        proc = subprocess.run([sys.executable, str(SCRIPTS / script), str(run)], capture_output=True, text=True)
    try:
        got = {x["rule"] for x in json.loads(proc.stdout)["violations"]}
    except (json.JSONDecodeError, KeyError):
        return False, f"출력 해석 실패: {proc.stdout[:200]} {proc.stderr[:200]}"
    want_code = 0 if not expected else 1
    ok = proc.returncode == want_code and got == expected
    return ok, f"exit {proc.returncode} (필요 {want_code}), 규칙 {sorted(got)} (필요 {sorted(expected)})"


def sync_checks(rules):
    text = DESIGN_MD.read_text(encoding="utf-8")
    results = []

    design_colors = {c.upper() for c in re.findall(r"#[0-9A-Fa-f]{6}\b", text)}
    rule_colors = {c.upper() for c in rules["colors_allowed"]}
    ok = design_colors == rule_colors
    detail = "" if ok else f"design.md에만: {sorted(design_colors - rule_colors)}, rules.json에만: {sorted(rule_colors - design_colors)}"
    results.append(("SYNC-COLOR", ok, detail))

    m = re.search(r"^## Components\n(.*?)^## ", text, re.S | re.M)
    design_comps = set(re.findall(r"\*\*`([a-z0-9-]+)`\*\*", m.group(1))) if m else set()
    rule_comps = set(rules["components"])
    ok = bool(design_comps) and design_comps == rule_comps
    detail = "" if ok else f"design.md에만: {sorted(design_comps - rule_comps)}, rules.json에만: {sorted(rule_comps - design_comps)}"
    results.append(("SYNC-COMP", ok, detail))
    return results


def main():
    failed = 0
    print("== 게이트 샘플 ==")
    for fixture, expected in CASES:
        ok, detail = run_case(fixture, expected)
        failed += not ok
        print(f"[{'PASS' if ok else 'FAIL'}] {fixture}: {detail}")

    print("\n== 동기화 ==")
    for rule_id, ok, detail in sync_checks(load_rules()):
        failed += not ok
        print(f"[{'PASS' if ok else 'FAIL'}] {rule_id} {detail}".rstrip())

    print(f"\n결과: {'통과' if not failed else f'실패 {failed}건'}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
