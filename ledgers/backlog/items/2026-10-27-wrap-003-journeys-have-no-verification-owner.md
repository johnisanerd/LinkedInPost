---
id: 2026-10-27-wrap-003-journeys-have-no-verification-owner
title: 146 journeys have no verification owner, so no one is accountable for running them
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
type: decision
raw_id: WRAP-003
source_file: docs/launch-readiness/findings/GAPS.md (wrap-up)
---

## Problem

Every journey record in ledgers/journeys carries verification_owner 'unassigned (owner to set)'. A journey can only become verified with a named owner, so none can be verified yet.

## Evidence and reproduction

`grep -l 'unassigned (owner to set)' ledgers/journeys/items/*.md | wc -l` -> 146.

## Acceptance criteria

- Each journey names a verification owner, or the owner records a rule (for example one owner per section).

## Plan

Owner decision: pick owners per section (frontend, worker, generation-worker, setup, automations, application). Recommendation: one owner per section, recorded in the section review.

## Attempts

- 2026-10-27 — Filed during wrap-up. Options and recommendation recorded; no owner chosen.

## Verification

Pending. Owner decision needed.

