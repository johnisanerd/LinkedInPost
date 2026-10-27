---
id: 2026-10-27-lr-188-small-access-admin-defects-sql-text
title: 'Small access/admin defects: SQL text interpolation of days, suspended or removed admins stay admin via env, suspending an admin email does nothing.'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j123-admin-panel-users-approve-suspend-budget
- 2026-10-27-j124-usage-meter-and-usage-page
related: []
docs:
- worker/src/db/llm-usage.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: worker/auth
raw_id: LR-188
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Small access/admin defects: SQL text interpolation of days, suspended or removed admins stay admin via env, suspending an admin email does nothing.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-123, J-124
- **Aliases:** WKA-038
- **Evidence:** worker/src/db/llm-usage.ts:57-62; worker/src/index.ts:3070-3084
- **Repro:** static.
- **Fix hint:** Bind days as a parameter and refuse to suspend admin emails explicitly.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Bind days as a parameter and refuse to suspend admin emails explicitly.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-188). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/db/llm-usage.ts:57-62.
