---
id: 2026-10-27-inv-018-does-the-wizard-s-deployment-mode
title: Does the wizard's DEPLOYMENT_MODE setting reach the deployed Worker? (SET-034)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-051-deployment-mode-never-reaches-the-worker
docs:
- setup/wizard/steps/mode.py
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: setup/config
raw_id: INV-018
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does the wizard's DEPLOYMENT_MODE setting reach the deployed Worker? (SET-034). If it never reaches the Worker, selfHosted installs run with SaaS token budgets and can block generation.

## Evidence and reproduction

- **Question:** The wizard regex-replaces DEPLOYMENT_MODE in worker/wrangler.jsonc, but the key is absent from the tracked vars. Does the worker read it from env or from generated features.ts?
- **Why it matters:** If it never reaches the Worker, selfHosted installs run with SaaS token budgets and can block generation.
- **How to settle it:** Read setup/wizard/steps/mode.py and `grep -n DEPLOYMENT_MODE worker/wrangler.jsonc worker/src/index.ts`. To settle: choose selfHosted in the wizard, deploy to a test account, and call a generation action.
- **Related items:** LR-051
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-018). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code: worker/src/index.ts:192 types DEPLOYMENT_MODE and lines 1004,1574,1586,2532 default it to 'saas'; wrangler.jsonc has no DEPLOYMENT_MODE hit in the grep. Wizard write path not re-read. Covered by LR-051..
