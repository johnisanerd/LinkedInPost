---
id: 2026-10-27-lr-096-onboarding-requests-the-full-google-drive
title: Onboarding requests the full Google Drive scope and forwards the access token to the worker just to share one sheet.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j030-onboarding-with-a-sheet-url-drive
- 2026-10-27-j032-connect-a-sheet-from-connections-consent
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/onboarding
raw_id: LR-096
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Onboarding requests the full Google Drive scope and forwards the access token to the worker just to share one sheet.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-030, J-032
- **Aliases:** FEB-012
- **Evidence:** frontend/src/features/onboarding/OnboardingModal.tsx:30-33; frontend/src/App.tsx:453-455
- **Repro:** static reasoning.
- **Fix hint:** Use drive.file plus Picker or the manual share path; verify the worker does not persist the token.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use drive.file plus Picker or the manual share path; verify the worker does not persist the token.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-096). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/onboarding/OnboardingModal.tsx:30-33.
