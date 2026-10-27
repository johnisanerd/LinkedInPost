---
id: 2026-10-27-jrn-003-deleting-a-topic-removes-images-and
title: Deleting a topic removes images and D1 data before the sheet row, so a Sheets failure leaves the row visible with its media gone
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j039-delete-a-topic-and-its-generated
related:
- 2026-10-27-lr-073-deleterow-trusts-the-client-row-index
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
area: worker/tenancy
raw_id: JRN-003
source_file: docs/launch-readiness/findings/JOURNEY-DELTA.md
---

## Problem

Deleting a topic removes images and D1 data before the sheet row, so a Sheets failure leaves the row visible with its media gone.

## Evidence and reproduction

- **Journeys:** J-039
- **Covers:** none (LR-073 is about trusting the client row index)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:2289-2299 (deleteGcsObjectsForTopicRow, then Promise.all of D1 deletes, then sheets.deleteRow last)
- **Repro:** Make Sheets fail (revoke the share) and delete a topic. Expect the GCS images and pipeline_state row gone, the sheet row still present, and the topic reappearing as a sheet-only row on the next list. Pass: delete is all-or-nothing or the error tells the user what remains.
- **Fix hint:** Delete the sheet row first (or tolerate its absence), then D1 and GCS; return a partial-failure message if any step fails.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Delete the sheet row first (or tolerate its absence), then D1 and GCS; return a partial-failure message if any step fails.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/JOURNEY-DELTA.md (JRN-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: worker/src/index.ts:2289-2299.
