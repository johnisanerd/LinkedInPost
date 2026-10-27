---
id: 2026-10-27-lr-147-migration-0010-may-orphan-legacy-rows
title: Migration 0010 may orphan legacy rows (backfill before admin sheet is copied from KV) and rewrites topic_key
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j137-apply-new-d1-migrations-on-upgrade
- 2026-10-27-j138-legacy-rows-and-shared-config-data
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
related: []
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
raw_id: LR-147
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Migration 0010 may orphan legacy rows (backfill before admin sheet is copied from KV) and rewrites topic_key. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-137, J-138, J-140
- **Aliases:** WKA-027
- **Evidence:** worker/migrations/0010_pipeline_user_primary.sql
- **Repro:** static. Executor: apply 0010 to a copy of production data and compare row counts per user.
- **Fix hint:** Backfill from the KV/admin mapping before the swap, preserve topic_key and assert row counts; test on a copy of production data.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Backfill from the KV/admin mapping before the swap, preserve topic_key and assert row counts; test on a copy of production data.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-147). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of worker/migrations/0010_pipeline_user_primary.sql; confirm by running the Repro and observing the described behaviour.
