# Bootstrap an agent-readable project ledger system

This is the single entry document for an agent adopting the setup template.
Read it alongside the target project's existing agent instructions. Access to
this private repository requires an authenticated account with permission.

## Intended result

One linked development record system: backlog, features, decisions, ideas,
research, reviews, journeys, and document ownership. Each has a template, active items, archives,
and a generated index. Core designs express intent; backlog/features express
work and delivery status; research retains dated evidence and uncertainty.

Do not import setup/moduleCoder/Trade product-specific records, Git history,
secrets, release data, or implementation claims into the destination.

## New project

Create a repository from p1927/setup using GitHub's template action or `gh repo
create OWNER/PROJECT --private --template p1927/setup --clone`. Creating or
pushing a remote repository requires user authorization. If the user requested
only local scaffolding, stop at the local result without publishing anything.
Install `requirements-ledgers.txt`, read AGENTS.md, and validate the empty ledgers.
Keep project-specific existing instructions if any.

## Existing project

1. Inspect its current agent instructions, design sources, work tracking, and Git
   status. Search before filing. If a ledger already exists, extend/reconcile it
   rather than installing a second authoritative record system.
2. Use a dedicated branch in an isolated worktree. Preserve other agents' work;
   no destructive Git commands, stash operations, or automatic pushes.
3. From an authenticated local copy of setup, preview the installer:
   `python3 /path/to/setup/tools/install.py /path/to/project-worktree`.
4. Review conflicts and the proposed agent instruction blocks. Existing project
   rules remain binding. The installer appends marked blocks to AGENTS.md and
   CLAUDE.md, preserves existing content, and refuses other differing files.
   Reconcile substantive policy conflicts before continuing; do not erase rules
   to get a clean installation. Do not modify the source template to match the
   target project.
5. Apply with the same command plus `--apply`; add `--with-ci` if the project
   wants GitHub Actions ledger validation. The installer performs no Git/remote
   operations and copies neither project records nor its own repository README.
6. Install `requirements-ledgers.txt` in the project's chosen environment.
   Run index, check, and ledger-tool tests. Register existing canonical designs
   where they live; moving them into docs/core is unnecessary.
7. Add a backlog item for unresolved documentation/work-tracking migration.
   Preserve old research, decisions, history, and outstanding work with source
   revision/date. Replace migrated live stores with successor pointers; do not
   duplicate them. Never mark imported historical status freshly verified.
8. Review the resulting diff, record actual checks/evidence, commit selected
   session files, and integrate only if concurrent work is preserved. Do not push
   or create a PR without user authorization.

The installation is a bootstrap step. Once the ledger exists, claim project work
before investigation/editing and publish that claim per the protocol.

## Reproduce manually if the installer cannot run

Copy these fixed assets from setup, inspecting collisions first:

- ledgers/README.md and ledgers/PROTOCOL.md.
- Each of backlog, features, decisions, ideas, research, reviews, journeys, documents: TEMPLATE.md,
  empty items/, archive/README.md, and empty archive/. Generate a fresh README
  index for each; do not copy any source items or archival records.
- tools/ledgers/manage.py, tools/ledgers/journeys.py, tools/ledgers/test_manage.py,
  requirements-ledgers.txt.
- docs/core/README.md when the project has no equivalent design-location guide.
- Merge the managed instruction blocks from AGENTS.md and CLAUDE.md into existing
  agent entry points; preserve project instructions and resolve policy conflicts.
- Optionally .github/workflows/ledgers.yml; adapt it to the project's CI without
  creating duplicate checks or replacing unrelated workflows.

Use the checked-in templates and protocol for exact metadata and lifecycle
requirements. Do not invent alternative statuses or another index mechanism.

## First real project records

Capture the user's intent as an idea or feature with provenance. Register the
project's actual authoritative design documents. File known gaps with evidence,
acceptance criteria, and links. Before working an item record owner, exact branch,
worktree, and timezone-aware claim time, publish safely, and check competing
claims. Append attempts and handoff details; close only with real verification.
Record research questions, sources/revisions, findings, limits, and resulting
work. Record accepted decisions with authority; agent guesses remain proposals.

Update the relevant designs, feature acceptance checks, decisions, and work
records together whenever behavior changes. Generate indexes and run structural
checks before committing. The checks do not certify semantic correctness or
perform document updates for the agent.


## Review board

Read ledgers/reviews/README.md for the latest completed overall review and the
latest reviews of individual sections/features, plus drafts and history. After
meaningful work or a requested review, record the actual scope, source revision,
capabilities, conflicts, priorities, and verification limits. A section update
does not refresh the overall review. Link follow-up backlog items instead of
maintaining another task status list in review documents.


## Journey board

Use ledgers/journeys/README.md to navigate user, workflow and information-flow
journeys by section/feature. Record actors, prerequisites, steps, modules/files,
acceptance, failure/recovery and checked revision. Link tickets and evidence via
their journeys field. Resolve all required linked work and rerun full acceptance;
closed tickets alone never establish journey correctness. The validator rejects
verified journeys with unresolved linked backlog work.
