#!/usr/bin/env python3
"""Generate setup-scaffold ledger records from the launch-readiness review evidence.

Reads docs/launch-readiness/** (findings, journeys, status.json) and writes records
into ledgers/<kind>/items or archive. Reads only; no product code is touched.
"""
import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path("/Users/pratyush.mishra/Documents/GitHub/LinkedInPost")
LR = ROOT / "docs/launch-readiness"
L = ROOT / "ledgers"
DATE = "2026-10-27"
NOW = "2026-10-27T15:44:37+01:00"
REV = "a65b712"  # main when the review read the code
OWNER_NOTE = "repository owner"
REVIEWER = "Claude Haiku 5.5 (read-only review agents, coordinated by the lead)"
RAW_LEGACY = {
    "MCP-PROGRESS.md": "MCP-PROGRESS.md",
    "MCP-TEST-IDEAS.md": "MCP-TEST-IDEAS.md",
    "FEED_EXPLORATION_REPORT.md": "FEED_EXPLORATION_REPORT.md",
    "ideas.md": "ideas.md",
}

status = json.loads((LR / "status.json").read_text())
used_ids = set()
records = {}  # raw/J id -> dict(kind, id, folder, path)
pending = []  # (kind, meta, body, folder, filename)

ID_RE = r"(?:LR|NI|HYG|JRN|TST|AUT|SWP|INV|GAP|ARCH|CONS|UC|FR|SP|AC|NW|IDEA|FRZ|REJ|FZ)-\d+"


def slug(text, n=6):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return "-".join(words[:n]) or "item"


def unique_id(prefix, title, n=6):
    base = f"{DATE}-{prefix}-{slug(title, n)}"
    cand, k = base, 2
    while cand in used_ids:
        cand = f"{base}-{k}"
        k += 1
    used_ids.add(cand)
    return cand


def parse_blocks(text, head_re):
    """Split markdown into blocks at headings matching head_re; return dicts with fields."""
    out = []
    for part in re.split(r"(?m)^(?=### )", text):
        m = re.match(head_re, part)
        if not m:
            continue
        body = part[m.end():]
        fields, order, cur = {}, [], None
        for line in body.splitlines():
            fm = re.match(r"^- \*\*([^*]+):\*\*\s*(.*)$", line)
            if fm:
                cur = fm.group(1).strip()
                order.append(cur)
                fields[cur] = fm.group(2).strip()
            elif cur and line.startswith("  "):
                fields[cur] += "\n" + line.strip()
            elif line.strip() == "" and cur is None:
                continue
        out.append(dict(m.groupdict(), fields=fields, order=order, body=body.strip()))
    return out


def items_from(path, head_re=r"### (?P<id>[A-Z]{1,4}-\d+) (?P<sev>P[0-3]) (?P<area>.+?) - (?P<title>.*)\n"):
    return parse_blocks(path.read_text(), head_re)


def expand_journeys(text):
    found = set()
    for a, b in re.findall(r"J-(\d{3})\.\.J-(\d{3})", text or ""):
        found.update(range(int(a), int(b) + 1))
    for n in re.findall(r"J-(\d{3})", text or ""):
        found.add(int(n))
    return sorted(n for n in found if 1 <= n <= 146)


def doc_paths(text):
    paths = []
    for p in re.findall(r"([A-Za-z0-9_.\-/]+\.(?:ts|tsx|js|jsx|mjs|cjs|py|md|yml|yaml|json|jsonc|sh|sql|toml|html|txt|example|development))", text or ""):
        p = p.lstrip("./")
        if (ROOT / p).is_file() and p not in paths:
            paths.append(p)
    return paths


def fmt_body(sections):
    out = []
    for name, text in sections:
        out.append(f"## {name}\n\n{text.strip() or 'None recorded.'}\n")
    return "\n".join(out)


def write(kind, folder, rid, meta, body):
    pending.append((kind, folder, rid, meta, body))


