---
id: 2026-10-27-lr-187-getnodecatalog-returns-a-response-object-inside
title: getNodeCatalog returns a Response object inside the JSON envelope, so the node list arrives empty
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j113-enrichment-page-and-node-catalog-admin
related: []
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
raw_id: LR-187
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

getNodeCatalog returns a Response object inside the JSON envelope, so the node list arrives empty. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-113
- **Aliases:** WKA-036
- **Evidence:** worker/src/index.ts:1875-1877
- **Repro:** static. Executor: call `getNodeCatalog` and inspect `data`.
- **Fix hint:** Return the plain object { nodes: [...] }.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return the plain object { nodes: [...] }.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-187). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of worker/src/index.ts:1875-1877; confirm by running the Repro and observing the described behaviour.
