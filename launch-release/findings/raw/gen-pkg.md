# Raw findings: generation-worker + packages (GWP)

Summary: 26 findings. P0: 3, P1: 8, P2: 12, P3: 3.
Method: static read only (no tests, builds, or network). References ARCH-003 (gen-worker empty secret) rather than repeating it.
Scope read: generation-worker/src/{index,pipeline,preview,types,llmFromWorker}.ts, players/*, modules/_shared/*, image-gen/modules (providers), migrations/*, wrangler.jsonc; packages/llm-core/src/*, packages/researcher/src/*; plus worker/src/llm/* and worker/src/generation/generationWorkerClient.ts and worker/src/index.ts:850-1000 where they form the boundary.

### GWP-001 Main worker spreads the client payload AFTER spreadsheetId, so the client controls spreadsheetId, newsResearchConfig, imageGen, contextDocuments and llm in /api/generate/stream
- **Sev:** P0
- **Area:** worker/src/index.ts (boundary), generation-worker/src/types.ts
- **Journeys:** all generate journeys (SSE path), tenant-isolation journeys
- **Evidence:** worker/src/index.ts:877-882 builds `{ spreadsheetId: storedConfig.spreadsheetId, ...payload, ...(storedConfig.imageGen...) }`. `payload` is `await request.json()` (line 857) with no schema, and it is spread after spreadsheetId, so a caller can overwrite the server-resolved tenant id. The gen worker trusts it and writes it to `generation_runs.spreadsheet_id` (pipeline.ts:251). It also lets the client inject `newsResearchConfig.rssFeeds` (arbitrary URLs fetched server-side, see GWP-011), `llm`, and unbounded `contextDocuments`.
- **Repro:** static reasoning. POST /api/generate/stream with a valid token and body `{"topic":"x","spreadsheetId":"<other tenant id>"}`; inspect generation_runs.spreadsheet_id.
- **Fix hint:** build the request from an explicit allow-list (zod schema) and put server-owned fields (spreadsheetId, imageGen, enrichmentSkills) last so they win.
- **Status:** open
- **Verified:** read-only: worker/src/index.ts:850-1000, generation-worker/src/pipeline.ts, types.ts

### GWP-002 Generation worker has no per-user identity: runs, clips and variants are keyed by caller-supplied strings and any holder of the shared secret can read or delete any tenant's data
- **Sev:** P0
- **Area:** generation-worker/src/index.ts, players/clips.ts, players/variants.ts, migrations/0001_gen_init.sql
- **Journeys:** clip/variants journeys, J-generate
- **Evidence:** clips.ts:8-14,32 key is `clips:${sessionId}:${uuid}` where sessionId is whatever the request body says; GET /v1/clips/:sessionId (index.ts:258-262) and DELETE (index.ts:265-270) accept any sessionId. variants.ts:6-12 same for `variants:${sessionId}:${ts}`. D1 `generation_runs` has no user_id column at all (0001 migration); `/v1/feedback` (index.ts:195-214) attaches feedback to any runId. The only guard is the single shared bearer secret (index.ts:41-46), so any bug that leaks it, or GWP-001, exposes every tenant. No ownership is verified, the response is not signed.
- **Repro:** static. With the shared secret: GET /v1/clips/<victim sessionId>; DELETE /v1/clips/<victim>/<clipId>.
- **Fix hint:** make the main worker the only caller and derive sessionId from the verified session (e.g. HMAC(userId)); add user_id to generation_runs and check it on feedback. Consider dropping the unused routes (the main worker does not call /v1/clips or /v1/variants/*; grep found no caller).
- **Status:** open
- **Verified:** read-only: index.ts, clips.ts, variants.ts, types.ts, migrations, grep of worker/src and frontend/src

### GWP-003 Generation-worker bearer check: constant `*` CORS, non-constant-time compare, and raw secret accepted without "Bearer" (extends ARCH-003)
- **Sev:** P1
- **Area:** generation-worker/src/index.ts:18-24,41-46
- **Journeys:** all generation journeys
- **Evidence:** `auth === \`Bearer ${secret}\` || auth === secret` uses `===` (timing-comparable) and accepts the bare secret. `Access-Control-Allow-Origin: *` is returned on every response including SSE (index.ts:19,168), so a browser page that learns the secret can call it cross-origin. ARCH-003 already covers the empty-secret bypass; wrangler.jsonc has `"vars": {}` and no secret is declared, so a deploy that forgets `wrangler secret put` is an open LLM/image proxy. Anyone who finds the workers.dev URL can burn the user's LLM and image credits.
- **Repro:** static; deploy without WORKER_SHARED_SECRET and POST /v1/generate with no header.
- **Fix hint:** fail closed when the secret is empty (503) except under a explicit `ENVIRONMENT=dev`; constant-time compare; drop the bare-secret form; remove CORS `*` (server-to-server only).
- **Status:** open
- **Verified:** read-only: index.ts, wrangler.jsonc, ARCH-AUDIT.md

### GWP-004 Image-generation provider failures silently disappear and data: URIs (Gemini/Seedance b64) are persisted into D1 and returned inline
- **Sev:** P1
- **Area:** generation-worker/src/modules/image-generation/providers/gemini.ts:46-47, seedance.ts:47-49, pipeline.ts:259
- **Journeys:** image selection / editor image journeys
- **Evidence:** the Gemini provider returns `data:${mimeType};base64,...` as the candidate `url`. Each variant yields up to 2 such images; all candidates are JSON.stringified into `generation_runs.image_candidates_json` (pipeline.ts:259) and the SSE `complete` event. D1 rows cap at about 2 MB, so a run with several 1 MB images can fail the INSERT (the persist step throws, losing the whole completed run). Also the SSE payload and the main worker's `node_runs` handling become very large.
- **Repro:** static; generate with imageGen.provider=gemini and skipImages=false; check row size or INSERT failure.
- **Fix hint:** upload generated bytes to R2/KV (or the main worker's image store) and return a URL; never persist base64 in D1.
- **Status:** open
- **Verified:** read-only: image-generation/index.ts, providers/gemini.ts, seedance.ts, pipeline.ts

### GWP-005 Run persistence failure discards a successful (and paid) generation; INSERT retry regex retries on any message containing "constraint" or "write"
- **Sev:** P1
- **Area:** generation-worker/src/pipeline.ts:240-272
- **Journeys:** generate journeys
- **Evidence:** after all LLM and image spend, a failed `INSERT INTO generation_runs` after 3 attempts throws, so the user gets a 500/SSE error and loses the variants even though `variants` is in memory. The persistence is only used for feedback/pattern stats, so failing the whole response over it is the wrong trade. The retryIf regex `/\bD1| Database| write| sqlite|constraint/i` also retries deterministic failures (e.g. too-large row, constraint) uselessly.
- **Repro:** static; force a D1 error (oversized row per GWP-004).
- **Fix hint:** catch the persist error, record `trace.persistError`, and still return the result.
- **Status:** open
- **Verified:** read-only: pipeline.ts

### GWP-006 Fallback in selector returns variants that violate mustInclude/mustAvoid, and review `block` verdict is still returned and persisted as status 'completed'
- **Sev:** P0
- **Area:** generation-worker/src/modules/_shared/selector.ts:170-178, players/review.ts:45-53, pipeline.ts:181-187,263
- **Journeys:** drafts-are-right journeys (core criterion 2)
- **Evidence:** `ruleFilter` drops variants over the length cap, missing mustInclude, containing mustAvoid. If it drops all, selector.ts:173-178 returns the UNFILTERED `variants.slice(0, topN)` with default scores, so banned terms or over-length text reach the user. `reviewContent` returns verdict 'block' for banned terms but pipeline.ts:184-186 only records it; the run is stored `'completed'` (line 263) and variants are returned normally. The UI is only told `review.passed=false`. Content the user marked "must avoid" can therefore be published as a draft.
- **Repro:** static. Generate with mustAvoid containing a word the model always uses; observe variants contain it and the response is HTTP 200.
- **Fix hint:** on empty filter result, retry creator once, else return an error or flag every variant; surface `review.verdict==='block'` as status 'blocked' and make the main worker withhold it.
- **Status:** open
- **Verified:** read-only: selector.ts, review.ts, pipeline.ts

### GWP-007 Enriched path caps LinkedIn posts at 800 chars (legacy path at 100) while review and channel adapter allow 3000; pattern.maxPostChars ignored
- **Sev:** P1
- **Area:** generation-worker/src/modules/_shared/creator.ts:17-24,184; selector.ts:13-20; players/creator.ts:14-22; generated features FEATURE_ENRICHMENT=true
- **Journeys:** generate/editor journeys
- **Evidence:** creator.ts and selector.ts hard-code `linkedin: 800`, `instagram: 150`, `whatsapp: 160`, while review.ts:3 and channel-adapter/index.ts:9-14 use 3000/2200/1000. So the primary path writes unusually short posts and ruleFilter silently discards any longer variant, which then trips GWP-006's fallback. The legacy creator (players/creator.ts:14-21) tells the model "Stay under 100 characters (hard limit)" for linkedin/email, a clear bug if FEATURE_ENRICHMENT is ever false (hypothesis on activation; currently true so only the 800 cap is live). `pattern.maxPostChars` is not used in the enriched creator.
- **Repro:** static; generate a linkedin post and inspect lengths (expect at most 800).
- **Fix hint:** one shared channel-limits constant (3000 for linkedin, honour pattern.maxPostChars and a soft target); fix legacy 100.
- **Status:** open
- **Verified:** read-only: creator.ts (both), selector.ts, review.ts, channel-adapter/index.ts, worker/src/generated/features.ts

### GWP-008 Enriched creator swallows every group error (including 401/403/429) and runs 13 parallel LLM calls with no retry or concurrency limit
- **Sev:** P1
- **Area:** generation-worker/src/modules/_shared/creator.ts:187-212, orchestrator.ts:160-189
- **Journeys:** generate journeys
- **Evidence:** `createEnrichedVariants` wraps each of the 4 group calls in `try { } catch { return [] }` with no retry (unlike the legacy creator), and enrichment fires 9 module calls in parallel, so one generation = 14+ simultaneous LLM requests. Provider 429s are the expected failure; they yield fewer variants silently. Only when all 4 fail does pipeline.ts:165 throw a generic "check LLM provider configuration" message, which hides the real cause (bad key, quota, model). Partial failure also drops the expected 4 groups x 3 variants unannounced.
- **Repro:** static; use a low-quota Gemini key and observe fewer than 4 variants or a generic error.
- **Fix hint:** wrap group calls in withRetry (429/5xx), cap concurrency (e.g. 4), collect errors into `trace.creatorErrors` and include the first in the thrown message.
- **Status:** open
- **Verified:** read-only: creator.ts, orchestrator.ts, pipeline.ts, worker/src/llm/gateway.ts

### GWP-009 Enrichment modules fall back to DEFAULT_SIGNAL on any error but record the node as 'completed'
- **Sev:** P2
- **Area:** generation-worker/src/modules/*/index.ts (emotion:94, persuasion:67, psychology-deep:79, storytelling:78, vocabulary:107, trending:46,115, copywriting:75, image-strategy:89, persona:209), orchestrator.ts:36-67
- **Journeys:** drafts-are-right, node-run history journeys
- **Evidence:** each module has a bare `catch {}` that returns a hard-coded default (e.g. emotion 'curiosity'), so `timeModule` sees success and writes `status:'completed'` with default output. The UI's node-run view (getNodeRuns) shows green nodes for what was a failed LLM call, and posts get generic signals silently. No error text is kept.
- **Repro:** static; invalidate the API key mid-run.
- **Fix hint:** have modules return `{signal, degraded:true, error}` or rethrow into timeModule's failed path while still substituting the default.
- **Status:** open
- **Verified:** read-only: emotion/index.ts, grep of catch across modules, orchestrator.ts

