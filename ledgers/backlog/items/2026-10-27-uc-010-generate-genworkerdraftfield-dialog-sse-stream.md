---
id: 2026-10-27-uc-010-generate-genworkerdraftfield-dialog-sse-stream
title: Generate -> GenWorkerDraftField dialog, SSE stream
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-163-use-cases-md-and-related-docs
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: wiring-gap
severity: P2
area: frontend/use-cases
raw_id: UC-010
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Generate -> GenWorkerDraftField dialog, SSE stream.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 2, row U-J1.6
- **Alias:** U-J1.6
- **Original tag:** ✅ (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:161,212-220 (dialog exists; "Save & Continue saveDraftVariants" not traced)
- **Covered by:** LR-163

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (UC-010). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (dialog exists; "Save & Continue saveDraftVariants" not traced); covered by LR-163.
