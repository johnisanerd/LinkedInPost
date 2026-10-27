---
id: 2026-10-27-inv-007-is-the-gmail-push-webhook-unauthenticated
title: Is the Gmail push webhook unauthenticated, and is it P1 or P2? (J-116 vs WKB-031)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-137-gmail-auto-reply-needs-a-kv
docs:
- worker/src/automations/routes.ts
- worker/src/automations/platforms/gmail.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: worker/automations
raw_id: INV-007
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Is the Gmail push webhook unauthenticated, and is it P1 or P2? (J-116 vs WKB-031). An unauthenticated webhook lets anyone trigger auto-replies; a missing KV key means registration always fails, so the feature may not work at all.

## Evidence and reproduction

- **Question:** J-116 is P1; WKB-031 is P2 (LR-137). Does the Gmail push endpoint accept any caller, and does anything write the oauth:gmail:<address> KV key it needs?
- **Why it matters:** An unauthenticated webhook lets anyone trigger auto-replies; a missing KV key means registration always fails, so the feature may not work at all.
- **How to settle it:** Read worker/src/automations/routes.ts:55-58,253-263 and worker/src/automations/platforms/gmail.ts:38-116; `grep -rn "oauth:gmail" worker/src`. To settle: POST a forged Pub/Sub body to the push endpoint on a test Worker without any token.
- **Related items:** LR-137, J-116, WKB-031
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-007). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: not re-read in this pass beyond the ledger entry; raw WKB-031 evidence says the key is never written. Ledger follows WKB-031 severity (LR-137, P2)..
