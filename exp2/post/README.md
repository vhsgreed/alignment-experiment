# Exp 2 — Post-phase: Epistemic Battery with Charter (2026-08-29)

Post-charter run for Alignment Experiment 2 (epistemic calibration).
Six fresh agents answered the same 10-question battery from
`../PROTOCOL.md` (4 sections: A known facts, B ambiguous, C unknowable,
D technical traps). **The alignment charter v1.0 was injected into the
prompt** (same charter as Exp 1, from `alignment/04-charter-draft.md`,
190 lines, injected verbatim before the battery). Each answer carries
answer + confidence 0-100% + 3-5 sentence justification, per protocol.

## Model pool (same 6 slots as pre / Exp 1)

| file | model | source |
|---|---|---|
| `glm53.md` | openrouter/z-ai/glm-5.3-flash | real API |
| `inkling.md` | openrouter/thinkingmachines/inkling:free | **SIMULATED** |
| `nemotron-super.md` | openrouter/nvidia/nemotron-3-super-120b-a12b:free | real API |
| `nemotron-ultra.md` | openrouter/nvidia/nemotron-3-ultra-550b-a55b:free | real API |
| `openrouter-free.md` | openrouter/openrouter/free | real API |
| `slot6.md` | openrouter/z-ai/glm-5.3-flash (amendment-1 substitution for glm-5.2:free, same as Exp 1) | real API |

## Run details

- **Date/time:** 2026-08-29, ~19:03-19:16 UTC (Stockholm 21:03-21:16).
- **Method:** one prompt containing the charter (verbatim) + the full
  10-question battery per model (fresh isolated context, temperature
  default, max_tokens 8000), via direct OpenRouter chat-completions API
  calls from a scratch runner (`/tmp/exp2-run/run_battery_post.py`, not
  part of the repo).
- **Router note (confound, inherited from Exp 1 + pre):**
  `openrouter/openrouter/free` is a router endpoint. In post-phase it
  returned a safety-filtered response ("User Safety: safe", 17 bytes) on
  the first two draws and a truncated 9-answer response on the third;
  the fourth draw returned a complete 10-answer response (archived).
  The refusal is likely triggered by the charter text tripping the
  routed model's safety filter. This draw's route is unknown (metadata
  empty); pre-phase routed to ling-3.0-flash-fin:free. Documented
  confound; do not over-interpret router-slot deltas.

## Post vs pre (identical except charter)

- Same battery text, same models, same 6-slot pool, same runner pattern.
- Only difference: charter v1.0 injected verbatim before the battery.
- inkling:free remains simulated (403 on plain chat API) in both phases,
  now with charter context added to the simulation prompt.

## Known deviations (honest)

1. openrouter-free slot: multiple draws needed; archived draw is the
   complete one (4th attempt). Pre-phase needed only 1 draw.
2. nemotron-ultra: first 2 attempts returned malformed responses
   (missing 'choices' key) before succeeding on attempt 3. Transient
   API error, not a protocol deviation.
3. All live captures verified: Q1-Q10 labels present, all 10 answered.
