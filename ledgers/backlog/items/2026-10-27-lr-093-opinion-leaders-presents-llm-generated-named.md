---
id: 2026-10-27-lr-093-opinion-leaders-presents-llm-generated-named
title: Opinion Leaders presents LLM-generated named people as real without an AI disclaimer
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j047-debate-mode-returns-an-invented-opposing
- 2026-10-27-j048-cross-domain-and-opinion-leader-angles
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
area: frontend/feed
raw_id: LR-093
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Opinion Leaders presents LLM-generated named people as real without an AI disclaimer.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-047, J-048
- **Aliases:** FEA-021
- **Evidence:** frontend/src/features/feed/components/DraftContextView.tsx:531-545
- **Repro:** Open a draft in the feed > Opinion Leaders tab.
- **Fix hint:** Add the same disclaimer as Debate Mode or label them illustrative personas.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add the same disclaimer as Debate Mode or label them illustrative personas.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-093). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/components/DraftContextView.tsx:531-545.
