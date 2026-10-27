import pathlib, re, yaml
ROOT = pathlib.Path("/Users/pratyush.mishra/Documents/GitHub/LinkedInPost")
L = ROOT / "ledgers"
DATE = "2026-10-27"

def find(raw):
    hits = [p for p in L.rglob("*.md") if p.parent.name in ("items", "archive")
            and re.search(rf"^raw_id: {re.escape(raw)}$", p.read_text(), re.M)]
    assert len(hits) == 1, (raw, hits)
    return hits[0]

def load(p):
    raw = p.read_text(encoding="utf-8")
    front, body = raw[4:].split("\n---\n", 1)
    return yaml.safe_load(front), body

def save(p, meta, body, folder):
    head = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10000)
    dest = L / p.parent.parent.name / folder / p.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"---\n{head}---\n{body}", encoding="utf-8")
    if dest != p:
        p.unlink()

def set_section(body, name, text):
    head = f"## {name}\n"
    pre, rest = body.split(head, 1) if head in body else (body.rstrip() + "\n\n" + head, "")
    if head in body:
        after = rest.split("\n## ", 1)
        tail = ("\n## " + after[1]) if len(after) > 1 else ""
    else:
        tail = ""
    return pre + head + "\n" + text.strip() + "\n" + tail

def append_section(body, name, line):
    head = f"## {name}\n"
    i = body.index(head) + len(head)
    j = body.find("\n## ", i)
    j = len(body) if j < 0 else j
    return body[:j].rstrip() + "\n" + line + "\n" + body[j:]

def close(raw, resolution, verification, attempt):
    p = find(raw)
    meta, body = load(p)
    meta["status"] = "closed"
    meta["resolution"] = resolution
    meta["updated"] = DATE
    body = append_section(body, "Attempts", f"- {DATE} — {attempt}")
    body = set_section(body, "Verification", verification)
    save(p, meta, body, "archive")
    return p.name

def create(raw, title, slug, status, typ, body_sections, related=(), docs=()):
    rid = f"{DATE}-{slug}"
    assert not (L / "backlog" / "items" / f"{rid}.md").exists()
    meta = dict(id=rid, title=title, created=DATE, updated=DATE, journeys=[], related=list(related),
                docs=list(docs), status=status, owner=None, branch=None, worktree=None, claimed_at=None,
                blocked_reason=None, type=typ, raw_id=raw, source_file="docs/launch-readiness/findings/GAPS.md (wrap-up)")
    body = "".join(f"## {name}\n\n{text.strip()}\n\n" for name, text in body_sections)
    head = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10000)
    (L / "backlog" / "items" / f"{rid}.md").write_text(f"---\n{head}---\n\n{body}", encoding="utf-8")
    return rid

# 1. close what the hygiene commit resolved
ver_hyg = ("Checked on branch wrap-hygiene at commit 77ad744: `git ls-files state | wc -l` -> 0 (was 14); "
           "`git ls-files | grep -c '\\.DS_Store$'` -> 0 (was 10); `.gitignore` now ignores `.DS_Store`; "
           "`git check-ignore -q state/exec/events.jsonl` succeeds. Files remain on disk. Not run: any app test (no code changed).")
print(close("HYG-001", "fixed", ver_hyg, "Untracked the 10 committed .DS_Store files and ignored them (commit 77ad744)."))
print(close("HYG-002", "fixed",
            ver_hyg + " Secret-shape scan of the 14 files before untracking: no matches for key, token, or private-key patterns.",
            "Scanned state/exec for key/token/private-key patterns (none), then untracked state/exec (commit 77ad744). Files kept on disk."))

# 2. correct GAP-008: the setup repository exists
print(close("GAP-008", "fixed",
            "Correction: the repository exists at /Users/pratyush.mishra/setup (git, origin P1927/setup, with ledgers/ and tools/ledgers). "
            "Checked with `ls -la ~/setup` and `git -C ~/setup remote -v`. The scaffold was installed from it and the ledgers were rebuilt on it (commit 85b2fb7 on main).",
            "Found the setup repository at ~/setup (home folder, not ~/Documents/GitHub). The earlier 'no such repo' statement was wrong: the search had not covered the home folder. Corrected here."))

