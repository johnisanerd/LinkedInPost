---
id: 2026-10-27-inv-014-does-getnodecatalog-return-an-empty-node
title: Does getNodeCatalog return an empty node list to the Enrichment page? (WKA-036)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-187-getnodecatalog-returns-a-response-object-inside
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: worker/api
raw_id: INV-014
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does getNodeCatalog return an empty node list to the Enrichment page? (WKA-036). The Enrichment node list would arrive empty.

## Evidence and reproduction

- **Question:** The case returns Response.json({nodes}); the caller wraps it as {ok:true,data:<Response>}. Does the dispatcher unwrap a Response or serialise it as {}?
- **Why it matters:** The Enrichment node list would arrive empty.
- **How to settle it:** Read the action dispatcher in worker/src/index.ts around the getNodeCatalog case (line 1875) and its caller. To settle: call ACTION getNodeCatalog on a local worker and inspect data.
- **Related items:** LR-187
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-014). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code returns Response.json at worker/src/index.ts:1875-1877; the dispatcher's handling of Response was not traced. Covered by LR-187..
