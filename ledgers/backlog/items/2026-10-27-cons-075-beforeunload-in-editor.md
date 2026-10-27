---
id: 2026-10-27-cons-075-beforeunload-in-editor
title: beforeunload in editor
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-089-the-editor-has-no-beforeunload-guard
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/editor
raw_id: CONS-075
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

beforeunload in editor.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-5
- **Alias:** C06-5
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep beforeunload: only DashboardSettingsDrawer.tsx:1242 (leaving editor with unsaved edits is unguarded at browser level)
- **Covered by:** LR-089

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-075). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (leaving editor with unsaved edits is unguarded at browser level); covered by LR-089.
