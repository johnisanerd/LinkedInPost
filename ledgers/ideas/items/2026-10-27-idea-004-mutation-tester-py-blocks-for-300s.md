---
id: 2026-10-27-idea-004-mutation-tester-py-blocks-for-300s
title: mutation_tester.py blocks for 300s+ (project-root detection, full-repo copy)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- setup/wizard/steps/mode.py
status: rejected
promoted_to: []
raw_id: IDEA-004
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

mutation_tester.py blocks for 300s+ (project-root detection, full-repo copy). Captured from the legacy tracker; not a commitment. - **Source:** docs/launch-readiness/legacy/MCP-TEST-IDEAS.md (mutation_tester systemic issues)
- **Detail:** Run on setup/wizard/steps/mode.py it copied the whole repo to a temp dir and timed out.
- **Action:** Developer tooling; not shipped to users.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: dev-only script (mutation_tester.py at repo root); accepted as out of scope for launch.

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
