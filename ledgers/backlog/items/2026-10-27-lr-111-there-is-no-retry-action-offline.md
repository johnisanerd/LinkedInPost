---
id: 2026-10-27-lr-111-there-is-no-retry-action-offline
title: There is no retry action, offline banner or status-code error messaging, and the ErrorBanner, EmptyState and LoadingSkeleton are unused.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j021-google-id-token-expires-mid-session
- 2026-10-27-j023-backend-unreachable-at-boot
- 2026-10-27-j125-monthly-token-budget-exhausted
related: []
docs:
- frontend/src/components/useAlert.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/shell
raw_id: LR-111
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

There is no retry action, offline banner or status-code error messaging, and the ErrorBanner, EmptyState and LoadingSkeleton are unused.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-021, J-023, J-125
- **Aliases:** C13-2, C13-3, C13-4, C13-5, NEW-3
- **Evidence:** frontend/src/components/ui/ErrorBanner.tsx (zero imports); frontend/src/components/useAlert.ts
- **Repro:** (static check) Open frontend/src/components/ui/ErrorBanner.tsx (zero imports) and confirm the behaviour described in the summary; then exercise the matching journey (J-021, J-023, J-125) to observe it.
- **Fix hint:** Adopt ErrorBanner in the load paths already touched by the silent-failure fixes and map status codes to copy.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Adopt ErrorBanner in the load paths already touched by the silent-failure fixes and map status codes to copy.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-111). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/ui/ErrorBanner.tsx (zero imports).
