"""G3 Figma 프레임 게이트: runs/<run>/03-figma/03-figma-frames.json 을 검사하고
결과를 runs/<run>/04-review/04-review.json, 04-review.md 로 쓴다.
★ A(조회 전용) 검사를 포함한다."""
import json
import re
import sys
from collections import Counter

from _common import HARNESS_DIR, emit, forbidden_hits, load_json, load_rules, run_dir_arg, violation

HUMAN_CHECKS = [
    "레퍼런스가 유저스토리와 실제로 관련 있는가",
    "화면 설계가 유저스토리를 제대로 풀었는가",
    "전체적인 인상 (깔끔하고 모던한가)",
]


def norm_hex(value):
    return value.upper() if isinstance(value, str) and re.fullmatch(r"#[0-9A-Fa-f]{6}", value) else None


def radii(value):
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def check_node(node, where, rules, v, counts):
    colors = set(rules["colors_allowed"])
    name = node.get("name", "")
    comp = node.get("component")

    for key in ("fills", "strokes"):
        for c in node.get(key) or []:
            if c == "image":
                continue
            hx = norm_hex(c)
            if hx is None or hx not in colors:
                v.append(violation("G3-COLOR", f"허용되지 않은 색 {c} ({key})", where))

    for r in radii(node.get("radius")):
        if r not in rules["radius_allowed"]:
            v.append(violation("G3-RADIUS", f"허용되지 않은 모서리 {r}", where))

    if node.get("shadow") and name not in rules["shadow_allowed_on"] and comp not in rules["shadow_allowed_on"]:
        v.append(violation("G3-SHADOW", "그림자는 amount-bubble, transaction-sheet에만 허용", where))

    if comp == rules["primary_button"]["component"]:
        counts["primary"] += 1

    text = node.get("text")
    if node.get("type") == "TEXT" or text is not None:
        if node.get("font_family") not in rules["font_family"]:
            v.append(violation("G3-FONT-FAMILY", f"폰트 {node.get('font_family')}", where))
        if node.get("font_size") not in rules["font_size_allowed"]:
            v.append(violation("G3-FONT-SIZE", f"글자 크기 {node.get('font_size')}", where))
        if node.get("font_weight") not in rules["font_weight_allowed"]:
            v.append(violation("G3-FONT-WEIGHT", f"글자 굵기 {node.get('font_weight')}", where))

        text = text or ""
        amount = rules["amount_text"]
        if re.fullmatch(amount["pattern"], text.strip()):
            expected = amount["color_by_sign"][text.strip()[0]]
            fill = norm_hex((node.get("fills") or [None])[0])
            if fill != expected:
                v.append(violation("G3-AMOUNT-COLOR", f"금액 '{text}'의 색 {fill} (필요: {expected})", where))

        for word in forbidden_hits(text, rules["readonly_forbidden_words"]):
            v.append(violation("A-FORBIDDEN", f"조회 전용 위반 금지어 '{word}': {text}", where))


def check(data, rules):
    v = []
    frames = data.get("frames") if isinstance(data, dict) else None
    if not isinstance(frames, list):
        return [violation("G3-FRAME-COUNT", "frames 배열이 없습니다")]

    lo, hi = rules["screens_per_run"]
    if not lo <= len(frames) <= hi:
        v.append(violation("G3-FRAME-COUNT", f"프레임 {len(frames)}개 (허용 {lo}~{hi}개)"))

    w, h = rules["frame"]["width"], rules["frame"]["height"]
    for i, frame in enumerate(frames):
        fname = f"frames[{i}] {frame.get('name', '')}".strip()
        if frame.get("width") != w or frame.get("height") != h:
            v.append(violation("G3-FRAME-SIZE", f"{frame.get('width')}×{frame.get('height')} (필요 {w}×{h})", fname))

        counts = Counter()
        check_node(frame, fname, rules, v, counts)
        for node in frame.get("nodes") or []:
            where = f"{fname} > {node.get('name', node.get('id', ''))}"
            check_node(node, where, rules, v, counts)

        if counts["primary"] > rules["primary_button"]["max_per_frame"]:
            v.append(violation("G3-PRIMARY-BTN", f"button-primary {counts['primary']}개 (최대 {rules['primary_button']['max_per_frame']}개)", fname))
    return v


def figma_link(data):
    config, _ = load_json(HARNESS_DIR / "config.json")
    url = (config or {}).get("figma_file_url") or ""
    if not url and isinstance(data, dict) and data.get("file_key"):
        url = f"https://www.figma.com/design/{data['file_key']}"
    return url or "(Figma 주소 없음)"


def write_review(run, data, violations):
    out = run / "04-review"
    out.mkdir(parents=True, exist_ok=True)
    result = {"gate": "G3", "passed": not violations, "violations": violations}
    (out / "04-review.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    by_rule = Counter(x["rule"] for x in violations)
    lines = [
        f"# 가이드 검토 결과: {run.name}",
        "",
        f"- 판정: **{'통과' if not violations else '실패'}** (위반 {len(violations)}건)",
        f"- Figma: {figma_link(data)}",
        f"- 페이지: {(data or {}).get('page', '') if isinstance(data, dict) else ''}",
        "",
    ]
    if violations:
        lines += ["## 규칙별 위반 수", "", "| 규칙 | 건수 |", "|---|---|"]
        lines += [f"| {r} | {n} |" for r, n in sorted(by_rule.items())]
        lines += ["", "## 위반 목록", ""]
        lines += [f"- `{x['rule']}` {x['where']}: {x['message']}" for x in violations]
        lines += [""]
    lines += ["## 사람이 확인할 것 (스크립트로 못 잡음)", ""]
    lines += [f"- [ ] {c}" for c in HUMAN_CHECKS]
    lines += ["", "승인하려면 \"승인\", 되돌리려면 \"반려 S2\" 또는 \"반려 S3\"라고 말하세요.", ""]
    (out / "04-review.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    run = run_dir_arg()
    data, err = load_json(run / "03-figma" / "03-figma-frames.json")
    violations = [violation("G3-FILE", err)] if err else check(data, load_rules())
    write_review(run, data, violations)
    return emit("G3", violations)


if __name__ == "__main__":
    sys.exit(main())
