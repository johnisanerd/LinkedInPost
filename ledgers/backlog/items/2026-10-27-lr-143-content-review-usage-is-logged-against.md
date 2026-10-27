---
id: 2026-10-27-lr-143-content-review-usage-is-logged-against
title: Content review usage is logged against the topic id, and non-Gemini fenced outputs fail to parse, so the verdict falls to flag.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j069-content-review-checklist-before-publishing
- 2026-10-27-j124-usage-meter-and-usage-page
related: []
docs:
- worker/src/features/content-review/orchestrator.ts
- worker/src/features/content-review/textReviewRunner.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/content-review
raw_id: LR-143
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Content review usage is logged against the topic id, and non-Gemini fenced outputs fail to parse, so the verdict falls to flag.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-069, J-124
- **Aliases:** WKB-029
- **Evidence:** worker/src/features/content-review/orchestrator.ts:51-59; worker/src/features/content-review/textReviewRunner.ts:6-35
- **Repro:** static; executor: set review ref to grok.
- **Fix hint:** Pass the session user id and reuse stripJsonCodeFences.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Pass the session user id and reuse stripJsonCodeFences.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-143). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/features/content-review/orchestrator.ts:51-59.
