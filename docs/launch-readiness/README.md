# Launch readiness: evidence folder

The ledger of record is [ledgers/](../../ledgers/README.md), built from the setup repository scaffold (see [ledgers/PROTOCOL.md](../../ledgers/PROTOCOL.md)). Start there: search it before filing, claim before working, and never close an item without a dated Attempts entry and Verification.

This folder holds the evidence the ledger records cite. It is not a second ledger.

| Path | What it is |
|---|---|
| [PLAN.md](PLAN.md) | Core promise, value criteria, finding format, rules |
| [findings/](findings/) | Per-area review output: REVIEW-ITEMS, HYGIENE, SWEEP, INVESTIGATE, JOURNEY-DELTA, TEST-COVERAGE, AUTOMATIONS, GAPS, EXISTING-REVIEWS, LEGACY-TRACKERS, FROZEN, REJECTED, ARCH-AUDIT, ARCH-ITEMS, EXEC-RESULTS |
| [findings/raw/](findings/raw/) | Raw reviewer output the review items were merged from |
| [journeys/](journeys/) | Journey designer output (JOURNEYS.md) and the journey-to-item coverage table |
| [legacy/](legacy/) | Root trackers moved here: MCP-PROGRESS, MCP-TEST-IDEAS, FEED_EXPLORATION_REPORT, ideas |
| [LEARNINGS.md](LEARNINGS.md) | Append-only lessons from the review. Also imported as a research record |
| [status.json](status.json) | Pre-setup status snapshot (ID to status and read-only evidence). Superseded by the ledger records; kept for provenance |
| [skill/SKILL.md](skill/SKILL.md) | Copy of the release-readiness skill that defined the first layout |

## State

- Ledger: `python3 tools/ledgers/manage.py check` passes on all records.
- Nothing has been executed. Every review item is read-only evidence until an executor runs its journey and records the result in the item's Verification.
- Next step for whoever picks this up: claim a P0 backlog item, read its Evidence, reproduce it, and record the result in its Attempts.
