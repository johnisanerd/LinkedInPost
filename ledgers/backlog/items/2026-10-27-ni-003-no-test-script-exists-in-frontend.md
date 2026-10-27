---
id: 2026-10-27-ni-003-no-test-script-exists-in-frontend
title: No `test` script exists in frontend or worker, although AGENTS.md tells agents to run one
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j013-documented-developer-test-commands-exist
related: []
docs:
- AGENTS.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: hygiene
severity: P2
area: worker,frontend/test
raw_id: NI-003
source_file: docs/launch-readiness/findings/HYGIENE.md
---

## Problem

No `test` script exists in frontend or worker, although AGENTS.md tells agents to run one.

## Evidence and reproduction

- **Journeys:** J-013
- **Confidence:** confirmed-by-reading
- **Evidence:** frontend/package.json scripts: prebuild, dev, build, lint, preview, setup-wizard, test:e2e, test:e2e:ui, test:e2e:headed, test:e2e:setup (no `test`). worker/package.json scripts: pretypecheck, dev, dev:default, dev:remote, deploy, typecheck (no `test`). AGENTS.md says `cd frontend && npm run test` and `cd worker && npm run test`.
- **Repro:** `npm run test` in frontend/ or worker/ fails with "Missing script".
- **Fix hint:** add a `test` script that runs the unit tests (or change AGENTS.md to the scripts that exist). Do not add a script that only runs e2e and calls it unit testing.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a `test` script that runs the unit tests (or change AGENTS.md to the scripts that exist). Do not add a script that only runs e2e and calls it unit testing.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/HYGIENE.md (NI-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: checked by reading the cited file and git ls-files.
