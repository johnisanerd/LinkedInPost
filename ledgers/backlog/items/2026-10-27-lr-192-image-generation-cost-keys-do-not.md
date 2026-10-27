---
id: 2026-10-27-lr-192-image-generation-cost-keys-do-not
title: Image generation cost keys do not match model ids so image cost logs as 0 USD
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j068-ai-image-generation-text-and-reference
- 2026-10-27-j124-usage-meter-and-usage-page
related: []
docs:
- worker/src/llm/pricing.ts
- worker/src/image-gen/model-catalog.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: worker/llm
raw_id: LR-192
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Image generation cost keys do not match model ids so image cost logs as 0 USD.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-068, J-124
- **Aliases:** WKB-042
- **Evidence:** worker/src/llm/pricing.ts:36-60; worker/src/image-gen/model-catalog.ts:11-37
- **Repro:** static.
- **Fix hint:** Key by the real model id.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Key by the real model id.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-192). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/llm/pricing.ts:36-60.
