---
id: 2026-10-27-lr-059-gmail-to-cc-bcc-and-subject
title: Gmail To, Cc, Bcc and Subject from the client go unsanitised into raw MIME headers (header injection) and are sent from the shared mailbox.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j078-send-via-gmail
- 2026-10-27-j103-a-user-with-no-linkedin-connection
related: []
docs:
- worker/src/integrations/gmail/index.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/integrations
raw_id: LR-059
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Gmail To, Cc, Bcc and Subject from the client go unsanitised into raw MIME headers (header injection) and are sent from the shared mailbox.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-078, J-103
- **Aliases:** WKB-008
- **Evidence:** worker/src/integrations/gmail/index.ts:133-137; worker/src/index.ts:5104-5110
- **Repro:** static. Executor: publish via gmail with `emailSubject:"hi\r\nBcc: you@x"`; inspect the sent message headers.
- **Fix hint:** Reject CR/LF in header values, validate addresses, RFC 2047-encode the subject, cap recipient count.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Reject CR/LF in header values, validate addresses, RFC 2047-encode the subject, cap recipient count.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-059). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/integrations/gmail/index.ts:133-137.
