---
id: 2026-10-27-gap-008-template-source-repo-named-setup-not
title: Template source repo named 'setup' not found
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
type: process
severity: P3
area: process/review
raw_id: GAP-008
source_file: docs/launch-readiness/findings/GAPS.md
resolution: fixed
---

## Problem

Template source repo named 'setup' not found.

## Evidence and reproduction

- **Gap:** The owner named a repository 'setup'. No local repo of that name exists in ~/Documents/GitHub. The ledger template was taken from trade/docs-manager/launch-release and Developer-Tools/skills/release-readiness.
- **Action:** Owner confirms the source repo.
- **Owner:**

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/GAPS.md (GAP-008). Static reading only; nothing executed.
- 2026-10-27 — Found the setup repository at ~/setup (home folder, not ~/Documents/GitHub). The earlier 'no such repo' statement was wrong: the search had not covered the home folder. Corrected here.

## Verification

Correction: the repository exists at /Users/pratyush.mishra/setup (git, origin P1927/setup, with ledgers/ and tools/ledgers). Checked with `ls -la ~/setup` and `git -C ~/setup remote -v`. The scaffold was installed from it and the ledgers were rebuilt on it (commit 85b2fb7 on main).
