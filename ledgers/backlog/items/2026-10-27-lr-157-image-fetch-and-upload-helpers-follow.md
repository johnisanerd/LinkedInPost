---
id: 2026-10-27-lr-157-image-fetch-and-upload-helpers-follow
title: Image fetch and upload helpers follow redirects, read whole bodies with no size cap or host rules, and accept SVG into a public bucket.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j067-pick-and-upload-images-for-a
- 2026-10-27-j143-generated-and-uploaded-images-in-a
related: []
docs:
- worker/src/integrations/media.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/media
raw_id: LR-157
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Image fetch and upload helpers follow redirects, read whole bodies with no size cap or host rules, and accept SVG into a public bucket.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-067, J-143
- **Aliases:** WKA-031, WKB-026 (image part)
- **Evidence:** worker/src/integrations/media.ts:187-205; worker/src/index.ts:5747-5759
- **Repro:** static. Executor: upload a 100 MB data URL.
- **Fix hint:** Cap bytes with a stream limit, allow-list content types excluding SVG, https-only, verify topic ownership, key objects by userId/.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Cap bytes with a stream limit, allow-list content types excluding SVG, https-only, verify topic ownership, key objects by userId/.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-157). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/integrations/media.ts:187-205.
