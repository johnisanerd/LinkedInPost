---
id: 2026-10-27-lr-021-the-in-app-linkedin-guide-tells
title: The in-app LinkedIn guide tells users to register /api/auth/linkedin/callback but the real worker route is /auth/linkedin/callback.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j094-connect-linkedin-popup-oauth
- 2026-10-27-j101-oauth-misconfiguration-missing-or-wrong-client
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/automations
raw_id: LR-021
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The in-app LinkedIn guide tells users to register /api/auth/linkedin/callback but the real worker route is /auth/linkedin/callback.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-094, J-101
- **Aliases:** ARCH-008
- **Evidence:** frontend/src/features/automations/LinkedInSetupGuide.tsx:33; worker/src/index.ts:772
- **Repro:** (static check) Open frontend/src/features/automations/LinkedInSetupGuide.tsx:33 and confirm the behaviour described in the summary; then exercise the matching journey (J-094, J-101) to observe it.
- **Fix hint:** Change the guide text to /auth/linkedin/callback.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Change the guide text to /auth/linkedin/callback.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-021). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/automations/LinkedInSetupGuide.tsx:33.
