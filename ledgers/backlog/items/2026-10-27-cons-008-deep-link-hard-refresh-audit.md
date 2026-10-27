---
id: 2026-10-27-cons-008-deep-link-hard-refresh-audit
title: Deep-link hard-refresh audit
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
severity: P1
area: frontend/navigation
raw_id: CONS-008
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Deep-link hard-refresh audit.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-8
- **Alias:** C01-8
- **Original tag:** HIGH (mapped to P1)
- **Current status:** unverified
- **Evidence:** App.tsx:262 stored-path restore (mechanism exists (post-auth return path); no audit seen)
- **Covered by:** none

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-008). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: reconciler could not confirm in code (mechanism exists (post-auth return path); no audit seen); needs a check.