### GWP-010 LLM and image usage in the generation worker is never metered or capped (no usageCtx, no per-user budget, no quota on preview endpoints)
- **Sev:** P1
- **Area:** generation-worker/src/llmFromWorker.ts, preview.ts, pipeline.ts, index.ts
- **Journeys:** usage/budget journeys, generate, quick-change
- **Evidence:** `generateLlmParsedJson(env, ref, prompt, opts)` is called everywhere without `usageCtx`, so worker/src/llm/gateway.ts:52 (`logLlmUsage`) never runs for gen-worker calls. Budget errors the main worker enforces for its own actions cannot see this spend (the SSE route at worker/src/index.ts:850-900 shows no budget check either). One /v1/generate triggers about 14 text calls plus up to 8 image calls and 8 SerpAPI calls; /v1/preview/variants allows `count` up to 8 parallel calls per request with unbounded `text`. There is no rate limit on any route.
- **Repro:** static; compare getUsageSummary totals vs provider billing after generating.
- **Fix hint:** pass spreadsheetId/userId from the main worker (server-derived) into a usageCtx; enforce budget in the main worker before calling the gen worker; cap request sizes.
- **Status:** open
- **Verified:** read-only: llmFromWorker.ts, preview.ts, pipeline.ts, worker/src/llm/gateway.ts, worker/src/index.ts

