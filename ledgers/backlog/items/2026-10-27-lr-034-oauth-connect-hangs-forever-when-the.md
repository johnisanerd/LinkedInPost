---
id: 2026-10-27-lr-034-oauth-connect-hangs-forever-when-the
title: OAuth connect hangs forever when the popup is blocked, and consent refusals or disconnect failures are only logged to the console.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j094-connect-linkedin-popup-oauth
- 2026-10-27-j095-connect-instagram
- 2026-10-27-j096-connect-gmail
- 2026-10-27-j097-connect-youtube
- 2026-10-27-j098-oauth-popup-closed-blocked-or-cancelled
- 2026-10-27-j099-connect-whatsapp-admin-only-phone-selection
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
area: frontend/shell
raw_id: LR-034
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

OAuth connect hangs forever when the popup is blocked, and consent refusals or disconnect failures are only logged to the console.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-094..J-099
- **Aliases:** FEB-005, FEB-006
- **Evidence:** frontend/src/App.tsx:397-418,432-447
- **Repro:** block popups, click Connect LinkedIn. Static reasoning.
- **Fix hint:** If window.open returns null show an alert and return; clear the interval and listener on close; route errors through AlertProvider.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

If window.open returns null show an alert and return; clear the interval and listener on close; route errors through AlertProvider.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-034). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/App.tsx:397-418,432-447.
