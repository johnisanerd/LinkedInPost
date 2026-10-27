---
id: 2026-10-27-lr-140-env-secrets-and-legacy-plaintext-tokens
title: Env secrets and legacy plaintext tokens are copied into the KV shared config in clear by every persist and disconnect path.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j132-missing-secret-encryption-key
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/config
raw_id: LR-140
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Env secrets and legacy plaintext tokens are copied into the KV shared config in clear by every persist and disconnect path.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-132, J-140
- **Aliases:** WKA-016
- **Evidence:** worker/src/index.ts:3148-3170,4212-4337
- **Repro:** static. Executor: set `TELEGRAM_BOT_TOKEN` in env, connect LinkedIn, `wrangler kv key get shared-config` and look for the token.
- **Fix hint:** Persist only fields that came from KV (read raw, modify, write), never the env-merged view.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist only fields that came from KV (read raw, modify, write), never the env-merged view.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-140). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:3148-3170,4212-4337.
