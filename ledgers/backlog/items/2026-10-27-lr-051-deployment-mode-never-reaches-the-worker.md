---
id: 2026-10-27-lr-051-deployment-mode-never-reaches-the-worker
title: DEPLOYMENT_MODE never reaches the worker, so a selfHosted deploy runs with SaaS token budgets and can block generation
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j006-wizard-mode-step-and-deploymentmode-propagation
- 2026-10-27-j126-self-hosted-deployment-still-enforces-the
related: []
docs:
- worker/src/index.ts
- worker/src/auth.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/config
raw_id: LR-051
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

DEPLOYMENT_MODE never reaches the worker, so a selfHosted deploy runs with SaaS token budgets and can block generation.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-006, J-126
- **Aliases:** ARCH-007, SET-034
- **Evidence:** worker/src/index.ts:1004,1574,1586,2532; worker/src/auth.ts:34-37
- **Repro:** static; check how worker/src reads deployment mode.
- **Fix hint:** Use the generated deploymentMode constant in the worker, or have setup write DEPLOYMENT_MODE into wrangler vars; delete the no-op regex in generate_features.py.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use the generated deploymentMode constant in the worker, or have setup write DEPLOYMENT_MODE into wrangler vars; delete the no-op regex in generate_features.py.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-051). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:1004,1574,1586,2532.
