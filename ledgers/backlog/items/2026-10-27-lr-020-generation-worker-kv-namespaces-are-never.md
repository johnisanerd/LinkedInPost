---
id: 2026-10-27-lr-020-generation-worker-kv-namespaces-are-never
title: Generation worker KV namespaces are never provisioned and the committed ids belong to the owner, so deploy fails on any other account.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j002-headless-full-bootstrap-with-python-setup
- 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
- 2026-10-27-j004-generation-worker-deploy-requires-an-llm
related: []
docs:
- setup/cloudflare.py
- setup.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: deploy/config
raw_id: LR-020
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Generation worker KV namespaces are never provisioned and the committed ids belong to the owner, so deploy fails on any other account.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-002..J-004
- **Aliases:** SET-012
- **Evidence:** generation-worker/wrangler.jsonc:14-21; setup/cloudflare.py:386-438
- **Repro:** static. Fresh account, `python setup.py --all`, watch `deploy_generation_worker`.
- **Fix hint:** Create and patch both KV namespaces in provision_generation_worker_d1 and use placeholders in the tracked config.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Create and patch both KV namespaces in provision_generation_worker_d1 and use placeholders in the tracked config.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-020). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/wrangler.jsonc:14-21.