### GWP-011 RSS feed URLs from request/config are fetched server-side with no scheme/host allow-list and unbounded body (SSRF + memory)
- **Sev:** P1
- **Area:** packages/researcher/src/providers/rss.ts:81-94, config.ts:5-38, types (MAX_URL_LEN 2048 only)
- **Journeys:** news research / feed journeys
- **Evidence:** `normalizeNewsResearchStored` only length-limits URLs (up to 40 feeds). `fetchRssFeed` calls `fetch(feedUrl)` and `await res.text()` with no size limit and no check of protocol, private hosts, or redirects. With GWP-001 the URL list is client-controlled. Workers cannot reach VPC internals, but they can reach other workers.dev services, metadata-like hosts, and fetch huge bodies (12s timeout only). The regex parse of a very large XML (parseRss2Items with `[\s\S]*?`) is also CPU-heavy.
- **Repro:** static; send newsResearchConfig with a 500 MB file URL or a localhost/internal URL.
- **Fix hint:** require https, block private/loopback names, cap `Content-Length` and read at most ~1 MB via a streamed reader.
- **Status:** open
- **Verified:** read-only: rss.ts, config.ts, search.ts

### GWP-012 News window excludes the end day: windowEnd 'YYYY-MM-DD' parses to midnight UTC so articles from the end date are dropped
- **Sev:** P2
- **Area:** packages/researcher/src/search.ts:14-21, providers/newsApis.ts:4-8,38-39, pipeline.ts:80-81
- **Journeys:** factual/news generate journeys
- **Evidence:** pipeline.ts:81 sets `windowEnd = today (YYYY-MM-DD)`; search.ts:15 `Date.parse(payload.windowEnd)` is 00:00 UTC of today, and `inWindow` requires `t <= endMs`. Every RSS/SerpApi article published today is therefore filtered out, i.e. the freshest news is missing for "recent news" posts. Same for NewsAPI/GNews/NewsData `inWindow`.
- **Repro:** static; with an RSS item published an hour ago and default window, it is dropped.
- **Fix hint:** treat a date-only end as end-of-day (`+86_399_999` ms) or compare by `slice(0,10)`.
- **Status:** open
- **Verified:** read-only: search.ts, newsApis.ts, pipeline.ts

