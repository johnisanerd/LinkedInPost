---
id: 2026-10-27-lr-128-the-python-wizard-has-no-csrf
title: The Python wizard has no CSRF or Host/Origin protection, so a visited web page can trigger a deploy or overwrite config
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j005-wizard-deploy-step-streaming-logs-timeout
related: []
docs:
- setup/wizard/server.py
- setup/wizard/steps/deploy.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/wizard
raw_id: LR-128
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The Python wizard has no CSRF or Host/Origin protection, so a visited web page can trigger a deploy or overwrite config.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-005
- **Aliases:** SET-024
- **Evidence:** setup/wizard/server.py:14,44; setup/wizard/steps/deploy.py
- **Repro:** static.
- **Fix hint:** Per-run random CSRF token, validate Host and Origin, random secret_key.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Per-run random CSRF token, validate Host and Origin, random secret_key.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-128). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/wizard/server.py:14,44.