# ---------------------------------------------------------------- journeys
journey_items = items_from(LR / "journeys/JOURNEYS.md", r"### (?P<id>J-\d{3}) (?P<title>.*)\n")
jrec = {}
for it in journey_items:
    n = int(it["id"][2:])
    f = it["fields"]
    prio = f.get("Priority", "P2")
    title = it["title"].strip()
    rid = unique_id(f"j{n:03d}", title, 6)
    jrec[it["id"]] = rid
    anchors = f.get("Code anchors", "")
    code_paths = doc_paths(anchors)
    scope_word = next((w for w in ("frontend", "worker", "generation-worker", "setup", "packages", "automations", ".github") if anchors.startswith(w) or f"{w}/" in anchors), None)
    if scope_word:
        scope_type, scope = "section", scope_word
    else:
        scope_type, scope = "overall", "application"
    meta = dict(
        id=rid, title=f"{it['id']} {title}", status="planned", created=DATE, updated=DATE,
        journey_type="user" if "Self" not in f.get("Persona", "") else "workflow",
        scope_type=scope_type, scope=scope, actor=f.get("Persona", "unspecified"),
        trigger=(f.get("Preconditions", "") or "see steps")[:200],
        verification_owner="unassigned (owner to set)", source_revision=None, checked_at=None,
        modules=code_paths, code_paths=code_paths, related=[], journeys=None,
        docs=["docs/launch-readiness/journeys/JOURNEYS.md"],
        priority=prio, core=f.get("CORE", ""), external_service=f.get("External service", ""),
        legacy_id=it["id"],
    )
    meta.pop("journeys")
    steps = f.get("Steps", "")
    not_impl = "NOT IMPLEMENTED" in it["body"]
    body = fmt_body([
        ("Purpose and scope", f"{title}. Priority {prio}, CORE {f.get('CORE', '?')}. Imported from journey {it['id']} in docs/launch-readiness/journeys/JOURNEYS.md. "
         + ("The journey designer marked part of this journey NOT IMPLEMENTED per code reading." if not_impl else "")),
        ("Actor, trigger and prerequisites", f"Persona: {f.get('Persona', '?').rstrip('.')}. Preconditions: {f.get('Preconditions', 'none recorded').rstrip('.')}."),
        ("Steps and information flow", steps or "None recorded."),
        ("Modules and code map", (anchors or "None recorded.") + ("\n\nCode anchors that exist: " + ", ".join(code_paths) if code_paths else "")),
        ("Success and acceptance", f.get("Pass check", "None recorded.")),
        ("Failure, edge cases and recovery", "Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record)."),
        ("Verification evidence", "Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision."),
        ("Gaps and linked work", "Linked work is derived from the backlog records whose journeys field names this record. " + ("Not implemented per the journey designer: see the NOT IMPLEMENTED text in the steps." if not_impl else "")),
        ("Next actions", "Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified."),
    ])
    write("journeys", "items", rid, meta, body)

# ---------------------------------------------------------------- backlog (findings)
ARCH_MAP = {}
review_lr = items_from(LR / "findings/REVIEW-ITEMS.md")
alias_of = {}  # raw alias -> LR id
for it in review_lr:
    for a in re.findall(r"[A-Z]{1,4}-\d+", it["fields"].get("Aliases", "")):
        alias_of[a] = it["id"]

FILE_OF = {}  # raw id -> source file (for provenance)
sources = [
    ("REVIEW-ITEMS.md", review_lr, "defect"),
    ("HYGIENE.md", items_from(LR / "findings/HYGIENE.md"), "hygiene"),
    ("SWEEP.md", items_from(LR / "findings/SWEEP.md"), "investigation"),
    ("INVESTIGATE.md", items_from(LR / "findings/INVESTIGATE.md"), "investigation"),
    ("JOURNEY-DELTA.md", items_from(LR / "findings/JOURNEY-DELTA.md"), "defect"),
    ("TEST-COVERAGE.md", items_from(LR / "findings/TEST-COVERAGE.md"), "test-gap"),
    ("AUTOMATIONS.md", items_from(LR / "findings/AUTOMATIONS.md"), "defect"),
    ("GAPS.md", items_from(LR / "findings/GAPS.md"), "process"),
    ("EXISTING-REVIEWS.md", items_from(LR / "findings/EXISTING-REVIEWS.md"), "gap"),
    ("ARCH-ITEMS.md", items_from(LR / "findings/ARCH-ITEMS.md"), "architecture"),
    ("LEGACY-TRACKERS.md", items_from(LR / "findings/LEGACY-TRACKERS.md"), "idea"),
    ("FROZEN.md", items_from(LR / "findings/FROZEN.md"), "frozen"),
    ("REJECTED.md", items_from(LR / "findings/REJECTED.md"), "rejected"),
]
all_items = []
for fname, its, typ in sources:
    for it in its:
        it["_file"] = fname
        it["_type"] = typ
        FILE_OF[it["id"]] = fname
        all_items.append(it)

