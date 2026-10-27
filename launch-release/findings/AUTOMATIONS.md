# Automations review

Read-only. automations/ holds two files: `__init__.py` (empty) and `youtube_poller.py` (265 lines). No secrets or tokens are hard-coded; credentials come from environment variables. The only caller found is `.github/workflows/youtube-comment-poll.yml` (manual `workflow_dispatch`; the cron is commented out), plus tests in `tests/automations/test_youtube_poller.py`. The worker routes the script calls (`/automations/internal/rules/lookup`, `/automations/internal/youtube/poll`) exist in `worker/src/automations/routes.ts` and are guarded by `verifySchedulerSecret` (worker/src/index.ts:1298), which rejects an empty secret. Nothing in the script deletes data.

### AUT-001 P1 automations - YouTube poller loses its "already replied" list on every CI run, so each run re-replies to every comment
- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** automations/youtube_poller.py:19 stores replied IDs in `.youtube_replied_ids` in the working directory (load_replied line 140, save_replied line 152). .github/workflows/youtube-comment-poll.yml:17-31 checks out a fresh clone, runs the script, and has no cache or artifact step for that file, so the list is empty at the start of every run. The worker records only a poll timestamp (routes.ts:208), not reply IDs.
- **Repro:** Run the workflow twice against a channel with a comment rule: the second run posts a second reply under every top-level comment the first run answered.
- **Fix hint:** Persist the replied IDs between runs (actions/cache or a KV/D1 record through the worker) and skip any thread that already has a reply from the channel owner.

### AUT-002 P1 automations - First run auto-replies to every historic comment on every video, with no recency limit or dry run
- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** The docstring says "recent comments" (youtube_poller.py:3), but main() pages `search` over all channel videos (lines 183-211) and `commentThreads` over all pages of each video (lines 225-252) and calls post_reply for each thread not in the replied set (lines 237-244). There is no date cutoff, no per-run cap, no skip for the owner's own comments, and no confirm or dry-run switch.
- **Repro:** Enable a comment rule with a template, run the workflow on a channel with a few hundred old comments: every one gets the template reply in one run.
- **Fix hint:** Add a publishedAfter cutoff (for example the last recorded poll time), a per-run reply cap, skip comments authored by the channel itself, and a `DRY_RUN=1` mode that only prints what it would send.

### AUT-003 P2 automations - An expired OAuth token marks the whole backlog as replied, so those comments are never answered
- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** youtube_poller.py:110-112 returns True for HTTP 401 ("treat as permanent"). main() then adds the thread to `new_replied` (lines 245-248), saves the list (line 254) and records a successful poll (line 256). YOUTUBE_OAUTH_TOKEN is a single access token in a GitHub secret (workflow line 28), and Google access tokens last about an hour, so a stale token is the normal case.
- **Repro:** Run with an expired YOUTUBE_OAUTH_TOKEN: the log shows "reply auth failed (401)" for each comment, the run reports "done — replied to N comments", and after refreshing the token a rerun skips all of them.
- **Fix hint:** Return False (not replied) on 401 and abort the run on the first 401; document or implement token refresh from a refresh token.

### AUT-004 P2 automations - The YouTube poll schedule saved in the UI is never used; the workflow has no schedule and does not read it
- **Journeys:** none
- **Confidence:** confirmed-by-reading
- **Evidence:** The Automations page shows a cron field (frontend/src/features/automations/YouTubeScheduler.tsx:50, saved by PUT /automations/youtube/schedule in worker/src/automations/routes.ts:142-149 into KV) and the text "YouTube uses scheduled polling — no webhook registration needed." (frontend/src/features/automations, rendered for the youtube tab). .github/workflows/youtube-comment-poll.yml:9-11 has `# schedule:` and the cron commented out, "Disabled by default"; the only trigger is manual `workflow_dispatch` with a required channel_id. The workflow also reads the worker URL from `secrets.VITE_WORKER_URL` (line 29), a frontend variable name that setup does not document for this job, and the script's WORKER_SCHEDULER_SECRET is described as optional by main() (line 169 does not require it) although the worker rejects an empty one.
- **Repro:** Save a YouTube comment rule and a cron such as `0 */6 * * *` in /automations, wait: no replies are ever posted unless someone triggers the workflow by hand; with the secret unset the script prints "no active comment rule" (a 401 from the worker, swallowed at lines 55-57).
- **Fix hint:** Either have the workflow (or a worker cron) read the saved cron, or change the UI text to say the cron must be set in the workflow file; require WORKER_SCHEDULER_SECRET in main(), and print the HTTP status when the rule lookup fails.

### AUT-005 P3 automations - Poller spends YouTube quota on every run (search.list per page plus a comment fetch per video)
- **Journeys:** none
- **Confidence:** hypothesis
- **Evidence:** youtube_poller.py:183-211 pages search.list (100 quota units per call) over all videos and lines 217-252 call commentThreads for every video on every run, plus comments.insert (about 50 units) per reply. With the default 10,000 units per day, a six-hourly schedule on a large channel can exhaust quota, after which 403 responses are retried forever (lines 101-108).
- **Repro:** Static check only: count the calls per run for a channel with more than 100 videos; not run against the YouTube API.
- **Fix hint:** Use the channel's uploads playlist (playlistItems.list, 1 unit) and stop paging once videos older than the last poll are reached.
