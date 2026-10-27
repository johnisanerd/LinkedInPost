---
id: 2026-10-27-ac-002-interest-group-crud-endpoints
title: Interest-group CRUD endpoints
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
type: acceptance-gap
severity: P2
area: worker/feed
raw_id: AC-002
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Interest-group CRUD endpoints.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 5, row D3-2
- **Alias:** D3-2
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** worker index.ts:72,1723-1733 (action-based listInterestGroups etc., db/interestGroups.ts) (not REST /api/interest-groups; design differs, functionally present)
- **Covered by:** none

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (AC-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (not REST /api/interest-groups; design differs, functionally present); no LR item covers it.
