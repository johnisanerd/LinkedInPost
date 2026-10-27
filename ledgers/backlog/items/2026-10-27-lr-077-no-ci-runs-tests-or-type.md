---
id: 2026-10-27-lr-077-no-ci-runs-tests-or-type
title: No CI runs tests or type checks on pull requests and the Pages build proceeds with unset repo secrets
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j013-documented-developer-test-commands-exist
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
raw_id: LR-077
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

No CI runs tests or type checks on pull requests and the Pages build proceeds with unset repo secrets.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002, J-013
- **Aliases:** SET-031
- **Evidence:** .github/workflows/deploy-workers.yml; .github/workflows/deploy-pages.yml
- **Repro:** static.
- **Fix hint:** Add a pull_request workflow running tsc for all three packages, npm run test and pytest setup/wizard/tests; fail Pages when secrets are empty.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a pull_request workflow running tsc for all three packages, npm run test and pytest setup/wizard/tests; fail Pages when secrets are empty.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-077). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of .github/workflows/deploy-workers.yml.