# Assign record IDs to every item that becomes a backlog/idea/research-or-closed record.
RECORD_ID = {}
for it in all_items:
    rid_raw = it["id"]
    st = status.get(rid_raw, ["open", ""])[0]
    if it["_type"] in ("frozen",):
        kind = "ideas"
    elif it["_type"] == "idea":
        kind = "ideas"
    elif it["_type"] == "rejected" or st in ("rejected", "fixed") and rid_raw.startswith("REJ"):
        kind = "research"
    elif st == "fixed":
        kind = "research"
    else:
        kind = "backlog"
    it["_kind"] = kind
    if kind == "research":
        continue
    RECORD_ID[rid_raw] = unique_id(rid_raw.lower(), it["title"], 6)

# journeys mapping per backlog item
def journeys_for(it):
    txt = it["fields"].get("Journeys", "") or it["fields"].get("Journeys ", "")
    nums = expand_journeys(txt)
    return [jrec[f"J-{n:03d}"] for n in nums if f"J-{n:03d}" in jrec]


ALIASES_OF = {}
for _a, _lr in alias_of.items():
    ALIASES_OF.setdefault(_lr, []).append(_a)


def related_for(it):
    ids = set(re.findall(ID_RE, it["body"] + " " + it["title"]))
    ids.update(ALIASES_OF.get(it["id"], []))
    out = []
    for r in sorted(ids):
        if r == it["id"]:
            continue
        target = alias_of.get(r, r) if r in alias_of else r
        if target in RECORD_ID and RECORD_ID[target] not in out and target != it["id"]:
            out.append(RECORD_ID[target])
    return out


def frz_target(it):
    txt = status.get(it["id"], ["", ""])[1]
    m = re.search(r"FRZ-\d{3}|FZ-\d{3}", txt + " " + it["body"])
    if m:
        key = m.group(0).replace("FZ-", "FRZ-")
        return RECORD_ID.get(key)
    return None


DEFECT_TYPE = {"CONS": "ux-gap", "UC": "wiring-gap", "FR": "feature-gap", "SP": "plan-gap",
               "AC": "acceptance-gap", "ARCH": "architecture", "NW": "new-finding"}

for it in all_items:
    if it["_kind"] != "backlog":
        continue
    raw = it["id"]
    st, verified = status.get(raw, ["open", ""])
    prefix = raw.split("-")[0]
    typ = it["_type"]
    btype = DEFECT_TYPE.get(prefix) or ("investigation" if st == "investigate" else ("hypothesis" if "hypothesis" in it["fields"].get("Confidence", "") else typ))
    if st == "investigate":
        btype = "investigation"
    shown_title = it["title"].strip()
    if prefix == "ARCH":
        cover_id = alias_of.get(raw)
        cover_title = next((x["title"].strip() for x in review_lr if x["id"] == cover_id), shown_title)
        shown_title = f"{cover_title} (architecture-audit view of {cover_id})"
    meta = dict(
        id=RECORD_ID[raw], title=shown_title, created=DATE, updated=DATE,
        journeys=journeys_for(it), related=related_for(it), docs=doc_paths(it["body"])[:12],
        status="open", owner=None, branch=None, worktree=None, claimed_at=None, blocked_reason=None,
        type=btype, severity=it["sev"], area=it["area"], raw_id=raw, source_file=f"docs/launch-readiness/findings/{it['_file']}",
    )
    closed = None
    if prefix == "ARCH":
        lr = alias_of.get(raw)
        closed = ("duplicate", f"Duplicate of {lr}; the work is tracked on {lr} (record {RECORD_ID.get(lr, '?')}). Closed here so there is one owner for the work.")
    elif st == "frozen":
        tgt = frz_target(it)
        closed = ("superseded", "Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.")
        if tgt:
            meta["related"] = sorted(set(meta["related"] + [tgt]))
    elif st in ("n-a", "accepted"):
        closed = ("declined", f"Not applicable or accepted as-is per the reconciliation: {verified}")
    if closed:
        meta["status"] = "closed"
        meta["resolution"] = closed[0]
        folder = "archive"
        verification = f"{closed[1]}\n\nEvidence: {verified.replace('see LEDGER.md Frozen', 'see findings/FROZEN.md')}"
    else:
        folder = "items"
        verification = (f"Pending. No check has been run: this record was filed from static reading only. "
                        f"Read-only evidence on file: {verified or 'none'}.")
    plan = it["fields"].get("Fix hint", "") or it["fields"].get("Repro or check", "")
    question = it["fields"].get("Why it matters", "")
    acc = []
    if st == "investigate" or btype == "investigation":
        acc.append("- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.")
    else:
        acc.append("- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.")
    if it["fields"].get("Journeys"):
        acc.append(f"- Journeys named in this record's journeys field pass their pass checks after the fix.")
    body = fmt_body([
        ("Problem", f"{it['title'].strip().rstrip('.')}." + (f" {question}" if question else "") +
         (" Suspected, not confirmed (see Confidence in the evidence)." if "hypothesis" in it["fields"].get("Confidence", "") else "")),
        ("Evidence and reproduction", "\n".join(f"- **{k}:** {v}" for k, v in it["fields"].items()) or it["body"]),
        ("Acceptance criteria", "\n".join(acc)),
        ("Plan", plan or "Decide the fix first; record the decision in Attempts."),
        ("Attempts", f"- {DATE} — Filed from {meta['source_file']} ({raw}). Static reading only; nothing executed."
                     + (f" Closed as {closed[0]}." if closed else "")),
        ("Verification", verification),
    ])
    write("backlog", folder, RECORD_ID[raw], meta, body)

