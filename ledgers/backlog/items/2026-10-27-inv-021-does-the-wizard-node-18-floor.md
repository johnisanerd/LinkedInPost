---
id: 2026-10-27-inv-021-does-the-wizard-node-18-floor
title: Does the wizard Node 18 floor accept a Node version that the pinned wrangler 4 cannot run on?
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
related: []
docs:
- setup.md
- setup/wizard/steps/prereqs.py
- SETUP.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: setup/wizard
raw_id: INV-021
source_file: docs/launch-readiness/findings/SWEEP.md
---

## Problem

Does the wizard Node 18 floor accept a Node version that the pinned wrangler 4 cannot run on?. If wrangler 4.92 needs Node 20 or newer, a user on Node 18 passes the prerequisite step and then fails at deploy. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/setup.md SET-033 (setup.md:333, "Node 18 is below what wrangler 4 / CI (Node 24) assume (hypothesis)")
- **Journeys:** J-001, J-002
- **Confidence:** hypothesis
- **Evidence:** setup/wizard/steps/prereqs.py:22-29 (Node 18+); .github/workflows/deploy-workers.yml:26,63 and deploy-pages.yml:33 (Node 24); worker/package.json wrangler ^4.92.0
- **Why it matters:** If wrangler 4.92 needs Node 20 or newer, a user on Node 18 passes the prerequisite step and then fails at deploy.
- **Repro or check:** `npm view wrangler@^4.92.0 engines.node` and `npm view wrangler@^4.78.0 engines.node`; compare with the floor in prereqs.py:22-29.
- **Fix hint:** decide: raise the floor in prereqs.py (and SETUP.md) to the engines value, or confirm 18 is enough and drop the question.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

decide: raise the floor in prereqs.py (and SETUP.md) to the engines value, or confirm 18 is enough and drop the question.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/SWEEP.md (INV-021). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: setup/wizard/steps/prereqs.py:22-29; .github/workflows/deploy-workers.yml:26.
