---
id: 2026-10-27-lr-074-template-assignments-news-snapshots-and-llm
title: template_assignments, news_snapshots and llm_settings are keyed by spreadsheet_id with no user column, so sheetless tenants share one key.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j059-pick-a-writing-pattern-template-for
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
- 2026-10-27-j141-two-tenants-connect-the-same-google
- 2026-10-27-j142-per-user-lists-are-scoped-clips
related: []
docs:
- worker/src/persistence/pipeline-db/pipeline.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/tenancy
raw_id: LR-074
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

template_assignments, news_snapshots and llm_settings are keyed by spreadsheet_id with no user column, so sheetless tenants share one key.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-059, J-140..J-142
- **Aliases:** WKA-028
- **Evidence:** worker/src/persistence/pipeline-db/pipeline.ts (savePatternMetadata, listTemplateAssignments); worker/migrations/0005
- **Repro:** static. Executor: two sheetless users each assign a pattern; call `listPatternAssignments` as one of them.
- **Fix hint:** Add user_id to these tables or key by (user_id, topic_id); require a non-empty tenant key.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add user_id to these tables or key by (user_id, topic_id); require a non-empty tenant key.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-074). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/persistence/pipeline-db/pipeline.ts (savePatternMetadata, listTemplateAssignments).
