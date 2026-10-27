---
id: 2026-10-27-lr-097-the-queue-row-has-no-channel
title: The queue row has no channel pill although the onboarding Tour promises one, which risks publishing to the wrong channel.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j040-topic-list-merges-sheets-and-d1
- 2026-10-27-j076-publish-now-to-linkedin
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
area: frontend/queue
raw_id: LR-097
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The queue row has no channel pill although the onboarding Tour promises one, which risks publishing to the wrong channel.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-040, J-076
- **Aliases:** C04-2, NEW-2
- **Evidence:** frontend/src/components/dashboard/tabs/DashboardQueue.tsx:435,768
- **Repro:** (static check) Open frontend/src/components/dashboard/tabs/DashboardQueue.tsx:435,768 and confirm the behaviour described in the summary; then exercise the matching journey (J-040, J-076) to observe it.
- **Fix hint:** Render the channel pill on each row or correct the Tour copy.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Render the channel pill on each row or correct the Tour copy.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-097). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/tabs/DashboardQueue.tsx:435,768.
