import pathlib, re, yaml
ROOT = pathlib.Path("/Users/pratyush.mishra/Documents/GitHub/LinkedInPost")
L = ROOT / "ledgers"
DATE = "2026-10-27"
SRC = "docs/plans/video-pipeline/BACKLOG.md"
used = {p.stem for p in L.rglob("*.md")}
section = ""
n = 0
for line in (ROOT / SRC).read_text().splitlines():
    if line.startswith("## "):
        section = line[3:].strip()
        continue
    m = re.match(r"^- (B-[A-Z0-9]+-\d+) (.*)$", line)
    if not m:
        continue
    bid, text = m.group(1), m.group(2).strip()
    trig = ""
    tm = re.search(r"\s*Trig:\s*(.*)$", text)
    if tm:
        trig = tm.group(1).strip()
        text = text[:tm.start()].strip()
    value = effort = ""
    vm = re.search(r"\s*V ([HML]), E ([SML])(?: each)?\.?\s*$", text)
    if vm:
        value, effort = vm.group(1), vm.group(2)
        text = text[:vm.start()].strip()
    text = text.rstrip(".")
    rejected = "REJECTED" in text
    title = f"{bid} {text}".strip()
    slug = re.sub(r"[^a-z0-9]+", "-", f"{bid} {text}".lower()).strip("-")[:70].rstrip("-")
    rid = f"{DATE}-{slug}"
    k = 2
    base = rid
    while rid in used:
        rid = f"{base}-{k}"; k += 1
    used.add(rid)
    status = "closed" if rejected else "open"
    meta = dict(id=rid, title=title, created=DATE, updated=DATE, journeys=[], related=[], docs=[SRC],
                status=status, owner=None, branch=None, worktree=None, claimed_at=None, blocked_reason=None,
                type="improvement", area=f"video-pipeline/{section}", raw_id=bid, value=value or "unset", effort=effort or "unset")
    if rejected:
        meta["resolution"] = "declined"
    folder = "archive" if rejected else "items"
    verif = (f"Declined: {text} The item stays in the source backlog for history." if rejected else
             "Pending. Filed from the video-pipeline backlog as an improvement; nothing was built or checked here.")
    body = (
        f"## Problem\n\n{text}. Section: {section}. Value {value or 'unset'}, effort {effort or 'unset'}."
        + (f" Trigger: {trig}." if trig else "") + "\n\n"
        "## Evidence and reproduction\n\n"
        f"- Source: {SRC} ({bid}).\n- Not a defect report; an improvement the owner already listed.\n\n"
        "## Acceptance criteria\n\n- The change named in the title is built, and its effect is measured against the trigger (if any).\n\n"
        "## Plan\n\nDecide scope when the trigger fires; record the decision in Attempts.\n\n"
        f"## Attempts\n\n- {DATE} — Imported from {SRC} into the ledger. No work started.\n\n"
        f"## Verification\n\n{verif}\n")
    head = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10000)
    d = L / "backlog" / folder
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{rid}.md").write_text(f"---\n{head}---\n\n{body}", encoding="utf-8")
    n += 1
print("video backlog records:", n)
