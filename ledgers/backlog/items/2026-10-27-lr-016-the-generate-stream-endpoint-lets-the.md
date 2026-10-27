---
id: 2026-10-27-lr-016-the-generate-stream-endpoint-lets-the
title: The generate-stream endpoint lets the client override server-owned fields (spreadsheetId, llm, imageGen), so callers control tenant and models.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j057-client-supplied-spreadsheetid-overrides-the-server
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: worker/tenancy
raw_id: LR-016
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The generate-stream endpoint lets the client override server-owned fields (spreadsheetId, llm, imageGen), so callers control tenant and models.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-057, J-140
- **Aliases:** WKB-004, GWP-001
- **Evidence:** worker/src/index.ts:877-882
- **Repro:** static. Executor: POST `/api/generate/stream` with `{"spreadsheetId":"<other>","topic":"x"}`; check the generation worker's saved variants key.
- **Fix hint:** Build the generation request from an allow-listed schema and put server-owned fields (spreadsheetId, imageGen, enrichmentSkills) last; same for the callGenerationWorker action.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Build the generation request from an allow-listed schema and put server-owned fields (spreadsheetId, imageGen, enrichmentSkills) last; same for the callGenerationWorker action.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-016). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:877-882.
