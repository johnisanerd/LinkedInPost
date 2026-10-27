---
id: 2026-10-27-inv-005-is-an-unset-worker-shared-secret
title: Is an unset WORKER_SHARED_SECRET on the generation worker P0 or P1? (J-060 vs ARCH-003)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-050-the-generation-worker-accepts-requests-when
docs:
- generation-worker/src/index.ts
- setup/worker_config.py
- setup/cloudflare.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P0
area: generation-worker/auth
raw_id: INV-005
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Is an unset WORKER_SHARED_SECRET on the generation worker P0 or P1? (J-060 vs ARCH-003). A manually deployed generation worker without the secret lets anyone run the LLM pipeline on the operator's keys. The setup path generates the secret, so the exposure depends on how people deploy.

## Evidence and reproduction

- **Question:** J-060 is P0 (CORE) in the journeys; ARCH-003 and GWP-003 rate the same defect P1 (LR-050). Which severity?
- **Why it matters:** A manually deployed generation worker without the secret lets anyone run the LLM pipeline on the operator's keys. The setup path generates the secret, so the exposure depends on how people deploy.
- **How to settle it:** Read generation-worker/src/index.ts:41-45 (checkAuth) and setup/worker_config.py + setup/cloudflare.py to see whether every supported deploy path sets the secret. To settle: `curl -X POST <gen-worker>/v1/generate` against a test deploy with the secret unset (expect 401 after the fix).
- **Related items:** LR-050, J-060, ARCH-003, GWP-003
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-005). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code confirms checkAuth returns true when WORKER_SHARED_SECRET is empty (generation-worker/src/index.ts:41-45). Whether any supported deploy path leaves it empty was not traced. Ledger uses P1 (LR-050); the owner decides..
