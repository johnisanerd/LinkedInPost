---
id: 2026-10-27-idea-003-setup-wizard-tests-fixtures-leak-flask
title: setup/wizard/tests fixtures leak Flask state when run with tests/
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: captured
promoted_to: []
raw_id: IDEA-003
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

setup/wizard/tests fixtures leak Flask state when run with tests/. Captured from the legacy tracker; not a commitment. - **Source:** docs/launch-readiness/legacy/MCP-TEST-IDEAS.md (infrastructure bugs)
- **Detail:** Run together with tests/, 10+ tests fail in a cascade; run alone, all 18 pass. The note records only a workaround.
- **Action:** Isolate the Flask client fixture, or document running the suites separately.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: listed pending or blocked in the legacy tracker; not re-run here

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
