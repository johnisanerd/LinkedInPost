---
id: 2026-10-27-jrn-004-when-the-sheets-merge-fails-the
title: When the Sheets merge fails, the topic list silently falls back to D1 rows with no signal to the user that the sheet is out of sync
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j129-google-sheets-unavailable-or-unshared-during
related:
- 2026-10-27-lr-055-addtopic-swallows-a-sheets-failure-so
- 2026-10-27-lr-091-feed-load-has-no-cancellation-or
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/db
raw_id: JRN-004
source_file: docs/launch-readiness/findings/JOURNEY-DELTA.md
---

## Problem

When the Sheets merge fails, the topic list silently falls back to D1 rows with no signal to the user that the sheet is out of sync.

## Evidence and reproduction

- **Journeys:** J-129
- **Covers:** none (LR-091 is the feed load error state; LR-055 is addTopic)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:1559-1569 (catch logs to console and returns pipeline.getRowsByUserId())
- **Repro:** Unshare the sheet from the service account, open the queue. Expect rows to load with no banner; edits then diverge from the sheet. Pass: a visible "sheet unavailable, showing saved copy" notice.
- **Fix hint:** Return a flag (for example sheetSyncOk:false) alongside the fallback rows and have the queue show a banner.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return a flag (for example sheetSyncOk:false) alongside the fallback rows and have the queue show a banner.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/JOURNEY-DELTA.md (JRN-004). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: worker/src/index.ts:1559-1569.
