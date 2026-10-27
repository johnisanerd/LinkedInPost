---
id: 2026-10-27-lr-006-re-running-setup-without-worker-dev
title: Re-running setup without worker/.dev.vars generates a new SECRET_ENCRYPTION_KEY and pushes it to production, orphaning stored channel tokens.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j007-re-running-setup-py-is-idempotent
- 2026-10-27-j105-stored-token-can-no-longer-be
- 2026-10-27-j132-missing-secret-encryption-key
related: []
docs:
- setup/worker_config.py
- setup/cloudflare.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: setup/cli
raw_id: LR-006
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Re-running setup without worker/.dev.vars generates a new SECRET_ENCRYPTION_KEY and pushes it to production, orphaning stored channel tokens.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002, J-007, J-105, J-132
- **Aliases:** SET-007
- **Evidence:** setup/worker_config.py:115-122; setup/cloudflare.py:635-642
- **Repro:** static. Deploy once; delete `worker/.dev.vars` and unset `SECRET_ENCRYPTION_KEY`; run `python setup.py --deploy-worker`; observe a different key in the secrets file.
- **Fix hint:** Persist generated keys to .env (0600) at creation and refuse to deploy a freshly generated key if the worker already has the secret unless --rotate-keys.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist generated keys to .env (0600) at creation and refuse to deploy a freshly generated key if the worker already has the secret unless --rotate-keys.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-006). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/worker_config.py:115-122.
