---
id: 2026-10-27-lr-023-topicgenerationrules-is-used-for-both-add
title: topicGenerationRules is used for both Add-Topic JSON metadata and topic rules text, so metadata replaces the user's and global rules.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j035-add-a-topic-from-the-scratchpad
- 2026-10-27-j037-edit-a-topic-s-metadata
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j056-send-to-generation-button-on-a
- 2026-10-27-j071-personal-generation-rules-my-rules
- 2026-10-27-j072-global-generation-rules-admin-and-history
- 2026-10-27-j075-per-topic-rules-and-template-precedence
related: []
docs:
- frontend/src/features/review/context/useReviewFlowState.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/editor
raw_id: LR-023
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

topicGenerationRules is used for both Add-Topic JSON metadata and topic rules text, so metadata replaces the user's and global rules.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-035, J-037, J-053, J-056, J-071, J-072, J-075
- **Aliases:** FEA-005
- **Evidence:** frontend/src/features/review/context/useReviewFlowState.ts:65-81; worker/src/index.ts:1639,1658,1186-1200
- **Repro:** Add a topic with an "About" text and a Style. Open it in the editor: Rules panel shows `{"about":...}` and `Topic overrides` is on; generate a draft: the user's global rules are not applied. Then type rules in the panel and save: reopen Add-Topic edit and the fields are empty.
- **Fix hint:** Store Add-Topic metadata in its own field (topic_meta) and keep topicGenerationRules for rules only.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Store Add-Topic metadata in its own field (topic_meta) and keep topicGenerationRules for rules only.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-023). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowState.ts:65-81.