# 3. file this session's new findings
new = []
new.append(create("WRAP-001", "The ledger CI check from the setup scaffold is not installed, so ledger validity is only checked by hand", "wrap-001-ledger-ci-check-not-installed", "open", "process", [
    ("Problem", "The setup scaffold ships .github/workflows/ledgers.yml (install with --with-ci). This repository installed the scaffold without it, so nothing runs `manage.py check` on pull requests or pushes to main."),
    ("Evidence and reproduction", "`python3 /Users/pratyush.mishra/setup/tools/install.py <repo>` (preview) lists the workflow only with `--with-ci`. `ls .github/workflows` shows no ledgers.yml."),
    ("Acceptance criteria", "- The workflow runs `python3 tools/ledgers/manage.py check` on push and pull request, and it passes on main."),
    ("Plan", "Owner decision: install the workflow (`--with-ci --apply`) and check it passes on a branch before relying on it."),
    ("Attempts", f"- {DATE} — Filed during wrap-up. Not installed in this session; a workflow file is an owner-visible change."),
    ("Verification", "Pending. Not performed."),
]))
new.append(create("WRAP-002", "The ledger record generator exists only in scratch space, so the imported records cannot be regenerated from the repository", "wrap-002-ledger-generator-only-in-scratch", "open", "process", [
    ("Problem", "The 670 review records were generated by a script kept in the agent's scratch directory, not in the repository. The records are now the source of truth (hand edits are expected), but nobody can rerun the import to check it."),
    ("Evidence and reproduction", "Generator: scratchpad gen_ledgers.py and gen_video_backlog.py (not committed). Records: ledgers/*/items and archive, generated 2026-10-27."),
    ("Acceptance criteria", "- Either the import script is committed with a note that it is one-time, or it is deleted and the records are declared the only source (decision recorded)."),
    ("Plan", "Recommendation: keep the records as the source; do not commit the one-time importer. Record that decision in a decision record once the owner agrees."),
    ("Attempts", f"- {DATE} — Filed during wrap-up. No change made."),
    ("Verification", "Pending. Owner decision needed."),
]))
new.append(create("WRAP-003", "146 journeys have no verification owner, so no one is accountable for running them", "wrap-003-journeys-have-no-verification-owner", "open", "decision", [
    ("Problem", "Every journey record in ledgers/journeys carries verification_owner 'unassigned (owner to set)'. A journey can only become verified with a named owner, so none can be verified yet."),
    ("Evidence and reproduction", "`grep -l 'unassigned (owner to set)' ledgers/journeys/items/*.md | wc -l` -> 146."),
    ("Acceptance criteria", "- Each journey names a verification owner, or the owner records a rule (for example one owner per section)."),
    ("Plan", "Owner decision: pick owners per section (frontend, worker, generation-worker, setup, automations, application). Recommendation: one owner per section, recorded in the section review."),
    ("Attempts", f"- {DATE} — Filed during wrap-up. Options and recommendation recorded; no owner chosen."),
    ("Verification", "Pending. Owner decision needed."),
]))
new.append(create("WRAP-004", "The pre-setup status snapshot and its duplicate findings files can be retired once the ledger is accepted", "wrap-004-retire-pre-setup-status-snapshot", "open", "process", [
    ("Problem", "docs/launch-readiness/status.json and the findings files still hold the pre-setup status values. Those values are now duplicated by the ledger records, so two sources can drift."),
    ("Evidence and reproduction", "`ls docs/launch-readiness/status.json`; the ledger records carry the same IDs and statuses."),
    ("Acceptance criteria", "- The snapshot is either removed, or kept with a note that the ledger records supersede it, and nothing reads it."),
    ("Plan", "Recommendation: keep the findings files as evidence (they are cited) and delete status.json once the owner has accepted the ledger. Low priority."),
    ("Attempts", f"- {DATE} — Filed during wrap-up. No change made."),
    ("Verification", "Pending. Low priority; nothing depends on it."),
], related=[]))

# 4. correct stale launch-release paths inside record text
n = 0
for p in L.rglob("*.md"):
    t = p.read_text(encoding="utf-8")
    t2 = t.replace("launch-release/ledgers-legacy/", "docs/launch-readiness/legacy/").replace("launch-release/", "docs/launch-readiness/")
    if t2 != t:
        p.write_text(t2, encoding="utf-8"); n += 1
print("path corrections in", n, "records")