# ---------------------------------------------------------------- ideas (frozen + legacy)
for it in all_items:
    if it["_kind"] != "ideas":
        continue
    raw = it["id"]
    st, verified = status.get(raw, ["captured", ""])
    frozen = it["_type"] == "frozen"
    ist = "parked" if frozen else ("rejected" if st == "accepted" else "captured")
    meta = dict(
        id=RECORD_ID[raw], title=it["title"].strip(), created=DATE, updated=DATE,
        journeys=journeys_for(it), related=related_for(it), docs=doc_paths(it["body"])[:8],
        status=ist, promoted_to=[], raw_id=raw, source_file=f"docs/launch-readiness/findings/{it['_file']}",
    )
    body = fmt_body([
        ("Idea", f"{it['title'].strip()}. " + ("Frozen out of this release by the feature freeze (not a commitment). " if frozen else "Captured from the legacy tracker; not a commitment. ")
         + "\n".join(f"- **{k}:** {v}" for k, v in it["fields"].items())),
        ("Open questions", "What would justify promoting this: a real user need, an owner decision, or a failing journey. " + (verified or "")),
        ("Promotion", "No promotion yet. " + ("If promoted, link the new backlog item here and set promoted_to." if not frozen else "Frozen items stay parked until the owner lifts the freeze.")),
    ])
    write("ideas", "items", RECORD_ID[raw], meta, body)

# ---------------------------------------------------------------- decisions
DEC = [
    ("ledger-scaffold-from-setup-repo", "Use the setup repository scaffold for this project's ledgers",
     "The project's development records use the ledgers/ scaffold from the setup repository (~/setup, origin P1927/setup), installed with tools/install.py. Record formats, statuses, and checks follow ledgers/PROTOCOL.md.",
     "Owner instruction in chat on 2026-10-27: the ledger structure is set in the setup repository; copy it here and move the other ledgers in.",
     "The earlier launch-release folder layout was replaced. Its evidence files moved to docs/launch-readiness/."),
    ("merge-review-branch-to-main-without-prs", "Land ledger work by branch then merge to main, with no pull requests",
     "Review and ledger changes are committed on a single feature branch, merged into main with a merge commit, pushed to origin/main, and the branch is deleted. No pull requests are opened.",
     "Owner instruction in chat on 2026-10-27 ('commit and merge things into main ... I don't want PRs').",
     "Conflicts with AGENTS.md's 'work directly on main, no worktrees'. Tracked in the backlog for the owner to settle (GAP-007)."),
]
dec_ids = {}
for slugname, title, decision, authority, consequences in DEC:
    rid = unique_id("decision", title, 6)
    dec_ids[slugname] = rid
    meta = dict(id=rid, title=title, created=DATE, updated=DATE, journeys=[], related=[], docs=[],
                status="accepted", authority=authority, supersedes=[], superseded_by=[])
    body = fmt_body([("Decision", decision), ("Rationale and alternatives", "Chosen by the owner. The alternative was a template or workflow that the owner did not name."),
                     ("Consequences", consequences)])
    write("decisions", "items", rid, meta, body)

