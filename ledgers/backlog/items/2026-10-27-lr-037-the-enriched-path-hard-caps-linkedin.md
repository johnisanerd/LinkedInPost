---
id: 2026-10-27-lr-037-the-enriched-path-hard-caps-linkedin
title: The enriched path hard-caps LinkedIn posts at 800 characters (legacy path 100) while review allows 3000, and pattern.maxPostChars is ignored.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j063-open-generated-variants-and-pick-one
- 2026-10-27-j076-publish-now-to-linkedin
related: []
docs:
- generation-worker/src/modules/_shared/creator.ts
- generation-worker/src/modules/_shared/selector.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: generation-worker
raw_id: LR-037
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The enriched path hard-caps LinkedIn posts at 800 characters (legacy path 100) while review allows 3000, and pattern.maxPostChars is ignored.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-063, J-076
- **Aliases:** GWP-007
- **Evidence:** generation-worker/src/modules/_shared/creator.ts:17-24,184; generation-worker/src/modules/_shared/selector.ts:13-20
- **Repro:** static; generate a linkedin post and inspect lengths (expect at most 800).
- **Fix hint:** Use one shared channel-limit constant (3000 for LinkedIn), honour pattern.maxPostChars, fix the legacy 100.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use one shared channel-limit constant (3000 for LinkedIn), honour pattern.maxPostChars, fix the legacy 100.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-037). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/modules/_shared/creator.ts:17-24,184.
