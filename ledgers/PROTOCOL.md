# Ledger and documentation protocol

## Authority and record boundaries

Direct user instructions govern the task. `AGENTS.md` governs the agent workflow.
This protocol defines development record lifecycle. The document ledger maps a
scope to its authoritative design; it does not create another copy of the design.

- Design documents state intended behavior and boundaries, not delivery status.
- Feature records state capabilities/journeys and observable acceptance checks.
- Backlog records state work needed to close a gap, including investigation.
- Decisions record who settled a choice, why, and what it replaces. An idea,
  research recommendation, or agent inference is not automatically an accepted
  product decision. Record the authority explicitly.
- Research records evidence and uncertainty, including negative results.
- Reviews capture scoped application state, architectural conflicts, and direction
  at a named revision; they do not replace design or backlog ownership.
- Ideas are possibilities, not assignments or implementation commitments.
- Historical docs, generated mirrors, and archived items never override current
  authoritative sources. Contradictions require a backlog item; do not silently
  pick whichever doc supports an implementation.

## Filing and identity

1. Search all eight ledgers, including archives, before filing. Use `rg` with the
   symptom, affected path, feature, or related IDs. Extend an existing item;
   reopen a recurring closed issue so previous attempts remain attached.
2. Use a globally unique `YYYY-MM-DD-short-slug` ID and matching filename. The
   date is the creation/import date, not an invented original date. Use distinct
   slugs across ledgers. Add a suffix only on a real collision; no shared counter.
3. Copy the ledger template into `items/`. Fill title, status, dates, related IDs,
   repository-relative document paths, and the relevant body fields. Preserve
   provenance when importing older material. Use the client's date/timezone;
   claim timestamps include time and offset.
4. File concrete inefficiencies, boundary bypasses, suspicious behavior, and
   pre-existing failures immediately, even outside scope. Record the exact call
   path, reproduction/profile, measured versus suspected impact, and why it is
   deferred. An unconfirmed concern is an investigation, not a claimed defect.
5. Keep implementation plans in the backlog item's Plan section. Append dated
   revisions and attempts; link substantial existing plans instead of copying
   them. Never create another numbered plan merely to track status.

## Status vocabulary

| Ledger | Allowed states |
| --- | --- |
| Backlog | `open`, `in-progress`, `blocked`, `closed` |
| Features | `proposed`, `planned`, `in-progress`, `implemented`, `verified`, `retired` |
| Decisions | `accepted`, `superseded` |
| Ideas | `captured`, `exploring`, `parked`, `promoted`, `rejected` |
| Research | `planned`, `in-progress`, `complete`, `superseded` |
| Journeys | `planned`, `partial`, `verified`, `failing`, `blocked`, `retired` |
| Reviews | `draft`, `complete`, `superseded` |
| Documents | `current`, `review-needed`, `superseded`, `historical` |

`blocked` means identified actionable work with a blocker and an owner;
`parked` ideas have no current execution commitment. `implemented` is not
`verified`. Completion requires actual checks against the named source revision.

## Claim before investigation or editing

A filing/reconnaissance pass may identify a gap. Before working that item:

1. Read its evidence, related items, and Attempts. Inspect the authoritative
   integration branch and outstanding claims. Do not duplicate an active claim.
2. Work in an isolated worktree and dedicated branch. Set the item to
   `in-progress`; fill `owner` (agent/session identity), `branch` (exact Git
   branch), `worktree`, and `claimed_at` (ISO timestamp with timezone). Append
   a dated claim entry to Attempts. Keep identity separate from branch name.
3. Commit the claim and make it visible on the agreed integration branch using
   a normal merge that preserves concurrent changes, before dependent work.
   This is a local workflow; pushing is permitted only when the user requested
   it. For remote collaboration, use the explicitly agreed shared claim channel.
4. Re-read the published claim before starting. Conflicting claims are a conflict
   to resolve, not permission to overwrite another agent. If the claim cannot be
   published safely, retain the branch and report the blocker; do independent
   work only. Item metadata alone is not a distributed locking mechanism.
5. Do not steal a claim just because it is old. Check the owner's branch/session
   and handoff evidence. A takeover must record the prior owner, attempts, reason,
   and the new branch. Never remove another agent's working changes.

The checker validates claim fields; it cannot prove live ownership, prevent
concurrent work, or publish a claim. Agents must perform the steps above.

## While working and handing off

- Append dated Attempts for investigations and failed/successful approaches,
  naming evidence, commands, revision, outcomes, and remaining uncertainty.
- Preserve each item's branch and worktree across nonterminal attempts.
- A blocker sets `blocked`, keeps ownership, records `blocked_reason` and the
  concrete action needed. Waiting for someone else is not successful completion.
- For handoff, record exact branch/commit, working tree state, checks run, next
  step, and relevant IDs in the item's Attempts. Avoid a second status ledger.
- Research includes source paths/URLs and source revision/date, method, findings,
  limits, and recommendations. Link any resulting idea, decision, or backlog item.
  Research does not itself authorize implementation or sending messages.

## Implementing features and maintaining documents

Every feature/behavior change updates, in the same coherent change:

1. The owning design/reference documents identified through the document ledger.
2. The feature's acceptance checks/journeys and evidence; its linked backlog item.
3. Any changed interfaces, configuration, usage examples, and relevant tests.
4. A decision record if a material design choice was actually settled; cite its
   authority. Update the design deliberately rather than silently contradicting it.
5. Document registry `updated`/`reviewed_revision`/`related` fields and indexes.

