---
id: 2026-10-27-cons-129-pre-apply-diff-in-generationpanel
title: Pre-apply diff in GenerationPanel
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/signals
raw_id: CONS-129
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Pre-apply diff in GenerationPanel.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C11-4
- **Alias:** C11-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** ReviewDialogs.tsx:133 compare preview exists for editor scope (GenerationPanel diff not verified)
- **Covered by:** none

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-129). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (GenerationPanel diff not verified); no LR item covers it.