# ---------------------------------------------------------------- research (raw reviews, fixed, rejected, legacy, learnings)
def research(slugname, title, question, sources_list, findings, limits, recs, docs, source_rev=REV, related=None):
    rid = unique_id("research", title, 6)
    meta = dict(id=rid, title=title, created=DATE, updated=DATE, journeys=[], related=related or [], docs=docs,
                status="complete", source_revision=source_rev)
    body = fmt_body([("Question", question), ("Sources and method", sources_list), ("Findings", findings),
                     ("Limits", limits), ("Recommendations and follow-up", recs)])
    write("research", "items", rid, meta, body)
    return rid


LIMIT = ("Read-only static reading at the stated revision; nothing was executed. Items filed from this record are unverified until a check is run and recorded.")
RAW_DOCS = {
    "fe-a.md": "Frontend features part A (feed, add-topic, editor, review, schedule, persistence).",
    "fe-b.md": "Frontend features part B and the app shell (pages, auth, OAuth popups, admin, onboarding).",
    "worker-a.md": "Worker dispatcher, auth, persistence, scheduled publish, tenancy.",
    "worker-b.md": "Worker generation, LLM, integrations, newsletter, publish adapters.",
    "gen-pkg.md": "Generation worker and packages/llm-core, packages/researcher.",
    "setup.md": "Setup wizard, deploy scripts, GitHub workflows.",
    "existing-reviews.md": "Reconciliation of the prior reviews (cons/ UX audit, USE-CASES.md, feed report, plans, acceptance criteria).",
}
RAW_ID_HINT = {"fe-a.md": "FEA", "fe-b.md": "FEB", "worker-a.md": "WKA", "worker-b.md": "WKB",
               "gen-pkg.md": "GWP", "setup.md": "SET", "existing-reviews.md": "CONS"}
for fname, desc in RAW_DOCS.items():
    raw_path = LR / "findings/raw" / fname
    ids = re.findall(r"^#{2,4} ([A-Z]{1,4}-\d+)", raw_path.read_text(), re.M)
    filed = sorted({alias_of.get(i, i) for i in ids if alias_of.get(i, i) in RECORD_ID})
    research(fname, f"Raw review output: {desc.split(' (')[0]}",
             f"What does the code in this area get wrong, and what must be verified?",
             f"Read-only review by one reviewer agent at revision {REV}. Scope: {desc} Raw file: docs/launch-readiness/findings/raw/{fname}.",
             f"{len(ids)} raw items in the file. Items filed as backlog records (by ledger record, where the raw ID was merged or kept): {', '.join(RECORD_ID[f] for f in filed) if filed else 'none'}. Raw IDs: {', '.join(ids)}.",
             LIMIT, "Work each filed backlog item; add evidence in its Attempts.",
             [f"docs/launch-readiness/findings/raw/{fname}"])

research("architecture-audit", "Architecture audit: docs versus code conformance",
         "Do the documented architecture, config, and deployment claims match the code?",
         f"Static reading of docs and config at {REV}. docs/launch-readiness/findings/ARCH-AUDIT.md.",
         "20 architecture findings (ARCH-001..020), each tracked as a duplicate of a merged review item or kept as its own record. The conformance table lists each doc claim with its verdict.",
         LIMIT + " The architecture audit missed a tracked env file (HYG-003), so it is not a complete secret scan.",
         "Keep ARCH rows as duplicates of their review items; fix the review item, not the audit.",
         ["docs/launch-readiness/findings/ARCH-AUDIT.md"])
research("doubt-marker-sweep", "Sweep of doubt statements in every raw review",
         "Is every hypothesis, unverified, or TODO-style line in the raw reviews tracked?",
         "grep of doubt markers across raw reviews and findings; each hit judged tracked, new, or rejected. docs/launch-readiness/findings/SWEEP.md has the coverage table.",
         "The sweep reports 100 marker hit lines: 69 already tracked, 27 rejected as ordinary wording or definitions, and 4 hit lines produced 6 new items (SWP-001, SWP-002, INV-021..024). The sweep reports 4 further non-marker doubts, all already tracked. The sweep table itself is the authority for the counts.",
         LIMIT, "Re-run the sweep after each review pass.", ["docs/launch-readiness/findings/SWEEP.md"])
