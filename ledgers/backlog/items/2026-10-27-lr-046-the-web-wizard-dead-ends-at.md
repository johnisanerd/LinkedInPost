---
id: 2026-10-27-lr-046-the-web-wizard-dead-ends-at
title: 'The web wizard dead-ends at the Cloudflare step: the Google step writes GOOGLE_SERVICE_ACCOUNT_JSON but setup.py needs GOOGLE_CREDENTIALS_JSON.'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j134-missing-or-invalid-google-service-account
related:
- 2026-10-27-lr-079-several-env-names-read-by-the
docs:
- setup/wizard/steps/google.py
- setup/google_resources.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/wizard
raw_id: LR-046
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The web wizard dead-ends at the Cloudflare step: the Google step writes GOOGLE_SERVICE_ACCOUNT_JSON but setup.py needs GOOGLE_CREDENTIALS_JSON.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-134
- **Aliases:** SET-013, ARCH-014 (credential name)
- **Evidence:** setup/wizard/steps/google.py:72; setup/google_resources.py:133-143
- **Repro:** static. Walk the wizard with valid inputs; at step 4 observe `[fail] GOOGLE_CREDENTIALS_JSON: not set`.
- **Fix hint:** Write the canonical name, add a bucket field, or pass --skip-google when the wizard has no Drive bootstrap.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Write the canonical name, add a bucket field, or pass --skip-google when the wizard has no Drive bootstrap.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-046). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/wizard/steps/google.py:72.
