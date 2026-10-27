---
id: 2026-10-27-idea-008-frontend-bootstrap-network-timeout-and-empty
title: Frontend bootstrap, network-timeout and empty-feed tests were never run
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-inv-001-do-feed-and-clip-rest-calls
docs: []
status: captured
promoted_to: []
raw_id: IDEA-008
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

Frontend bootstrap, network-timeout and empty-feed tests were never run. Captured from the legacy tracker; not a commitment. - **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (New ideas - frontend coverage)
- **Detail:** Ticked [x] but blocked by a gateway 403. They cover App.tsx with a missing backend URL, backendApi.ts on network timeout and the feed with an empty response. The first relates to INV-001.
- **Action:** Write the three tests.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: listed pending or blocked in the legacy tracker; not re-run here

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
