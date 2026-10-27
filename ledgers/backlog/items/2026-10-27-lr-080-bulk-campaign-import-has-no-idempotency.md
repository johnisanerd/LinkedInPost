---
id: 2026-10-27-lr-080-bulk-campaign-import-has-no-idempotency
title: Bulk campaign import has no idempotency key or duplicate check, so a retry after a timeout adds every topic twice
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j106-bulk-import-by-pasting-campaign-json
- 2026-10-27-j108-re-importing-the-same-campaign-duplicate
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
area: frontend/campaign
raw_id: LR-080
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Bulk campaign import has no idempotency key or duplicate check, so a retry after a timeout adds every topic twice.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-106, J-108
- **Aliases:** FEB-022
- **Evidence:** frontend/src/features/campaign/CampaignPage.tsx:463-493
- **Repro:** import, kill the connection mid-response, retry. Static reasoning.
- **Fix hint:** Client-generated import id stored by the worker, or dedupe by topic and date; show a row-count confirm.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Client-generated import id stored by the worker, or dedupe by topic and date; show a row-count confirm.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-080). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/campaign/CampaignPage.tsx:463-493.