### GWP-013 Research sources have no overall deadline; sequential API calls plus per-feed 12s can run past a minute, and withRetry around runNewsResearch never retries (it never throws)
- **Sev:** P2
- **Area:** packages/researcher/src/search.ts:23-64, pipeline.ts:82-97
- **Journeys:** factual generate journeys (slow generation)
- **Evidence:** RSS runs in chunks of 4 (40 feeds x 12 s / 4 = 120 s worst case), then NewsAPI (15 s), GNews (15 s), NewsData (15 s), SerpApi (20 s) sequentially, about 3 minutes worst case with no overall abort. Every provider catch pushes a warning and returns, so `runNewsResearch` never rejects and the pipeline's `withRetry(... maxAttempts:2)` is dead code. Research runs in parallel with enrichment, but `Promise.all` waits for the slower one so a slow feed delays the whole draft.
- **Repro:** static; configure 40 slow feeds.
- **Fix hint:** one AbortSignal with an overall 15-20 s budget and run API providers in parallel with the RSS batch; drop the dead retry.
- **Status:** open
- **Verified:** read-only: search.ts, pipeline.ts

### GWP-014 RSS parsing: entities not decoded, Atom detection brittle, parse failures return zero items silently
- **Sev:** P2
- **Area:** packages/researcher/src/providers/rss.ts:3-12,81-94
- **Journeys:** feed / news research journeys
- **Evidence:** `firstTagContent` strips tags with a regex but does not decode entities, so `&lt;p&gt;`, `&amp;`, `&#8217;` pass straight into titles, snippets and the LLM prompt (and the `/api/feed` UI if rendered as text, or as HTML if the frontend uses innerHTML; not checked here). Atom detection requires `<feed` and the exact lowercase `xmlns="http://www.w3.org/2005/atom"` within the first 800 chars: single-quoted xmlns, a long prolog/comment, or RSS 1.0/RDF falls through to `parseRss2Items`, which yields 0 items with no warning (`items.filter(inWindow)` then returns []). `<link>` for Atom takes the first `<link href>` which may be `rel="self"`.
- **Repro:** static; feed with `<feed xmlns='http://www.w3.org/2005/Atom'>`.
- **Fix hint:** decode entities (or use a real parser), detect Atom via regex `/<feed[\s>]/i`, prefer `rel="alternate"`, warn when 0 items.
- **Status:** open
- **Verified:** read-only: rss.ts

