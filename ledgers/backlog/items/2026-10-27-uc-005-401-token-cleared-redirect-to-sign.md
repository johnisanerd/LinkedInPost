---
id: 2026-10-27-uc-005-401-token-cleared-redirect-to-sign
title: 401 -> token cleared, redirect to sign-in
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
raw_id: UC-005
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

401 -> token cleared, redirect to sign-in.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 2, row U-J1.1
- **Alias:** U-J1.1
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** services/backendApi.ts (no 401 literal hit; AUTH_ERROR_PATTERN / isAuthErrorMessage :~523, App.tsx onAuthExpired) (message-pattern based, not status based)
- **Covered by:** none

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-005). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: reconciler could not confirm in code (message-pattern based, not status based); needs a check.