research("journey-delta", "Journey-level code findings checked against the ledger",
         "Does every code finding in the journey file exist as a tracked item?",
         "Each CODE-READING FINDING in docs/launch-readiness/journeys/JOURNEYS.md checked against the review items.",
         "50 findings: 42 covered, 5 new (JRN-001..005), 3 rejected after reading the code.",
         LIMIT, "Keep JRN items linked to their journeys.", ["docs/launch-readiness/findings/JOURNEY-DELTA.md"])
research("test-coverage-map", "Automated test coverage of the P0/P1 core journeys",
         "Which P0/P1 core journeys have an automated test that asserts their pass check?",
         "find and grep over worker, frontend, tests, tests-e2e, generation-worker and setup test files. docs/launch-readiness/findings/TEST-COVERAGE.md.",
         "70 journeys checked: 9 covered, 24 partial, 37 with no test (TST items). 10 of 15 P0 journeys have none. tests-e2e wiring specs assert their own mocks, so they do not count.",
         LIMIT, "Write a test per TST item before its fix.", ["docs/launch-readiness/findings/TEST-COVERAGE.md"])
research("automations-review", "Review of automations/",
         "Do the automation scripts keep state, post safely, and match their docs?",
         "Read of automations/ and .github/workflows/youtube-comment-poll.yml. docs/launch-readiness/findings/AUTOMATIONS.md.",
         "5 findings (AUT-001..005) on the YouTube poller state and replies.",
         LIMIT, "See AUT items.", ["docs/launch-readiness/findings/AUTOMATIONS.md"])
research("hygiene-and-not-implemented", "Tracked-file hygiene and not-implemented journeys",
         "Which tracked files should not be in git, and which journey features are absent?",
         "git ls-files and grep checks at the review revision. docs/launch-readiness/findings/HYGIENE.md.",
         "10 tracked .DS_Store files, tracked agent run state under state/, a tracked frontend/.env.development with a bypass key, YouTube publish rejected, YouTube poll schedule commented out, no test script.",
         LIMIT, "See HYG and NI items.", ["docs/launch-readiness/findings/HYGIENE.md"])
research("rejected-claims", "Review claims that were rejected or already fixed",
         "Which raw claims were wrong, duplicated, or already fixed?",
         "Each claim re-checked in the code. docs/launch-readiness/findings/REJECTED.md.",
         f"{sum(1 for it in all_items if it['_type'] == 'rejected')} entries, each with its reason:\n" + "\n".join(
             f"- {it['id']} ({status.get(it['id'], ['', ''])[0]}): {it['title'].strip()}. Reason: {it['fields'].get('Reason', 'none recorded')}"
             for it in all_items if it['_type'] == 'rejected'),
         LIMIT, "Do not re-file these without new evidence.", ["docs/launch-readiness/findings/REJECTED.md"])
fixed_rows = [(k, v) for k, (s, v) in status.items() if s == "fixed"]
research("fixed-by-reading", "Items the reconciliation found fixed in the current code (read-only)",
         "Which previously reported items does the current code already fix?",
         "Reading of the cited code for each existing-review row marked fixed. Not executed.",
         "\n".join(f"- {k}: {v}" for k, v in sorted(fixed_rows)) or "None.",
         "These are read-only: the fix is visible in the code, not proven by a run. Verification requires an executor (GAP-001).",
         "Run the cited journey before closing any of these as verified.",
         ["docs/launch-readiness/findings/EXISTING-REVIEWS.md"])
research("journey-designer-output", "Journey designer output (146 journeys)",
         "What are the user and operator journeys the code actually supports?",
         "Journeys written from USE-CASES.md, the README, routes, dispatcher actions and wizard steps; each route checked with grep. docs/launch-readiness/journeys/JOURNEYS.md.",
         "146 journeys, each imported as a planned journey record. 47 carry code-reading findings; 3 are NOT IMPLEMENTED (J-013, J-081, J-118).",
         LIMIT + " Pass checks are not executed.", "Run each journey and set its status.",
         ["docs/launch-readiness/journeys/JOURNEYS.md", "docs/launch-readiness/journeys/COVERAGE.md"])