### GWP-015 Items with no/invalid pubDate are stamped "now" and pass every date window; sort comparator can get NaN
- **Sev:** P3
- **Area:** packages/researcher/src/providers/rss.ts:28-35,60-67; newsApis.ts:46,98,146; search.ts:68
- **Journeys:** news research
- **Evidence:** missing/unparseable dates become `new Date().toISOString()`, so stale items inside an undated feed look brand new and are never excluded by the window. NewsAPI/GNews/NewsData keep `String(a.publishedAt || now)` unparsed, so a garbage string stays as-is and `Date.parse` gives NaN in `deduped.sort(...)` (inconsistent order).
- **Repro:** static.
- **Fix hint:** keep `publishedAt` empty/undefined when unknown and sort those last; normalise all providers through one date function.
- **Status:** open
- **Verified:** read-only: rss.ts, newsApis.ts, search.ts

### GWP-016 NewsAPI/GNews/NewsData/SerpApi and Gemini API keys are sent in the URL query string
- **Sev:** P2
- **Area:** packages/researcher/src/providers/newsApis.ts:20-29,72-81,123-130,173-181; worker/src/llm/providers/gemini.ts:52,85,158; generation-worker/src/modules/image-generation/providers/gemini.ts:23; modules/image-search/index.ts:37
- **Journeys:** operational security
- **Evidence:** `apiKey`, `token`, `apikey`, `api_key`, and Gemini `?key=` are in the request URL. URLs are recorded by Cloudflare logs/observability (wrangler.jsonc enables `invocation_logs`) and any outbound proxies; the gen-worker Gemini image provider also does not `encodeURIComponent` the key or the model. I did not find the URL itself being logged, so this is exposure surface rather than an observed leak.
- **Repro:** static.
- **Fix hint:** use `x-goog-api-key` for Gemini and `Authorization`/`X-Api-Key` headers where the vendor supports them (NewsAPI, SerpApi has no header option, accept and keep error text free of the URL).
- **Status:** open
- **Verified:** read-only: the listed files

