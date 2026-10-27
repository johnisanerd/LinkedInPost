---
id: 2026-10-27-lr-190-the-workflow-engine-is-not-run
title: The workflow engine is not run by any route and its validator truncation would destroy line breaks
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j061-custom-workflows-post-types
- 2026-10-27-j062-node-runs-viewer-pipeline-observability
- 2026-10-27-j113-enrichment-page-and-node-catalog-admin
related: []
docs:
- worker/src/engine/executor/WorkflowRunner.ts
- worker/src/engine/nodes/definitions/constraint-validator.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: worker/engine
raw_id: LR-190
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The workflow engine is not run by any route and its validator truncation would destroy line breaks.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-061, J-062, J-113
- **Aliases:** WKB-044
- **Evidence:** worker/src/engine/executor/WorkflowRunner.ts; worker/src/engine/nodes/definitions/constraint-validator.ts:58-64
- **Repro:** static; grep `runWorkflow`.
- **Fix hint:** Treat engine/ as dead until wired; when wired validate variant count and truncate by sentence.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Treat engine/ as dead until wired; when wired validate variant count and truncate by sentence.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-190). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/engine/executor/WorkflowRunner.ts.
