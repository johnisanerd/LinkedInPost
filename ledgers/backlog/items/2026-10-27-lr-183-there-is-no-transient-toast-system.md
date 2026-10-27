---
id: 2026-10-27-lr-183-there-is-no-transient-toast-system
title: There is no transient toast system, so Save draft, Approve and AddTopic give no success feedback
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j035-add-a-topic-from-the-scratchpad
- 2026-10-27-j076-publish-now-to-linkedin
related: []
docs:
- frontend/src/components/useAlert.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/shell
raw_id: LR-183
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

There is no transient toast system, so Save draft, Approve and AddTopic give no success feedback.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-035, J-076
- **Aliases:** C04-5, NEW-5
- **Evidence:** frontend/src/features/add-topic/AddTopicPage.tsx:296; frontend/src/components/useAlert.ts
- **Repro:** (static check) Open frontend/src/features/add-topic/AddTopicPage.tsx:296 and confirm the behaviour described in the summary; then exercise the matching journey (J-035, J-076) to observe it.
- **Fix hint:** Reuse the existing local toast from SelectionClipper.tsx for success messages.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Reuse the existing local toast from SelectionClipper.tsx for success messages.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-183). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/add-topic/AddTopicPage.tsx:296.
