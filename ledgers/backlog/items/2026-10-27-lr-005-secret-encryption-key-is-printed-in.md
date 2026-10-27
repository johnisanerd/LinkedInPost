---
id: 2026-10-27-lr-005-secret-encryption-key-is-printed-in
title: SECRET_ENCRYPTION_KEY is printed in clear in the bootstrap summary and streamed to the wizard browser
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j005-wizard-deploy-step-streaming-logs-timeout
related: []
docs:
- setup/worker_config.py
- setup/wizard/steps/deploy.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: setup/cli
raw_id: LR-005
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

SECRET_ENCRYPTION_KEY is printed in clear in the bootstrap summary and streamed to the wizard browser.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-002, J-005
- **Aliases:** SET-005
- **Evidence:** setup/worker_config.py:439; setup/wizard/steps/deploy.py:35-36,90
- **Repro:** static. Run `python setup.py --cloudflare`, read the summary.
- **Fix hint:** Print a masked placeholder like the other secrets.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Print a masked placeholder like the other secrets.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-005). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/worker_config.py:439.
