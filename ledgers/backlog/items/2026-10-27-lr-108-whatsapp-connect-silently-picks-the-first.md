---
id: 2026-10-27-lr-108-whatsapp-connect-silently-picks-the-first
title: WhatsApp connect silently picks the first phone number
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j079-send-via-whatsapp
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
raw_id: LR-108
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

WhatsApp connect silently picks the first phone number.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-079, J-099
- **Aliases:** FEB-010
- **Evidence:** frontend/src/App.tsx:420-429
- **Repro:** WABA with two numbers. Static reasoning.
- **Fix hint:** Show a picker listing verifiedName and displayPhoneNumber before completeWhatsAppConnection.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Show a picker listing verifiedName and displayPhoneNumber before completeWhatsAppConnection.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-108). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/App.tsx:420-429.
