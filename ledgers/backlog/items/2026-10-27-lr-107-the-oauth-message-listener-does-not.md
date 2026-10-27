---
id: 2026-10-27-lr-107-the-oauth-message-listener-does-not
title: The OAuth message listener does not check event.origin or event.source and is not removed when the popup closes
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
severity: P2
area: frontend/shell
raw_id: LR-107
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The OAuth message listener does not check event.origin or event.source and is not removed when the popup closes.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-094..J-099
- **Aliases:** FEB-009
- **Evidence:** frontend/src/App.tsx:407-417
- **Repro:** from the console of another window sharing the opener, post a forged message. Static reasoning.
- **Fix hint:** Require event.origin to equal the worker origin and event.source to equal the popup; remove the listener on close.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Require event.origin to equal the worker origin and event.source to equal the popup; remove the listener on close.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-107). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/App.tsx:407-417.
