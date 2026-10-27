---
id: 2026-10-27-gap-007-repo-rule-conflict-work-on-main
title: 'Repo rule conflict: work on main, no worktrees'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- AGENTS.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: process
severity: P3
area: process/review
raw_id: GAP-007
source_file: docs/launch-readiness/findings/GAPS.md
---

## Problem

Repo rule conflict: work on main, no worktrees.

## Evidence and reproduction

- **Gap:** AGENTS.md says to work directly on main and never use git worktrees. This review used the branch launch-readiness-review at the owner's request, and it is being merged into main.
- **Action:** Decision needed: keep or update that rule.
- **Owner:**

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/GAPS.md (GAP-007). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: AGENTS.md line 'Never use git worktrees; work directly on main branch' confirmed..