research("review-learnings", "Learnings from the launch-readiness review",
         "What went wrong in the review process, and what must the next review do differently?",
         "Append-only log in docs/launch-readiness/LEARNINGS.md.",
         f"{sum(1 for ln in (LR / 'LEARNINGS.md').read_text().splitlines() if ln.startswith('- 2026-'))} dated entries covering wrong premises, missed files, weak completeness checks, and network failures.",
         "Lessons, not measured results.", "Apply the lessons in the next review.", ["docs/launch-readiness/LEARNINGS.md"])
for fname, desc in [("MCP-PROGRESS.md", "MCP progress notes"), ("MCP-TEST-IDEAS.md", "MCP test ideas"),
                    ("FEED_EXPLORATION_REPORT.md", "Feed exploration report (content playbook and feed design)"), ("ideas.md", "Idea list")]:
    research(f"legacy-{fname.lower().replace('.md','').replace('_','-')}", f"Imported legacy tracker: {fname}",
             f"What did the earlier {desc} record, and which parts are still open?",
             f"Imported unchanged from the repository root: docs/launch-readiness/legacy/{fname}.",
             "Open items were filed as IDEA or FR records; the file is kept as provenance.",
             "Historical import; it does not assert present-day state.",
             "Work from the linked IDEA and FR records, not this file.",
             [f"docs/launch-readiness/legacy/{fname}"], source_rev="historical-import")

# ---------------------------------------------------------------- documents
DOCS = [
    ("architecture-design", "Architecture design (docs/ARCHITECTURE.md)", "docs/ARCHITECTURE.md", "architecture", "review-needed", "Several claims drift from the code (see the architecture audit)."),
    ("setup-guide", "Setup and deployment guide (SETUP.md)", "SETUP.md", "setup-guide", "review-needed", "Deploy steps differ from setup/ and start.sh (see SET and ARCH items)."),
    ("agent-rules", "Agent workflow rules (AGENTS.md)", "AGENTS.md", "agent-rules", "review-needed", "Rules conflict with the review branch decision (GAP-007) and reference test scripts that do not exist (NI-003)."),
    ("launch-readiness-plan", "Launch-readiness plan", "docs/launch-readiness/PLAN.md", "launch-readiness-plan", "current", "Scope and finding format for the review; the review was read-only."),
    ("use-cases-audit-2026-04", "Earlier wiring audit (USE-CASES.md)", "USE-CASES.md", "wiring-audit-2026-04", "historical", "Kept as history; its ✅ claims were re-checked in the review."),
    ("cons-ux-audit", "UX cons audit (cons/README.md)", "cons/README.md", "ux-cons-audit", "historical", "Critique record; open rows are tracked as CONS backlog records."),
]
for slugname, title, path, scope, status_, note in DOCS:
    rid = unique_id("document", title, 6)
    meta = dict(id=rid, title=title, created=DATE, updated=DATE, journeys=[], related=[], docs=[path],
                status=status_, path=path, scope=scope, role="design" if status_ != "historical" else "historical",
                owner=OWNER_NOTE, reviewed_revision=REV if status_ != "historical" else None, superseded_by=[])
    body = fmt_body([("Authority and purpose", f"Canonical or historical record for {scope}. Path: {path}."),
                     ("Maintenance", "Change triggers: edits to the documented area. Link feature, decision and backlog records here when behaviour changes."),
                     ("Known gaps", note)])
    write("documents", "items", rid, meta, body)

# ---------------------------------------------------------------- reviews (overall + section)
def review(scope_type, scope, title, status_, summary_points):
    rid = unique_id("review", title, 7)
    meta = dict(id=rid, title=title, status=status_, created=DATE, updated=DATE, scope_type=scope_type,
                scope=scope, reviewer=REVIEWER, reviewed_at=NOW, source_revision=REV, previous_review=None,
                journeys=[], related=[], docs=["docs/launch-readiness/findings/REVIEW-ITEMS.md"])
    body = fmt_body([
        ("Scope and revision", f"Scope: {scope_type} / {scope}. Source revision {REV} (main before this review). Read-only; nothing executed."),
        ("Executive summary", summary_points[0]),
        ("Current state and capabilities", summary_points[1]),
        ("Changes since previous review", "First review of this scope. There is no previous review."),
        ("Conflicts and architectural issues", summary_points[2]),
        ("Direction and priorities", summary_points[3]),
        ("Follow-up work", "Every item is a linked backlog record (see the backlog index). Priorities follow the severities in the records."),
        ("Evidence and limitations", "Static reading only. Nothing executed. Journeys and findings are unverified until an executor runs them at a named revision."),
    ])
    write("reviews", "items", rid, meta, body)
    return rid

