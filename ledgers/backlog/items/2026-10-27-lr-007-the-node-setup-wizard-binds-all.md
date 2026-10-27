---
id: 2026-10-27-lr-007-the-node-setup-wizard-binds-all
title: The Node setup wizard binds all interfaces without auth and returns raw secret values from /api/setup/state
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j011-local-development-loop
related: []
docs:
- frontend/server/setupWizard.js
- start.sh
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: setup/wizard
raw_id: LR-007
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The Node setup wizard binds all interfaces without auth and returns raw secret values from /api/setup/state.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-011
- **Aliases:** SET-001
- **Evidence:** frontend/server/setupWizard.js:595; frontend/server/setupWizard.js:131-141
- **Repro:** static. Run `./start.sh`, then from another host `curl 'http://<lan-ip>:3456/api/setup/state?projectDir=/abs/path/to/repo'`.
- **Fix hint:** server.listen(PORT, 127.0.0.1); return only isSet flags; reject non-localhost Host headers.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

server.listen(PORT, 127.0.0.1); return only isSet flags; reject non-localhost Host headers.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-007). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/server/setupWizard.js:595.
