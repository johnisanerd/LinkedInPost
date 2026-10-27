---
id: 2026-10-27-inv-008-can-production-users-see-mock-trending
title: Can production users see mock trending data? (FEB-020, NEW-6, U-J11)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-094-trending-falls-back-to-hard-coded
docs:
- frontend/src/features/trending/hooks/useTrending.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: frontend/trending
raw_id: INV-008
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Can production users see mock trending data? (FEB-020, NEW-6, U-J11). Invented YouTube videos and topics would be shown as real trends.

## Evidence and reproduction

- **Question:** useTrending returns MOCK_TRENDING_DATA when useRealApis is false. Is the sample data labelled in the UI, and can the flag be false in production?
- **Why it matters:** Invented YouTube videos and topics would be shown as real trends.
- **How to settle it:** Read frontend/src/features/trending/hooks/useTrending.ts:196-225,280-292 and where useRealApis is computed; open trending with no API keys on a test build and look for a Sample label.
- **Related items:** LR-094
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-008). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code has the mock path (useTrending.ts:280-292); the label and the flag source were not checked. Covered by LR-094..
