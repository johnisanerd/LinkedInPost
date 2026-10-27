---
id: 2026-10-27-inv-010-does-migration-0010-orphan-legacy-rows
title: Does migration 0010 orphan legacy rows and rewrite topic_key? (WKA-027)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-147-migration-0010-may-orphan-legacy-rows
docs:
- worker/migrations/0010_pipeline_user_primary.sql
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: worker/db
raw_id: INV-010
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does migration 0010 orphan legacy rows and rewrite topic_key? (WKA-027). Data loss-like behaviour on upgrading an existing deployment.

## Evidence and reproduction

- **Question:** The backfill sets user_id from users.spreadsheet_id, but the admin sheet is copied from KV lazily after deploy. Do legacy rows end up unreachable?
- **Why it matters:** Data loss-like behaviour on upgrading an existing deployment.
- **How to settle it:** Copy the production D1 data to a scratch database, apply worker/migrations/0010_pipeline_user_primary.sql, and compare row counts per user and topic_key values before and after.
- **Related items:** LR-147
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-010). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: migration file exists (worker/migrations/0010_pipeline_user_primary.sql); behaviour on real data not run. Covered by LR-147..