Use `docs` in the backlog/feature record to name affected files. If a document
needs no change, state why in Verification. For an implementation contradiction,
file a gap; do not edit the intended design merely to describe a defect as correct.
One scope has one canonical design. Link to it from other docs; do not copy it.
Core design should remain short enough to read as a whole. Dated audit results
belong in research records, not embedded as a second live design/status section.

## Promotion, decisions, and closure

- Promote an idea by creating/linking research, a feature, or actionable backlog
  work; set `promoted_to` to those IDs and retain the original reasoning.
- Completed research names a source revision, sources, findings, limits, and
  follow-up records (or explains why none). Preserve uncertainty and failed tests.
- Superseded decisions/documents point to their replacements. A new accepted
  decision names its authority and links the old one; never silently rewrite the
  old rationale. Git history preserves edits, but current readers need the pointer.
- Close a backlog item only with a dated Attempts entry, nonempty Verification,
  resolution, and relevant commit/check evidence. Fixed work names checks run,
  results, and document changes; unverified or blocked work remains open.
- Valid non-fix closures: `duplicate`, `superseded`, `not-reproduced`, `declined`,
  or `historical-import`, each with evidence/reason. Historical imports preserve
  prior closure claims and explicitly do not assert present-day verification.
- Move closed backlog items to `archive/` retaining the ID; regenerate indexes.
  Reopening moves the same file back to `items/`, records why, clears closure
  metadata, and keeps Attempts. Other ledgers may archive terminal records;
  retired/superseded records retain their replacement links.

## Journeys and linked work

Use `journeys/` for user, workflow, and information-flow contracts, organized by
whole application, section, or feature. Each record explains actor/trigger,
prerequisites, steps/handoffs, modules and source paths, success/acceptance,
failure/recovery, verification evidence, gaps and next actions.

- `scope_type` is overall/application, section/<stable area>, or feature/<existing
  feature record ID>. `journey_type` is user, workflow, or information-flow.
- States: planned, partial, verified, failing, blocked, retired. Verified is a claim
  at `source_revision` and timezone-aware `checked_at`, owned by verification_owner.
  Retain dated evidence/attempts; a code change may invalidate old verification.
- Backlog tickets and other affected records link through `journeys: [journey-id]`.
  This is the authoritative work-to-journey link; the generated board derives the
  linked work/status and unresolved-ticket counts. Do not maintain a second
  manual ticket/status list in the journey. Use related for supporting evidence.
- Before fixing a journey, search all active/archive records linked to it, discover
  missing required work, and inspect the full dependency/handoff chain. Claim the
  work per protocol; respect other active owners and coordinate through the
  existing channel. Do not silently take over another agent's tickets.
- Resolve all linked backlog work required for acceptance, not just the first
  symptom. Keep the journey partial/blocked/failing while any linked ticket is
  unresolved. The checker rejects verified with open/in-progress/blocked tickets,
  including a ticket reopened after an earlier verification.
- Update linked features, research, reviews and design evidence at the scope
  actually verified. A narrower journey passing does not verify its entire feature.
  Related non-ticket work must be assessed against acceptance too; document any
  justified exclusion. Do not close irrelevant work to force a green board.
- Closed tickets, duplicate/superseded/declined resolutions, test discovery and
  agent self-claims are not end-to-end evidence. Re-run complete acceptance,
  including failure/recovery, before marking verified. Non-fix closures must not
  hide a remaining blocker or an unresolved successor ticket.
- Scope-to-file maps include real files or directories. Missing implementation
  paths are described as gaps, not invented existing files. The checker validates
  declared paths and references but cannot prove complete coverage or test truth.
- Runtime task IDs may be cited as evidence; these development records do not
  replace product runtime tickets, scheduling, state transitions, or verification.

## Reviews and application direction

Use `reviews/` for dated overall, section, or feature snapshots. After a requested
review or meaningful work, append a review for the scope actually examined.
Before starting work, read the latest completed review of the relevant scope and
check its revision; old evidence is context, not proof of today's state.

- `scope_type: overall` uses `scope: application`; section uses a stable area name;
  feature uses the existing feature record ID. An overall report can contain
  subsections linking scoped reviews without pretending every section was retested.
- Records move `draft` → `complete`; `superseded` retains prior evidence. A completed
  review names `reviewer`, timezone-aware `reviewed_at`, and `source_revision`.
  Link `previous_review` to an older completed/superseded record of the same scope.
- State what exists, verified/partial/missing behavior, changes since the prior
  review, major conflicts/architectural issues, priorities, follow-up IDs, checks,
  sources, and exclusions. Completing the review does not certify the application.
- File actionable findings in the backlog and link them through `related`; the
  backlog owns claims and task status. Use research for supporting investigations
  and decisions for accepted choices. Recommendations do not silently change design.
- Preserve completed review bodies as snapshots; substantive new evidence belongs
  in a new linked review. Correct factual/clerical errors with a dated correction.
  Do not rewrite prior findings to make the current implementation look consistent.
- The generated board selects completed, active records by actual review time for
  each exact scope. Drafts and superseded/archived records do not displace it. Keep
  the latest completed review active; archive superseded snapshots with IDs intact.
  A section/feature update never refreshes an overall review's date or coverage.

## Checks and upkeep

Run `python3 tools/ledgers/manage.py index` then `check` before committing.
The check covers metadata, claim shape, status/location, declared relationships,
document paths, required record sections, and generated indexes. It does not
certify semantic correctness, working software, or complete document inventory.
Run behavior tests appropriate to code changes. Do not hide existing failures;
file or link them with reproduction evidence. Keep tests proportional to risk.

At handoff or when changing an area, review its linked records for stale status,
missing ownership, broken links, and duplicate authoritative documents. Preserve
history; archive superseded material with successor pointers. Scheduling periodic
upkeep requires an explicit user request.
