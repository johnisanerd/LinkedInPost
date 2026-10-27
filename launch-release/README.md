# launch-release — handover

**Goal:** make LinkedInPost safe to hand to end customers. This folder is the single source of truth for what is wrong, what is missing, what needs investigating, and what is proven.

**Branch:** merged to `main` and synced with `origin/main`. No PRs.

**Core promise and freeze:** see [PLAN.md](PLAN.md).

## Layout

| Path | What it is |
|---|---|
| [PLAN.md](PLAN.md) | Core promise, value criteria, roles, finding format, rules, scope |
| [LEDGER.md](LEDGER.md) | Delivery ledger: the Items table is generated from `findings/*.md` by `build_ledger.py`; Status and Verified come from `status.json` |
| [status.json](status.json) | Source of truth for Status and Verified, keyed by ID |
| [build_ledger.py](build_ledger.py) | Rebuilds the Items table in LEDGER.md (`python3 launch-release/build_ledger.py`) |
| [LEARNINGS.md](LEARNINGS.md) | Append-only learning ledger: dead ends, wrong assumptions, lessons |
| [journeys/JOURNEYS.md](journeys/JOURNEYS.md) | 146 user and operator journeys with pass checks |
| [journeys/COVERAGE.md](journeys/COVERAGE.md) | Journey → open ledger item map |
| [findings/REVIEW-ITEMS.md](findings/REVIEW-ITEMS.md) | Merged code, architecture, setup, and worker review items (LR-IDs) |
| [findings/FROZEN.md](findings/FROZEN.md) | Real items that need a new capability, with the in-scope alternative |
| [findings/REJECTED.md](findings/REJECTED.md) | Raw claims that were wrong or already fixed |
| [findings/EXISTING-REVIEWS.md](findings/EXISTING-REVIEWS.md) | Every row of the prior reviews (cons/, USE-CASES, feed report, plans), with current status |
| [findings/LEGACY-TRACKERS.md](findings/LEGACY-TRACKERS.md) | Open items from the moved root trackers |
| [findings/INVESTIGATE.md](findings/INVESTIGATE.md) | Things that need a check before anyone acts |
| [findings/GAPS.md](findings/GAPS.md) | Review gaps and process issues |
| [findings/ARCH-AUDIT.md](findings/ARCH-AUDIT.md) | Docs-vs-code conformance and architecture gaps |
| [findings/CODE-REVIEW.md](findings/CODE-REVIEW.md) | Index of the per-area code reviews |
| [findings/EXEC-RESULTS.md](findings/EXEC-RESULTS.md) | Execution results (empty: nothing has been executed yet) |
| [findings/raw/](findings/raw/) | Raw per-agent review output the items were merged from |
| [ledgers-legacy/](ledgers-legacy/) | Root trackers moved here: MCP-PROGRESS, MCP-TEST-IDEAS, FEED_EXPLORATION_REPORT, ideas |
| [skill/SKILL.md](skill/SKILL.md) | Copy of the release-readiness skill that defines this layout |
| [fixes/](fixes/) | Fix notes (empty: no product code changed in this pass) |

## Ledger rules

- Status vocabulary: `open` · `in-progress` · `fixed` · `accepted` · `frozen` · `rejected` · `investigate` · `n-a`.
- `fixed` means the current code shows the fix. It is not a verification. A `fixed` item is only proven once an executor reruns its journey and records the command → result in the Verification log.
- Edit findings files and `status.json`, then run `python3 launch-release/build_ledger.py` to regenerate the Items table. Do not hand-edit the Items table.

## How to continue

1. Read [LEDGER.md](LEDGER.md) and sort by Sev. Start with open P0 and P1.
2. Work the `investigate` items in [INVESTIGATE.md](findings/INVESTIGATE.md) and the GAP items in [GAPS.md](findings/GAPS.md) first. They decide what is real.
3. Pick a journey from [JOURNEYS.md](journeys/JOURNEYS.md), run its steps, and record output in `findings/EXEC-RESULTS.md`.
4. Confirm or reject each ledger item on that journey. Change its Verified text from `read-only` to `command → result`.
5. Fix by root cause, add a test, re-run the journey, then set the item to `fixed`.

## Current state

- Ledger filled from every review pass, the reconciled existing reviews, and the moved root trackers.
- Nothing executed. Every item is read-only evidence.
- Next step: an executor runs the P0/P1 journeys on a fresh clone and fills the Verification log.

## Related docs (kept in place, reconciled into the ledger)

- [`../AGENTS.md`](../AGENTS.md) — repo rules. It says to work on `main` and never use worktrees; see GAP-007.
- [`../cons/`](../cons/) — UX cons audit. Kept in place because its files link to each other. Its rows are tracked in EXISTING-REVIEWS.md.
- [`../USE-CASES.md`](../USE-CASES.md) — earlier wiring audit, kept as history.
- [`../docs/plans/video-pipeline/BACKLOG.md`](../docs/plans/video-pipeline/BACKLOG.md) and `video-pipeline/direction/skills/LEDGER.yaml` — belong to the video-pipeline product; out of scope (GAP-004).
