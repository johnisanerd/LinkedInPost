---
id: 2026-10-27-j111-scheduled-newsletter-send-vs-a-once
title: J-111 Scheduled newsletter send vs a once-a-day cron
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Background / agent actor
trigger: Newsletter with `scheduleTimes` such as `["09:00"]` and an approved issue.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/newsletter/scheduler.ts
- worker/src/newsletter/handlers.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'no'
external_service: Cloudflare, Gmail
legacy_id: J-111
---

## Purpose and scope

Scheduled newsletter send vs a once-a-day cron. Priority P1, CORE no. Imported from journey J-111 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Background / agent actor. Preconditions: Newsletter with `scheduleTimes` such as `["09:00"]` and an approved issue.

## Steps and information flow

1. Read `worker/wrangler.jsonc` `triggers.crons`: only `"0 3 * * *"`.
2. `scheduled()` calls `runNewsletterScheduler`; `processNewsletter` sends only when `now >= next_send_at && now - next_send_at < 2h`, and creates the draft only in the 24 h preview window.
3. Wait for the send time.

## Modules and code map

worker/wrangler.jsonc, worker/src/index.ts (`scheduled`), worker/src/newsletter/scheduler.ts, worker/src/newsletter/handlers.ts

Code anchors that exist: worker/src/index.ts, worker/src/newsletter/scheduler.ts, worker/src/newsletter/handlers.ts

## Success and acceptance

Issue is sent within minutes of its scheduled time. CODE-READING FINDING: with one run per day at 03:00 UTC, a newsletter due at any time other than 03:00-05:00 UTC is never sent (window missed, `next_send_at` not advanced). Also the legacy path says "delivery for legacy mode is handled by the Python pipeline" (`newsletter_id` null) which this repo does not contain (grep `scheduler/` only has `__init__.py`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
