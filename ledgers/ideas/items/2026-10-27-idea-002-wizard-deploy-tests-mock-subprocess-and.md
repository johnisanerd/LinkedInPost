---
id: 2026-10-27-idea-002-wizard-deploy-tests-mock-subprocess-and
title: Wizard deploy tests mock subprocess and kill 0% of mutants
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- setup/wizard/steps/deploy.py
status: captured
promoted_to: []
raw_id: IDEA-002
source_file: docs/launch-readiness/findings/LEGACY-TRACKERS.md
---

## Idea

Wizard deploy tests mock subprocess and kill 0% of mutants. Captured from the legacy tracker; not a commitment. - **Source:** launch-release/ledgers-legacy/MCP-TEST-IDEAS.md (mutation_tester on setup/wizard/steps/deploy.py)
- **Detail:** The mutation run reported a 0% kill rate: the tests are decorative.
- **Action:** Add assertions on the deploy step's real outputs, or treat setup tests as non-evidence for the setup P0 items.

## Open questions

What would justify promoting this: a real user need, an owner decision, or a failing journey. read-only: listed pending or blocked in the legacy tracker; not re-run here

## Promotion

No promotion yet. If promoted, link the new backlog item here and set promoted_to.
