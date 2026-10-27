---
id: 2026-10-27-lr-008-the-setup-wizard-trusts-projectdir-args
title: The setup wizard trusts projectDir, args and env from the request body, allowing remote code execution, command injection and env-file injection.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
- 2026-10-27-j011-local-development-loop
related: []
docs:
- frontend/server/setupWizard.js
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: setup/wizard
raw_id: LR-008
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The setup wizard trusts projectDir, args and env from the request body, allowing remote code execution, command injection and env-file injection.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001..J-003, J-011
- **Aliases:** SET-002, SET-003, SET-004
- **Evidence:** frontend/server/setupWizard.js:270-310; frontend/server/setupWizard.js:355-370
- **Repro:** static. POST `{"projectDir":"/tmp/x","args":[],"envVars":{"PYTHONPATH":"/tmp/evil"}}` to `/api/setup/run-setup-py`.
- **Fix hint:** Fix projectDir to the server repo root, allow-list args and env keys, use spawn with argument arrays (no bash -c), validate key names and reject control chars, merge instead of truncate, write 0600.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Fix projectDir to the server repo root, allow-list args and env keys, use spawn with argument arrays (no bash -c), validate key names and reject control chars, merge instead of truncate, write 0600.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-008). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/server/setupWizard.js:270-310.
