---
id: 2026-10-27-lr-142-content-review-is-advisory-only-publish
title: 'Content review is advisory only: publish and the scheduled run never read the verdict or fingerprint'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j069-content-review-checklist-before-publishing
- 2026-10-27-j076-publish-now-to-linkedin
related: []
docs:
- worker/src/features/content-review/orchestrator.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/content-review
raw_id: LR-142
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Content review is advisory only: publish and the scheduled run never read the verdict or fingerprint.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-069, J-076
- **Aliases:** WKB-028
- **Evidence:** worker/src/features/content-review/orchestrator.ts; worker/src/index.ts:4824
- **Repro:** static; executor: review a draft, edit it, publish.
- **Fix hint:** Enforce block and re-review on fingerprint change at publish, or relabel the feature as advisory in the UI.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Enforce block and re-review on fingerprint change at publish, or relabel the feature as advisory in the UI.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-142). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/features/content-review/orchestrator.ts.