def count_for(prefix_match):
    total = {"open": 0, "investigate": 0, "fixed": 0, "other": 0}
    for k, (s, _) in status.items():
        if prefix_match(k):
            total[s if s in total else "other"] += 1
    return total

ov = count_for(lambda k: True)
review("overall", "application", "Launch readiness of the whole application (read-only)", "complete",
       [f"The review found {ov['open']} open and {ov['investigate']} investigate items across the application and {ov['fixed']} items the current code already fixes. Nothing is verified by execution. The top risks are data-isolation and auth-gate defects (P0): shared channel credentials, a scheduled-publish user drop, an unenforced allowlist, and a shipped dev bypass secret (LR-001). A tracked dev env file with a bypass key (HYG-003) is P1.",
        "Implemented and read: frontend features, worker dispatcher and publish, generation worker, setup wizard, workflows. Missing or not implemented: YouTube publish, YouTube poll schedule, a test script, a pipeline_rows table. Test coverage of P0 journeys is weak (TST items).",
        "Architectural conflicts: per-tenant data and credentials are not isolated in the worker and the generation worker; setup scripts and the Node wizard expose secrets; documented allowlist and bypass behaviour contradict the code (ARCH items, linked as duplicates of review items).",
        "Priority: fix P0 tenancy and secret items first, then add tests for the P0 journeys, then P1. Verify by executing the P0 journeys on a fresh clone before any closure."])
review("section", "frontend", "Frontend section review (read-only)", "complete",
       ["Frontend features and app shell were read by two reviewers. Defects cluster in schedule/reschedule, editor recovery, generation handoff, and auth/OAuth popups.",
        "Feed, editor, schedule and settings screens exist and call the dispatcher; several controls depend on routes or fields that are missing or misnamed (see FEA/FEB items).",
        "Frontend-only checks were not verified as enforcement; the worker reviews carry the authorization findings. Conflicts are listed in the linked backlog records.",
        "Priority: scheduling correctness and the missing-route/field defects first."])
review("section", "worker", "Worker section review (read-only)", "complete",
       ["The main worker dispatcher, auth, publish, scheduled publish, newsletter and generation proxy were read by two reviewers.",
        "The dispatcher accepts client-controlled tenant fields in places, and credentials are shared across users (WKA/WKB items).",
        "The allowlist is not enforced and the scheduled-publish path drops the user identity.",
        "Priority: tenancy and credential isolation, then schedule correctness, then tests."])
review("section", "generation-worker", "Generation worker and packages section review (read-only)", "complete",
       ["The generation worker and packages were read by one reviewer (GWP items). The existing-review reconciler could not grep this directory in one pass.",
        "The generation worker has no per-user identity, and the selector can return unfiltered variants.",
        "Priority: per-user keys and the selector guard; then a second review pass over this directory (GAP-002).",
        "Coverage gap: one reviewer only."])
review("section", "setup", "Setup wizard and deploy scripts section review (read-only)", "complete",
       ["The Node and Python wizards, deploy scripts and workflows were read by one reviewer (SET items), plus the setup and ARCH checks.",
        "The Node wizard is unauthenticated and binds all interfaces; setup prints and rotates secrets; several committed owner IDs break setup for others.",
        "Priority: the wizard exposure and secret handling first (P0), then the non-owner setup path.",
        "Setup was not run; every SET item needs an executor check on a clean machine."])
review("section", "automations", "Automations section review (read-only)", "complete",
       ["automations/ is one YouTube comment poller. The review found state loss and reply-scope defects.",
        "The poller's replied-IDs file is not persisted between CI runs, and the first run replies to all history.",
        "Priority: persist state or make the run idempotent; then limit the first run.",
        "Nothing executed; the workflow schedule is disabled, so the poller is manual-only today."])

# ---------------------------------------------------------------- write everything
written = 0
for kind, folder, rid, meta, body in pending:
    base = L / kind / folder
    base.mkdir(parents=True, exist_ok=True)
    head = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10000)
    text = f"---\n{head}---\n\n{body}"
    if kind == "backlog" and folder == "items" and meta.get("status") == "closed":
        raise SystemExit("closed backlog must be archived")
    (base / f"{rid}.md").write_text(text, encoding="utf-8")
    written += 1
print("wrote", written, "records")
