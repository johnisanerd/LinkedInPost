---
id: 2026-10-27-uc-008-addtopic-7-fields-redirect-to-dashboard
title: AddTopic "7 fields", redirect to /dashboard
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
raw_id: UC-008
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

AddTopic "7 fields", redirect to /dashboard.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 2, row U-J1.4
- **Alias:** U-J1.4
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** AddTopicPage.tsx:296 navigate (route /dashboard not confirmed)
- **Covered by:** none

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-008). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: reconciler could not confirm in code (route /dashboard not confirmed); needs a check.
