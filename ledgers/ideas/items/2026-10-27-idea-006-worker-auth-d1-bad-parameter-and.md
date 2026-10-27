---
id: 2026-10-27-idea-006-worker-auth-d1-bad-parameter-and
title: Worker auth, D1 bad-parameter and missing-LLM-credential tests were never run
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: captured
promoted_to: []
raw_id: IDEA-006
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

Worker auth, D1 bad-parameter and missing-LLM-credential tests were never run. Captured from the legacy tracker; not a commitment. - **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (New ideas - worker/backend coverage)
- **Detail:** Three ideas are ticked [x] but their own text says they were blocked by a gateway 403 (marked with a cross). They have no result.
- **Action:** Write them as real tests: worker auth middleware, D1 queries with invalid parameters, llm client with missing credentials.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: listed pending or blocked in the legacy tracker; not re-run here

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
