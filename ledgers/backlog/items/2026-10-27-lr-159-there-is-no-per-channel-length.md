---
id: 2026-10-27-lr-159-there-is-no-per-channel-length
title: There is no per-channel length or format validation before publish (LinkedIn 3000, Instagram 2200, Telegram 4096), so users get late errors.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j077-publish-to-instagram-image-required
- 2026-10-27-j078-send-via-gmail
- 2026-10-27-j079-send-via-whatsapp
- 2026-10-27-j080-send-via-telegram
related: []
docs:
- frontend/src/features/review/context/useReviewFlowActions.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: worker/publish
raw_id: LR-159
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

There is no per-channel length or format validation before publish (LinkedIn 3000, Instagram 2200, Telegram 4096), so users get late errors. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-076..J-080
- **Aliases:** FEA-025, WKB-038
- **Evidence:** frontend/src/features/review/context/useReviewFlowActions.ts:624-721; worker/src/index.ts publishContent
- **Repro:** Paste >3000 characters, click Publish to LinkedIn.
- **Fix hint:** Validate per channel in publishContent before any upload and show a counter that blocks Approve/Publish above the limit.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Validate per channel in publishContent before any upload and show a counter that blocks Approve/Publish above the limit.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-159). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of frontend/src/features/review/context/useReviewFlowActions.ts:624-721; confirm by running the Repro and observing the described behaviour.
