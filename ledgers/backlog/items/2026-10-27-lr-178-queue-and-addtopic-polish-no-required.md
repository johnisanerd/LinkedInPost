---
id: 2026-10-27-lr-178-queue-and-addtopic-polish-no-required
title: 'Queue and AddTopic polish: no required-field asterisk and the republish tooltip does not say it creates a new draft'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j035-add-a-topic-from-the-scratchpad
- 2026-10-27-j091-republish-an-already-published-post
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/queue
raw_id: LR-178
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Queue and AddTopic polish: no required-field asterisk and the republish tooltip does not say it creates a new draft.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-035, J-091
- **Aliases:** C04-6, C04-17
- **Evidence:** frontend/src/features/add-topic/AddTopicPage.tsx:275; frontend/src/components/dashboard/tabs/DashboardQueue.tsx:925
- **Repro:** (static check) Open frontend/src/features/add-topic/AddTopicPage.tsx:275 and confirm the behaviour described in the summary; then exercise the matching journey (J-035, J-091) to observe it.
- **Fix hint:** Add the asterisk and clarify the tooltip.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add the asterisk and clarify the tooltip.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-178). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/add-topic/AddTopicPage.tsx:275.
