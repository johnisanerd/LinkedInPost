---
id: 2026-10-27-lr-062-normalizedeliveryimageurl-rewrites-any-url-with-an
title: normalizeDeliveryImageUrl rewrites any URL with an id= query parameter into a Drive thumbnail URL, breaking or swapping the post image.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j067-pick-and-upload-images-for-a
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j077-publish-to-instagram-image-required
- 2026-10-27-j079-send-via-whatsapp
- 2026-10-27-j080-send-via-telegram
related: []
docs:
- worker/src/integrations/media.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/media
raw_id: LR-062
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

normalizeDeliveryImageUrl rewrites any URL with an id= query parameter into a Drive thumbnail URL, breaking or swapping the post image.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-067, J-076, J-077, J-079, J-080
- **Aliases:** WKB-012
- **Evidence:** worker/src/integrations/media.ts:12-16,28-41
- **Repro:** static. Executor: `normalizeDeliveryImageUrl("https://images.example.com/p.jpg?id=77")`.
- **Fix hint:** Apply the id= and thumbnail patterns only when the host is drive.google.com or docs.google.com.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Apply the id= and thumbnail patterns only when the host is drive.google.com or docs.google.com.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-062). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/integrations/media.ts:12-16,28-41.
