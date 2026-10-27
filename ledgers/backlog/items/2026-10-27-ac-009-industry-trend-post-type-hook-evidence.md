---
id: 2026-10-27-ac-009-industry-trend-post-type-hook-evidence
title: Industry Trend post type + HOOK->EVIDENCE->... structure
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs:
- worker/src/engine/workflows/definitions/trend-commentary.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: acceptance-gap
severity: P2
area: worker/generation
raw_id: AC-009
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Industry Trend post type + HOOK->EVIDENCE->... structure.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 5, row D2-2
- **Alias:** D2-2
- **Original tag:** AC2 (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** worker/src/engine/workflows/definitions/trend-commentary.ts; __tests__/contentPostTypesPlaybook.spec.test.ts
- **Covered by:** none

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (AC-009). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (worker/src/engine/workflows/definitions/trend-commentary.ts; __tests__/contentPostTypesPlaybook.spec.test.ts); no LR item covers it.
