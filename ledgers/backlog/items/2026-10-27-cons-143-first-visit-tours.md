---
id: 2026-10-27-cons-143-first-visit-tours
title: First-visit tours
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P3
area: frontend/errors
raw_id: CONS-143
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

First-visit tours.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C13-11
- **Alias:** C13-11
- **Original tag:** LOW (mapped to P3)
- **Current status:** partial
- **Evidence:** components/Tour.tsx used in DashboardQueue.tsx:431; feed tour FeedPage.tsx:622 (newsletter tour at NewsletterTab.tsx:229)
- **Covered by:** none

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-143). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (newsletter tour at NewsletterTab.tsx:229); no LR item covers it.
