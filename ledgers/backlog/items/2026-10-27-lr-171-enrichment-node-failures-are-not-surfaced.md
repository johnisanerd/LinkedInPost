---
id: 2026-10-27-lr-171-enrichment-node-failures-are-not-surfaced
title: Enrichment node failures are not surfaced with a warning or re-run
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j113-enrichment-page-and-node-catalog-admin
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/enrichment
raw_id: LR-171
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Enrichment node failures are not surfaced with a warning or re-run.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-113
- **Aliases:** C10-2
- **Evidence:** frontend/src/features/generation/EnrichmentProgressPanel.tsx
- **Repro:** (static check) Open frontend/src/features/generation/EnrichmentProgressPanel.tsx and confirm the behaviour described in the summary; then exercise the matching journey (J-053, J-113) to observe it.
- **Fix hint:** Show a warning notice for failed nodes.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Show a warning notice for failed nodes.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-171). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/generation/EnrichmentProgressPanel.tsx.
