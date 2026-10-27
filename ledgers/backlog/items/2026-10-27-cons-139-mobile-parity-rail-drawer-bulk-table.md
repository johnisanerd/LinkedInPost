---
id: 2026-10-27-cons-139-mobile-parity-rail-drawer-bulk-table
title: Mobile parity (rail, drawer, bulk table scroll)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-095-feed-vote-and-clip-actions-are
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/errors
raw_id: CONS-139
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Mobile parity (rail, drawer, bulk table scroll).

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C13-7
- **Alias:** C13-7
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** CampaignPage.tsx:852 overflow-x-auto; feed rail hidden (C02-10); settings drawer not verified
- **Covered by:** LR-095

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-139). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (CampaignPage.tsx:852 overflow-x-auto; feed rail hidden (C02-10); settings drawer not verified); covered by LR-095.
