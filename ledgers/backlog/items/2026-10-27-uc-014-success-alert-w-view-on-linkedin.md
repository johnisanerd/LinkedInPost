---
id: 2026-10-27-uc-014-success-alert-w-view-on-linkedin
title: Success alert w/ "View on LinkedIn" link
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-088-there-is-no-permalink-or-view
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
raw_id: UC-014
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Success alert w/ "View on LinkedIn" link.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 2, row U-J1.10
- **Alias:** U-J1.10
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** unverified
- **Evidence:** useDashboardQueue.ts:587 shows generic 'Success' alert; no permalink/“View on” anywhere in frontend or worker (likely false claim)
- **Covered by:** LR-088

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-014). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: reconciler could not confirm in code (likely false claim); needs a check; covered by LR-088.
