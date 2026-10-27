---
id: 2026-10-27-lr-076-the-deploy-workflow-applies-d1-migrations
title: The deploy workflow applies D1 migrations on every push with cancel-in-progress, uses an unpinned third-party action, and deploys in the wrong order.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j145-operator-health-check-of-both-workers
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
area: deploy/ci
raw_id: LR-076
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The deploy workflow applies D1 migrations on every push with cancel-in-progress, uses an unpinned third-party action, and deploys in the wrong order.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002, J-145
- **Aliases:** ARCH-019, SET-030
- **Evidence:** .github/workflows/deploy-workers.yml:12-14,38-52,74-88; worker/package.json:7
- **Repro:** static; push two commits touching worker/ in quick succession.
- **Fix hint:** Pin the action to a SHA, cancel-in-progress false, deploy the generation worker first, add Python/PyYAML and permissions: contents: read.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Pin the action to a SHA, cancel-in-progress false, deploy the generation worker first, add Python/PyYAML and permissions: contents: read.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-076). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of .github/workflows/deploy-workers.yml:12-14,38-52,74-88.
