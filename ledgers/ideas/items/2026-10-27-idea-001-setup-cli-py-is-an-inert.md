---
id: 2026-10-27-idea-001-setup-cli-py-is-an-inert
title: 'setup/cli.py is an inert scaffold: parse_args() runs but nothing executes'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- setup/cli.py
- setup.py
status: captured
promoted_to: []
raw_id: IDEA-001
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

setup/cli.py is an inert scaffold: parse_args() runs but nothing executes. Captured from the legacy tracker; not a commitment. - **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (bootstrap idempotency test note)
- **Detail:** setup/cli.py is 40 lines: parse_args() and a __main__ call, no main action. Flags (including --web) are accepted and do nothing. The real entry is setup.py.
- **Action:** Delete the dead CLI or make it fail with a pointer to setup.py, so nobody thinks it configures anything.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: setup/cli.py read: 40 lines, only parse_args() (lines 9-40); no action code.

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
