---
id: 2026-10-27-lr-047-the-wizard-shells-out-to-python
title: The wizard shells out to python (not sys.executable) and to cwd-relative setup.py, features.yaml and state files
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j005-wizard-deploy-step-streaming-logs-timeout
related: []
docs:
- setup/wizard/steps/cloudflare.py
- setup/wizard/state.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/wizard
raw_id: LR-047
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The wizard shells out to python (not sys.executable) and to cwd-relative setup.py, features.yaml and state files.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-005
- **Aliases:** SET-014
- **Evidence:** setup/wizard/steps/cloudflare.py:75-78; setup/wizard/state.py:6
- **Repro:** static. `cd ~ && python3 ~/LinkedInPost/setup.py --web`.
- **Fix hint:** Use [sys.executable, ROOT/setup.py] and ROOT-anchored paths everywhere.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use [sys.executable, ROOT/setup.py] and ROOT-anchored paths everywhere.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-047). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/wizard/steps/cloudflare.py:75-78.
