---
id: 2026-10-27-lr-045-re-running-cloudflare-rewrites-wrangler-vars
title: Re-running --cloudflare rewrites wrangler vars from env only, so a blank allow-list reopens sign-up and migrations or bindings are dropped.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
- 2026-10-27-j007-re-running-setup-py-is-idempotent
- 2026-10-27-j015-approved-user-signs-in-self-hosted
related: []
docs:
- setup/worker_config.py
- setup/github.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: setup/cli
raw_id: LR-045
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Re-running --cloudflare rewrites wrangler vars from env only, so a blank allow-list reopens sign-up and migrations or bindings are dropped.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-003, J-007, J-015
- **Aliases:** SET-018
- **Evidence:** setup/worker_config.py:144-207; setup/github.py:50-51
- **Repro:** static. Hand-edit `ALLOWED_EMAILS` in wrangler.jsonc, then `python setup.py --cloudflare` with an empty env.
- **Fix hint:** Overwrite a var only when the new value is non-empty, keep unknown keys and migrations, refuse empty ALLOWED_EMAILS in selfHosted mode.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Overwrite a var only when the new value is non-empty, keep unknown keys and migrations, refuse empty ALLOWED_EMAILS in selfHosted mode.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-045). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of setup/worker_config.py:144-207.
