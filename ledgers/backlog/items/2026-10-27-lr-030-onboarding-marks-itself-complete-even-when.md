---
id: 2026-10-27-lr-030-onboarding-marks-itself-complete-even-when
title: Onboarding marks itself complete even when the sheet connect fails, with no message, and never reappears
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j029-first-sign-in-shows-onboarding-skipping
- 2026-10-27-j030-onboarding-with-a-sheet-url-drive
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/onboarding
raw_id: LR-030
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Onboarding marks itself complete even when the sheet connect fails, with no message, and never reappears.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-029, J-030
- **Aliases:** FEB-004
- **Evidence:** frontend/src/App.tsx:449-465; frontend/src/features/onboarding/OnboardingModal.tsx:31-40
- **Repro:** paste a sheet URL the service account cannot share, click Connect & start; modal closes silently. Static reasoning.
- **Fix hint:** Keep the modal open on failure and only call completeOnboarding after success or an explicit Skip.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Keep the modal open on failure and only call completeOnboarding after success or an explicit Skip.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-030). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/App.tsx:449-465.
