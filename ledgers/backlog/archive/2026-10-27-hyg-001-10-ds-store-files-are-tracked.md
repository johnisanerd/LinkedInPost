---
id: 2026-10-27-hyg-001-10-ds-store-files-are-tracked
title: 10 .DS_Store files are tracked by git
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: hygiene
severity: P2
area: repo/hygiene
raw_id: HYG-001
source_file: docs/launch-readiness/findings/HYGIENE.md
resolution: fixed
---

## Problem

10 .DS_Store files are tracked by git.

## Evidence and reproduction

- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** `git ls-files | grep .DS_Store` returns 10 paths, including .DS_Store, cons/.DS_Store, docs/.DS_Store, generation-worker/.DS_Store, packages/.DS_Store, setup/.DS_Store. The commit fec687f "chore: update .DS_Store" shows this was committed on purpose or by accident.
- **Repro:** `git ls-files | grep -c '\.DS_Store$'` returns 10.
- **Fix hint:** `git rm --cached` each file and add `.DS_Store` to .gitignore.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

`git rm --cached` each file and add `.DS_Store` to .gitignore.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/HYGIENE.md (HYG-001). Static reading only; nothing executed.
- 2026-10-27 — Untracked the 10 committed .DS_Store files and ignored them (commit 77ad744).

## Verification

Checked on branch wrap-hygiene at commit 77ad744: `git ls-files state | wc -l` -> 0 (was 14); `git ls-files | grep -c '\.DS_Store$'` -> 0 (was 10); `.gitignore` now ignores `.DS_Store`; `git check-ignore -q state/exec/events.jsonl` succeeds. Files remain on disk. Not run: any app test (no code changed).
