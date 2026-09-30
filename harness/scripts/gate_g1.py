"""G1 레퍼런스 게이트: runs/<run>/01-ref/01-references.json 을 검사한다."""
import sys

from _common import emit, load_json, load_rules, run_dir_arg, violation


def check(data, rules):
    v = []
    refs = data.get("references") if isinstance(data, dict) else None
    if not isinstance(refs, list):
        return [violation("G1-COUNT", "references 배열이 없습니다")]

    lo, hi = rules["references_per_run"]
    if not lo <= len(refs) <= hi:
        v.append(violation("G1-COUNT", f"레퍼런스 {len(refs)}개 (허용 {lo}~{hi}개)"))

    for i, ref in enumerate(refs):
        for field in rules["reference_required_fields"]:
            value = ref.get(field) if isinstance(ref, dict) else None
            if not isinstance(value, str) or not value.strip():
                v.append(violation("G1-FIELDS", f"'{field}'가 비어 있습니다", f"references[{i}]"))
    return v


def main():
    run = run_dir_arg()
    data, err = load_json(run / "01-ref" / "01-references.json")
    if err:
        return emit("G1", [violation("G1-FILE", err)])
    return emit("G1", check(data, load_rules()))


if __name__ == "__main__":
    sys.exit(main())
