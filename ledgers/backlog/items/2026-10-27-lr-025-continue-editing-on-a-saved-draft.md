---
id: 2026-10-27-lr-025-continue-editing-on-a-saved-draft
title: Continue editing on a saved Draft opens a blank new-topic form because of a wrong query param, and saving creates a duplicate topic.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j035-add-a-topic-from-the-scratchpad
- 2026-10-27-j037-edit-a-topic-s-metadata
- 2026-10-27-j056-send-to-generation-button-on-a
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/editor
raw_id: LR-025
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Continue editing on a saved Draft opens a blank new-topic form because of a wrong query param, and saving creates a duplicate topic.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-035, J-037, J-056
- **Aliases:** FEA-008
- **Evidence:** frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx:122,210; frontend/src/components/dashboard/index.tsx:75-80
- **Repro:** Add a topic (Draft), open it from the list, click "Continue editing": empty form, title empty. Type a title and save: two topics.
- **Fix hint:** Use ?edit= in TopicPostPreviewCard or accept both params in AddTopicPageWithEdit.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use ?edit= in TopicPostPreviewCard or accept both params in AddTopicPageWithEdit.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-025). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx:122,210.
