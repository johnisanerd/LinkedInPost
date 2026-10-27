---
id: 2026-10-27-lr-112-enrichment-modules-fall-back-to-a
title: Enrichment modules fall back to a default signal on any error but record the node as completed
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j062-node-runs-viewer-pipeline-observability
related: []
docs:
- generation-worker/src/modules/emotion/index.ts
- generation-worker/src/modules/_shared/orchestrator.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: generation-worker
raw_id: LR-112
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Enrichment modules fall back to a default signal on any error but record the node as completed.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-062
- **Aliases:** GWP-009
- **Evidence:** generation-worker/src/modules/emotion/index.ts:94; generation-worker/src/modules/_shared/orchestrator.ts:36-67
- **Repro:** static; invalidate the API key mid-run.
- **Fix hint:** Return {signal, degraded, error} or rethrow into the failed path while substituting the default.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return {signal, degraded, error} or rethrow into the failed path while substituting the default.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-112). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/modules/emotion/index.ts:94.
