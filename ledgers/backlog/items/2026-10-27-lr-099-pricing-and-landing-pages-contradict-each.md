---
id: 2026-10-27-lr-099-pricing-and-landing-pages-contradict-each
title: Pricing and landing pages contradict each other and promise a no-card trial, SLA and analytics that have no backing flow
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j016-saas-landing-page-and-redirect-for
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/saas
raw_id: LR-099
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Pricing and landing pages contradict each other and promise a no-card trial, SLA and analytics that have no backing flow.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-016
- **Aliases:** FEB-021
- **Evidence:** frontend/src/pages/PricingPage.tsx:50-160; frontend/src/features/saas/Landing.tsx:277-315
- **Repro:** compare the two pages. Static reasoning.
- **Fix hint:** Use a single source of plan data and remove or mark coming-soon claims with no backing.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use a single source of plan data and remove or mark coming-soon claims with no backing.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-099). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/pages/PricingPage.tsx:50-160.