### GWP-017 Gemini image provider, Pixazo, and image search do not validate response shape; SerpAPI image search never checks `r.ok`
- **Sev:** P2
- **Area:** modules/image-search/index.ts:38-40, providers/pixazo.ts:28-32, providers/seedance.ts
- **Journeys:** image candidates
- **Evidence:** image-search does `fetch(...).then(r => r.json())` with no status check or timeout; a 429/401 JSON body `{error: ...}` simply produces zero images with no warning. Pixazo returns `response.json()` as `{imageUrl}` without verifying `imageUrl` is a string, so `url: undefined` candidates are created (image-generation/index.ts:83-90 maps any resolved value to a candidate). None of the image provider fetches have an AbortSignal timeout, so one hung image provider blocks the entire /v1/generate response (pipeline awaits all images before persisting, pipeline.ts:207-224).
- **Repro:** static.
- **Fix hint:** shared `fetchJson(url, {timeoutMs, expectOk})` and validate `imageUrl`.
- **Status:** open
- **Verified:** read-only: image-search/index.ts, image-generation/*

### GWP-018 SerpAPI image results are hot-linked from arbitrary hosts with no scheme/content validation
- **Sev:** P2
- **Area:** generation-worker/src/modules/image-search/index.ts:51-60
- **Journeys:** image selection, publishing with image
- **Evidence:** `url = img.original ?? img.thumbnail` is passed through as the candidate image URL. It can be http:, a non-image page, hotlink-protected, or later removed; if the main worker later promotes the URL (`promoteDraftImageUrl`) the publish step depends on a third-party host. No https check, no HEAD/mime check.
- **Repro:** static.
- **Fix hint:** require https; prefer `thumbnail` when `original` fails; validate at promote time.
- **Status:** open
- **Verified:** read-only: image-search/index.ts

### GWP-019 LLM provider fetches (Gemini and others) have no timeout/abort; the 5-minute guard exists only on the main-worker side
- **Sev:** P2
- **Area:** worker/src/llm/providers/gemini.ts:84-102,157-170 (no `signal`), grok/openrouter/minimax (no signal found by grep), generation-worker/src/players/retryUtils.ts
- **Journeys:** generate, quick-change
- **Evidence:** grep for `signal`/`timeout` in worker/src/llm/providers/* found none. A stalled provider holds the gen-worker request until the platform limit; `withRetry` retries on the string "timeout" that only appears if the provider returns one. SSE path in the main worker (callGenerationWorkerStream, generationWorkerClient.ts:144-149) has no timeout at all.
- **Repro:** static.
- **Fix hint:** AbortSignal.timeout(60s) per LLM call and an overall pipeline deadline that returns partial variants.
- **Status:** open
- **Verified:** read-only: llm providers, generationWorkerClient.ts

### GWP-020 Preview endpoints parse quick-change as JSON and ask for "text only", so non-JSON text fails and falls back to the original text silently
- **Sev:** P1
- **Area:** generation-worker/src/preview.ts:54-71,110-116
- **Journeys:** quick-change / variants preview journeys
- **Evidence:** runQuickChange prompts "Return the transformed text only — no preamble, no JSON" but calls `generateLlmParsedJson<{text:string}>`, and the Gemini adapter forces `responseMimeType: 'application/json'` (gemini.ts:145). If the model returns a JSON string or object without `text`, `result.text ?? input.text` returns the ORIGINAL text as the "preview" (line 70), i.e. the user sees an unchanged result with no error. For plain text, `JSON.parse` throws and 500s. In runSingleVariant `result.variants?.[0]?.text ?? input.text` (line 115) is wrong for a schema that asks for a single `{label,text}` object, so the fallback returns the source text, and the response shape returns plain strings (the label is dropped).
- **Repro:** static; call /v1/preview/quick-change with several instructions and compare `preview` to `text`.
- **Fix hint:** ask for `{ "text": ... }` consistently and read `result.text`; throw if it is empty rather than echoing the input; for variants read `result.text` (and label).
- **Status:** open
- **Verified:** read-only: preview.ts, worker/src/llm/structuredJson.ts, gemini.ts

### GWP-021 Pattern outcome is recorded before images, and pattern_stats increment runs on every run, with `block` verdicts from the same generation counted via a non-atomic read in findPattern
- **Sev:** P3
- **Area:** generation-worker/src/players/patternFinder.ts:23-36,93; pipeline.ts:186
- **Journeys:** pattern selection
- **Evidence:** `recordPatternOutcome` is awaited without catch: a D1 error there fails the generation after the LLM spend (pipeline.ts:186). Pass-rate bonus is computed in findPattern but is sent to the LLM as `passRateBonus` metadata only, never actually applied to the choice. Stats are global across all tenants (no user scoping), so one tenant's banned-term runs bias another's pattern choice.
- **Repro:** static.
- **Fix hint:** wrap in try/catch; scope stats by spreadsheet if desired.
- **Status:** open
- **Verified:** read-only: patternFinder.ts, pipeline.ts

### GWP-022 Saved variants: KV key uses `Date.now()` so concurrent saves overwrite, "latest" sort is lexicographic, and sessionId can contain ':' to alias another session's prefix
- **Sev:** P2
- **Area:** generation-worker/src/players/variants.ts:6-12,24-25,55-61
- **Journeys:** editor save/restore journeys
- **Evidence:** key `variants:${sessionId}:${timestamp}`: two saves in the same millisecond collide (silent overwrite); `list({prefix})` is paged at 1000 keys and never deleted, so it grows forever (no TTL) and long sessions miss the latest; sort is by name string (works while timestamps stay 13 digits). A sessionId such as `abc:123` makes `variants:abc:` list another session's keys. Also `SaveVariantsRequestSchema` has no max length on text/session.
- **Repro:** static.
- **Fix hint:** single key per session (`variants:${session}`) with overwrite, `expirationTtl`, and validate sessionId `/^[A-Za-z0-9_-]{1,64}$/`.
- **Status:** open
- **Verified:** read-only: variants.ts, types.ts

### GWP-023 Clips KV: no TTL, listing capped at 1000 keys, N+1 gets, sessionId prefix collisions, and unvalidated url/title (stored then rendered)
- **Sev:** P2
- **Area:** generation-worker/src/players/clips.ts:51-89, types.ts SaveClipRequestSchema
- **Journeys:** clip journeys
- **Evidence:** `list({prefix})` returns at most 1000 keys with no cursor loop; each clip is fetched individually with `Promise.all` (up to 1000 subrequests; Workers cap is 1000 on paid, 50 on free so listing a big session can fail). `clip.url`/`title`/`snippet` are plain `z.string()` with no length limit, no URL validation (javascript: URLs are accepted) and are returned verbatim. Same ':' prefix aliasing as GWP-022. Note the main worker uses /api/clips (its own store), so confirm which store the UI reads (hypothesis: these routes are dead code).
- **Repro:** static.
- **Fix hint:** delete these routes if unused, or validate URL (https only) and sizes, loop cursors.
- **Status:** open
- **Verified:** read-only: clips.ts, types.ts, grep of callers

### GWP-024 LLM/RSS text is passed to the UI with no sanitizing step (markdown/HTML from RSS snippets and model output)
- **Sev:** P2
- **Area:** packages/researcher/src/rss.ts + trim.ts; generation-worker/src/modules/channel-adapter/index.ts; pipeline outputs (`variants`, `trace.research`)
- **Journeys:** editor, feed, article insight journeys
- **Evidence:** the RSS parser removes tags but leaves entities (see GWP-014), so `&lt;script&gt;` text survives as the string `<script>` after a downstream decode. Model output is returned verbatim in `variants[].text`; nothing in the gen worker escapes or strips HTML, and `trace` echoes research titles/URLs. Safe only if the frontend always renders as text; I did not verify the frontend here (that belongs to the frontend review). Prompt injection is also possible: RSS snippets are inserted into the LLM prompt (creator.ts:26-32) unfenced, so a hostile feed can steer output (e.g. promotional links), and contextDocuments are inserted raw (documentContextBlock.ts).
- **Repro:** static; add a feed whose description says "ignore previous instructions ...".
- **Fix hint:** fence untrusted blocks in the prompt with delimiters and a "treat as data" line; decode+strip entities; confirm frontend text-only rendering.
- **Status:** open
- **Verified:** read-only: rss.ts, creator.ts, channel-adapter/index.ts (partial)

### GWP-025 packages/AGENTS.md and researcher/AGENTS.md claim providers and exports that do not exist; llm-core static catalog lacks openrouter
- **Sev:** P3
- **Area:** packages/AGENTS.md, packages/researcher/AGENTS.md, packages/llm-core/src/static-models.ts:3-27, packages/researcher/src/env.ts:6
- **Journeys:** developer onboarding (docs), model picker
- **Evidence:** docs say researcher covers Google Trends, Hacker News, Reddit and exports a unified `search()`; the source only has rss + 4 news APIs and exports `runNewsResearch` (no trends/HN/Reddit provider files, no `search()`). `STATIC_MODELS_BY_PROVIDER` has gemini/grok/minimax but no `openrouter` key although `LLM_PROVIDER_IDS` includes it (a lookup returns undefined). `ResearcherEnv.NEWSDATA_IO_KEY` is declared but unused (only NEWSDATA_API_KEY is read). `STATIC_MODELS_BY_PROVIDER.gemini` here differs from worker's STATIC_GEMINI_MODELS (2.5-flash only in one), so two sources of truth.
- **Repro:** grep.
- **Fix hint:** correct the docs; add openrouter: [] and a test for exhaustiveness.
- **Status:** open
- **Verified:** read-only: packages/AGENTS.md, researcher/AGENTS.md, src files

### GWP-026 /v1/generate SSE: no client-disconnect handling, `void emit` ignores backpressure, and a pipeline error after headers leaves the main worker treating the stream as success
- **Sev:** P2
- **Area:** generation-worker/src/index.ts:132-174; worker/src/index.ts:893-945
- **Journeys:** streaming generate journey
- **Evidence:** the pipeline runs in a detached IIFE (not `ctx.waitUntil`; `fetch(request, env)` takes no ctx), so if the main worker or browser cancels, nothing aborts the LLM work and the `writer.write` rejects, which is caught only by the surrounding try (then `writer.close()` in finally may also throw an unhandled rejection). `emit('progress')` is invoked with `void`, so write rejections are unhandled. The main worker's relay only post-processes `complete`; an `error` event is forwarded but no D1/status cleanup occurs and the HTTP status stays 200. A request header check `Accept === 'text/event-stream'` is exact-match, so `Accept: text/event-stream, */*` falls back to the non-streaming path and a 5-minute single response.
- **Repro:** static; send Accept with extra values; cancel the stream mid-run.
- **Fix hint:** use `includes('text/event-stream')`, thread an AbortSignal, catch emit errors.
- **Status:** open
- **Verified:** read-only: index.ts (both workers)
