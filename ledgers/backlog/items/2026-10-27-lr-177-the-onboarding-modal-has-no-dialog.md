---
id: 2026-10-27-lr-177-the-onboarding-modal-has-no-dialog
title: The onboarding modal has no dialog semantics, focus trap or Escape handling, and labels and focus rings are only partly audited.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j029-first-sign-in-shows-onboarding-skipping
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/onboarding
raw_id: LR-177
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The onboarding modal has no dialog semantics, focus trap or Escape handling, and labels and focus rings are only partly audited.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-029
- **Aliases:** FEB-029, C13-8
- **Evidence:** frontend/src/features/onboarding/OnboardingModal.tsx:56-60
- **Repro:** tab through the page while the modal is open.
- **Fix hint:** Use the shared Dialog primitive and run an accessibility pass.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use the shared Dialog primitive and run an accessibility pass.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-177). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/onboarding/OnboardingModal.tsx:56-60.
