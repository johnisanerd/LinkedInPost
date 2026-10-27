# launch-release — handover

**Goal:** make LinkedInPost safe to hand to end customers. This folder is the single source of truth for what is wrong, what is missing, and what is proven.

**Branch:** `launch-readiness-review` (single branch, off `main`). Nothing pushed.

**Core promise and freeze:** see [PLAN.md](PLAN.md).

## Layout

| Path | What it is |
|---|---|
| [PLAN.md](PLAN.md) | Core promise, value criteria, roles, finding format, rules, scope |
| [LEDGER.md](LEDGER.md) | The delivery checklist: every backlog item, with Sev / Area / Journeys / Evidence / Status / Verified |
| [journeys/JOURNEYS.md](journeys/JOURNEYS.md) | User and agent journeys, with pass/fail checks |
| [findings/ARCH-AUDIT.md](findings/ARCH-AUDIT.md) | Docs-vs-code conformance and architecture gaps |
| [findings/CODE-REVIEW.md](findings/CODE-REVIEW.md) | Summary index of the per-area code reviews |
| [findings/EXEC-RESULTS.md](findings/EXEC-RESULTS.md) | Execution results (empty: this pass did not run anything) |
| [findings/raw/](findings/raw/) | Raw per-agent output that the ledger was merged from |
| [fixes/](fixes/) | Fix notes (empty: this pass changes no product code) |

## How to continue

1. Read [LEDGER.md](LEDGER.md) and sort by Sev. Start with open P0 and P1.
2. Pick a journey from [JOURNEYS.md](journeys/JOURNEYS.md) and run its steps. Record output in `findings/EXEC-RESULTS.md`.
3. Confirm or reject each ledger item on that journey. Change its `Verified` cell from `read-only` to `command → result`.
4. Fix by root cause, add a test, re-run the journey, then set the item to `fixed`.

## Current state

- Journeys: written from `USE-CASES.md`, the README, the routes, and the `cons/` persona set.
- Existing reviews reconciled against the current code (see `findings/raw/existing-reviews.md`).
- Code reviewed by area (read-only). Nothing executed.
- Next step: an executor runs P0/P1 journeys on a fresh clone, then the fixer batch starts.

## Related docs (not replaced by this folder)

- [`../AGENTS.md`](../AGENTS.md) — repo rules. Note: it says to work on `main`; this review uses a branch at the owner's request.
- [`../cons/`](../cons/) — UX cons audit (its items are reconciled in the ledger, not duplicated).
- [`../USE-CASES.md`](../USE-CASES.md) — earlier wiring audit (kept as history).
