---
id: 2026-10-27-gap-010-existing-review-rows-marked-unverified-were
title: Existing-review rows marked unverified were never checked
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- USE-CASES.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: process
severity: P2
area: process/review
raw_id: GAP-010
source_file: docs/launch-readiness/findings/GAPS.md
---

## Problem

Existing-review rows marked unverified were never checked.

## Evidence and reproduction

- **Gap:** Rows marked unverified in the cons/ audits, USE-CASES.md and the acceptance criteria were never checked in code. See the investigate rows in EXISTING-REVIEWS.md.
- **Action:** Check them after execution, or accept the unverified claims as stale documentation.
- **Owner:**

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/GAPS.md (GAP-010). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: EXISTING-REVIEWS.md carries these rows with status investigate..
