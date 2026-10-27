---
id: 2026-10-27-nw-003-components-ui-errorbanner-tsx-emptystate-tsx
title: components/ui/ErrorBanner.tsx, EmptyState.tsx, LoadingSkeleton.tsx are unused dead code; cons doc 13 treats them as the fix, but nothing adopts them.
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-111-there-is-no-retry-action-offline
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: new-finding
severity: P2
area: frontend/errors
raw_id: NW-003
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

components/ui/ErrorBanner.tsx, EmptyState.tsx, LoadingSkeleton.tsx are unused dead code; cons doc 13 treats them as the fix, but nothing adopts them.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md, row NEW-3
- **Alias:** NEW-3
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-111

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (NW-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (no code evidence given by reconciler); covered by LR-111.
