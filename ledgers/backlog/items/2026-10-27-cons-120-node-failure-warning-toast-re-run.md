---
id: 2026-10-27-cons-120-node-failure-warning-toast-re-run
title: Node-failure warning toast + re-run
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-171-enrichment-node-failures-are-not-surfaced
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/enrichment
raw_id: CONS-120
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Node-failure warning toast + re-run.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C10-2
- **Alias:** C10-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** EnrichmentProgressPanel.tsx (no failed/rerun hits)
- **Covered by:** LR-171

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-120). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (EnrichmentProgressPanel.tsx (no failed/rerun hits)); covered by LR-171.
