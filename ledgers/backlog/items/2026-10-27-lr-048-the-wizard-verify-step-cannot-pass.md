---
id: 2026-10-27-lr-048-the-wizard-verify-step-cannot-pass
title: 'The wizard verify step cannot pass: the worker URL depends on CLOUDFLARE_SUBDOMAIN which nothing sets, and it reads stale environment values.'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
- 2026-10-27-j008-verify-step-and-worker-health-probes
- 2026-10-27-j145-operator-health-check-of-both-workers
related: []
docs:
- setup/wizard/steps/verify.py
- setup/verification.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/wizard
raw_id: LR-048
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The wizard verify step cannot pass: the worker URL depends on CLOUDFLARE_SUBDOMAIN which nothing sets, and it reads stale environment values.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001, J-008, J-145
- **Aliases:** SET-015, SET-016
- **Evidence:** setup/wizard/steps/verify.py:15-32,20-24,46-47,56-58
- **Repro:** static. Finish deploy, open `/step/verify`.
- **Fix hint:** Persist VITE_WORKER_URL from the deploy output, re-read .env via dotenv_values, parse wrangler.jsonc with json5, probe the endpoint setup/verification.py uses.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist VITE_WORKER_URL from the deploy output, re-read .env via dotenv_values, parse wrangler.jsonc with json5, probe the endpoint setup/verification.py uses.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-048). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/wizard/steps/verify.py:15-32,20-24,46-47,56-58.
