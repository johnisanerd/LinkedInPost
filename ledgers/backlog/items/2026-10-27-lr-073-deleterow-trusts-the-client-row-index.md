---
id: 2026-10-27-lr-073-deleterow-trusts-the-client-row-index
title: deleteRow trusts the client row index and image URLs, so a stale tab deletes the wrong sheet row and a forged row deletes any stored object.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j039-delete-a-topic-and-its-generated
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
- 2026-10-27-j143-generated-and-uploaded-images-in-a
related: []
docs:
- worker/src/index.ts
- worker/src/persistence/drafts.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/tenancy
raw_id: LR-073
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

deleteRow trusts the client row index and image URLs, so a stale tab deletes the wrong sheet row and a forged row deletes any stored object.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-039, J-140, J-143
- **Aliases:** WKA-010
- **Evidence:** worker/src/index.ts:2289-2299,5309-5362; worker/src/persistence/drafts.ts:436-441
- **Repro:** static. Executor: open two tabs, delete a topic in one, delete another in the stale tab, check which Topics row disappeared.
- **Fix hint:** Re-read the row by (userId, topicId) server-side and use its indexes and URLs; delete Sheets first then D1.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Re-read the row by (userId, topicId) server-side and use its indexes and URLs; delete Sheets first then D1.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-073). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:2289-2299,5309-5362.
