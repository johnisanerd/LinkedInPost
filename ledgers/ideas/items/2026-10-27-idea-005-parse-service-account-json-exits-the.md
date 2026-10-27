---
id: 2026-10-27-idea-005-parse-service-account-json-exits-the
title: parse_service_account_json exits the process via fail()/sys.exit(1)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: captured
promoted_to: []
raw_id: IDEA-005
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

parse_service_account_json exits the process via fail()/sys.exit(1). Captured from the legacy tracker; not a commitment. - **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (DESIGN ISSUE note)
- **Detail:** The function cannot be unit-tested without mocking sys.exit, and a library helper kills the wizard process on bad input.
- **Action:** Raise an exception from the helper and let the caller decide.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: listed pending or blocked in the legacy tracker; not re-run here

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
