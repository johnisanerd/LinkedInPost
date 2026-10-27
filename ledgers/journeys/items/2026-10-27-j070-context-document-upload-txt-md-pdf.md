---
id: 2026-10-27-j070-context-document-upload-txt-md-pdf
title: J-070 Context document upload (txt, md, pdf)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: None.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P3
core: 'no'
external_service: none
legacy_id: J-070
---

## Purpose and scope

Context document upload (txt, md, pdf). Priority P3, CORE no. Imported from journey J-070 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: None.

## Steps and information flow

1. `ACTION uploadContextDocument {"contentBase64":"<b64>","mimeType":"text/plain","fileName":"n.txt"}`.
2. Repeat with a 3 MB file, an `image/png`, and a PDF with scanned (no text) pages.

## Modules and code map

worker/src/index.ts (`handleUploadContextDocument`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Returns `{documentId,extractedText,charCount}`; over 2 MB -> `File too large (...). Maximum is 2 MB.`; wrong mime -> `Unsupported file type: ... Allowed: txt, md, pdf.` PDF extraction is a naive printable-ASCII scan, so complex PDFs yield junk text (quality, not security). The text is returned to the client; confirm it is not persisted server-side without a retention policy.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
