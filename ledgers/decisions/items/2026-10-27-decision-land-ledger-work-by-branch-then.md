---
id: 2026-10-27-decision-land-ledger-work-by-branch-then
title: Land ledger work by branch then merge to main, with no pull requests
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: accepted
authority: Owner instruction in chat on 2026-10-27 ('commit and merge things into main ... I don't want PRs').
supersedes: []
superseded_by: []
---

## Decision

Review and ledger changes are committed on a single feature branch, merged into main with a merge commit, pushed to origin/main, and the branch is deleted. No pull requests are opened.

## Rationale and alternatives

Chosen by the owner. The alternative was a template or workflow that the owner did not name.

## Consequences

Conflicts with AGENTS.md's 'work directly on main, no worktrees'. Tracked in the backlog for the owner to settle (GAP-007).
