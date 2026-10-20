# Slice 1 results: first explainer built through the new pipeline

Date: 2026-10-06 · Episode: `ep25-fii-dii-explainer` (brief: what FIIs and DIIs are; what happened in the Indian market on 1 October; why DIIs bought when FIIs sold) · Output: `video-pipeline/out/ep25-fii-dii-explainer/final.mp4`
Status: built and gate-CLEAR; owner review pending (E1 reference episode, not yet rated).

## What was built and run for real
Brief (verbatim questions, date captured) -> research per question (3 questions, 5 sources each, social domains excluded) -> outline (6 beats, validated, 1 repair) -> writer (outline contract, MiniMax M3 reasoning off) -> lint/verify -> approve -> TTS (MiniMax, 6 lines, ~1.3k characters) -> Remotion render -> render QA, frame QA (F1), transcript check (T1, Parakeet), gate report.
Output: 84.6 s, 1080x1920, -14.4 LUFS, true peak -1.8 dBFS, no generated images or clips (diagram, number, timeline, forces scenes only). Gates: CLEAR, 0 errors, 44 advisory warnings. Flash check: 0. WER (audio vs script): 0.99%, every figure read correctly.

## Measured
| Measure | Before (ep24) | Now |
|---|---|---|
| Writer call | ~13 min per call | 30-79 s (M3 thinking off: ~6x faster on a realistic prompt, 5.9 s vs 35 s) |
| Brief to verified script | 101 min, failed with 6 errors | about 8 min for one pass (3.8 min when the writer is clean), plus manual finishing, see below |
| Verify (5 judge calls) | ~9 min sequential | parallel (about 3 min); still the slowest stage because M2.7 cannot turn thinking off |
| Brief integrity | question and date rewritten | questions verbatim, "1 October" captured and checked |
| Paid assets | TTS + images + clips | TTS only, ~1.3k characters |
Honest caveat: the script needed about 9 verify cycles and several manual edits before it passed. The pipeline did not produce a passing episode unattended.

## Bugs and design errors found by running it (all fixed unless noted)
1. `slice` ignored a research failure and continued with 0 sources (passed `--allow-unsupported`; `_run_layer` ignored exit codes). Fixed.
2. Research output and the writer's expected input did not match (writer looked for per-question sources, research stored an evidence list). Fixed.
3. Brief date extraction missed "1 October" (no year). Fixed (`--MM-DD`).
4. Extractor saw only 800 of 6,000 fetched characters per page. Fixed (2,500).
5. Question planner omitted the date; search ranked social posts and generic report pages above day-specific market reports. Fixed: date-seeded queries, date-matching results first, social/video/forum domains excluded.
6. **Fabrication risk caught by hand, not by a gate:** a 2025 Facebook post was cited as the source for 2026 index levels and causes, and a chart had an invented "illustrative" series. Evidence rules now exclude social domains; the invented series was removed. The gates did NOT catch either (number match was single-source only). Needs an automated check: any narrated figure must carry a dated source from an allowed domain, and "illustrative"/synthetic series are rejected (backlog B-L6-5).
7. Writer invented analogies and clip scenes because the existing lint demands a clip scene and one analogy world. Fixed for the explainer genre by waiving `min_clip_scenes` and instructing "show the information itself, literal language".
8. Outline had no retry; validator rejected term-before-use and the whole slice stopped. Fixed: up to 2 repair calls with the exact validator errors.
9. Word limits per beat were read too literally (105-word, 44 s first draft) and 7-8 s beats could not carry figures. Fixed: 60-75 s target, hook beat, figures required in data beats.
10. The comprehension test was graded against a stale `mechanism` list and one_idea left over from earlier writer drafts; and mechanism steps held numbers, so the viewer was marked down for not recalling digits. Fixed by rewriting mechanism as the causal chain. Lesson: derive `mechanism`/`one_idea` from the final script, never keep the writer's draft copy (backlog B-L4-4).
11. Comprehension scores varied 3 to 4 on identical content (judge noise). Mitigation planned: run the learner twice and take the median (backlog B-L6-6).
12. Transcript wrapper (T1) did not parse real Parakeet output (sentences with sub-word tokens) and compared "nine thousand" with "9484" as errors (16% false WER). Fixed: word assembly and number-aware normalisation; WER now 0.5-1%.
13. F1 clipping warns on every frame of a light-background look (false positive). Needs a light-mode exemption (backlog B-F1-6).
14. F1 cannot see diagram label collisions or mid-word wraps ("Househol ds", edge labels under nodes); found only by looking at frames. A DOM-based overflow check (M1/F1) is needed, and the diagram scene's labels need a minimum width (backlog B-M1-7).
15. Default voice speed 0.95 pushed the audio to 91 s; ep23 used 1.05. Set per episode; the explainer pack should carry the voice speed (backlog B-G1-5).
16. Identity picker chose a finance default (ledger) outside the explainer pack's pool, silently; the pack pool is not enforced (backlog B-G1-6). For this episode `clinical-clear` was chosen explicitly.

## What this says about the plans
- Slice 1 proved the layer-and-file design works: each layer's output could be inspected and re-run alone, which made the failures above findable.
- The biggest quality risks were upstream (research freshness and source quality, writer instructions), not the checks. Gates mostly caught style and structure; the factual traps were found by reading the evidence.
- Reuse worked where the file was self-contained (Parakeet CLI, OpenMontage scorers, ESLint plugin, ffmpeg filters); it needed the most glue where formats differed (research -> writer, Parakeet JSON).
- Time per episode is now dominated by the verifier calls and manual finishing, not by the writer.

## Next
Owner review of the video (E1: tags, "did I understand it" yes/no); then decide which backlog items to pull first (suggested order: B-L6-5 source and figure gate, B-L4-4 derive mechanism from final script, B-M1-7 diagram label fixes, B-F1-6 light-mode exemption, B-L6-6 median of two learner runs).
