---
id: 2026-10-27-lr-106-the-google-id-token-is-kept
title: The Google ID token is kept in localStorage and never refreshed, and several features ignore its expiry, so users hit errors after an hour.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j021-google-id-token-expires-mid-session
- 2026-10-27-j026-sign-out
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/shell
raw_id: LR-106
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The Google ID token is kept in localStorage and never refreshed, and several features ignore its expiry, so users hit errors after an hour.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-021, J-026
- **Aliases:** FEB-014
- **Evidence:** frontend/src/components/GoogleLoginButton.tsx:94; frontend/src/App.tsx:49-61,293-367
- **Repro:** leave a tab open past 1h, then click Connect or Clip. Static reasoning.
- **Fix hint:** Central 401 handling in BackendApi.post, or exchange the ID token for a worker session.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Central 401 handling in BackendApi.post, or exchange the ID token for a worker session.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-106). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/GoogleLoginButton.tsx:94.
