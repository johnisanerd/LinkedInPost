---
id: 2026-10-27-lr-041-deploy-worker-aborts-on-a-clean
title: --deploy-worker aborts on a clean .env because the secrets builder rejects the empty bypass secret, after the generation worker is already deployed.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j005-wizard-deploy-step-streaming-logs-timeout
related: []
docs:
- setup/worker_config.py
- setup/cloudflare.py
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
raw_id: LR-041
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

--deploy-worker aborts on a clean .env because the secrets builder rejects the empty bypass secret, after the generation worker is already deployed.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002, J-005
- **Aliases:** SET-008
- **Evidence:** setup/worker_config.py:282; setup/cloudflare.py:600-604
- **Repro:** static. Clean `.env` without `DEV_GOOGLE_AUTH_BYPASS_SECRET`, `python setup.py --deploy-worker`.
- **Fix hint:** Move the bypass key to the optional dict and delete the prod push per the bypass item.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Move the bypass key to the optional dict and delete the prod push per the bypass item.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-041). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/worker_config.py:282.
