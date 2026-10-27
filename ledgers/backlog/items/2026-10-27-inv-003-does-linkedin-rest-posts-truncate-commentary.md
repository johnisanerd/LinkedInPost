---
id: 2026-10-27-inv-003-does-linkedin-rest-posts-truncate-commentary
title: Does LinkedIn rest/posts truncate commentary at unescaped reserved characters? (WKB-022)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-152-linkedin-commentary-is-sent-raw-to
docs:
- worker/src/integrations/linkedin/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: worker/integrations
raw_id: INV-003
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does LinkedIn rest/posts truncate commentary at unescaped reserved characters? (WKB-022). LLM drafts routinely contain parentheses and hashtags, so multi-image LinkedIn posts could publish cut off at the first reserved character.

## Evidence and reproduction

- **Question:** The multi-image path sends commentary: request.text raw to /rest/posts. Does LinkedIn parse commentary as little text format so that characters such as ( ) [ ] @ # truncate the visible post?
- **Why it matters:** LLM drafts routinely contain parentheses and hashtags, so multi-image LinkedIn posts could publish cut off at the first reserved character.
- **How to settle it:** Read the LinkedIn Posts API 'little text' documentation, then on a test LinkedIn account publish a 2-image post with the text 'Results (up 40%) #growth' through worker/src/integrations/linkedin/index.ts and compare with the rendered post.
- **Related items:** LR-152, WKB-022
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code sends commentary: request.text unescaped at worker/src/integrations/linkedin/index.ts:60-63. LinkedIn API behaviour was not checked here. Covered by LR-152..
