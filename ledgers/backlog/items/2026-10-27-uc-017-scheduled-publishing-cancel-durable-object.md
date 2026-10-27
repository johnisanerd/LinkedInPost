---
id: 2026-10-27-uc-017-scheduled-publishing-cancel-durable-object
title: Scheduled publishing + cancel (Durable Object)
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
type: investigation
severity: P2
area: frontend/use-cases
raw_id: UC-017
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Scheduled publishing + cancel (Durable Object).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J7
- **Alias:** U-J7
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** scheduled-publish/ScheduledPublishBanner.tsx:42 cancel UI; worker/src/scheduled-publish present (alarms not traced)
- **Covered by:** none

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-017). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: reconciler could not confirm in code (alarms not traced); needs a check.
