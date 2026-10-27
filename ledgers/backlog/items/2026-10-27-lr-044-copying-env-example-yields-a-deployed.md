---
id: 2026-10-27-lr-044-copying-env-example-yields-a-deployed
title: Copying .env.example yields a deployed worker with the public placeholder SECRET_ENCRYPTION_KEY and other placeholders pushed as real secrets.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j007-re-running-setup-py-is-idempotent
related: []
docs:
- setup/worker_config.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/cli
raw_id: LR-044
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Copying .env.example yields a deployed worker with the public placeholder SECRET_ENCRYPTION_KEY and other placeholders pushed as real secrets.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002, J-007
- **Aliases:** SET-017
- **Evidence:** .env.example:9-10,22-23,32-33; setup/worker_config.py:115-122
- **Repro:** static. `cp .env.example .env`, set required fields, `python setup.py --all`.
- **Fix hint:** Comment out placeholder lines in .env.example and reject values matching REPLACE_WITH_ or your_*_here and non-32-byte base64 keys.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Comment out placeholder lines in .env.example and reject values matching REPLACE_WITH_ or your_*_here and non-32-byte base64 keys.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-044). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of .env.example:9-10,22-23,32-33.
