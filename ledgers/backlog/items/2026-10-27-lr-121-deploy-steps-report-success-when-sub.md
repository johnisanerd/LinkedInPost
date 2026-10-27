---
id: 2026-10-27-lr-121-deploy-steps-report-success-when-sub
title: Deploy steps report success when sub-steps failed or the worker URL was not found
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j005-wizard-deploy-step-streaming-logs-timeout
- 2026-10-27-j008-verify-step-and-worker-health-probes
related: []
docs:
- setup/cloudflare.py
- setup/wizard/steps/deploy.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: setup/cli
raw_id: LR-121
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Deploy steps report success when sub-steps failed or the worker URL was not found.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002, J-005, J-008
- **Aliases:** SET-020
- **Evidence:** setup/cloudflare.py:141-193,547-572,644-650; setup/wizard/steps/deploy.py:46-51
- **Repro:** static.
- **Fix hint:** Collect failures and exit non-zero; require a resolved URL before reporting success.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Collect failures and exit non-zero; require a resolved URL before reporting success.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-121). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/cloudflare.py:141-193,547-572,644-650.
