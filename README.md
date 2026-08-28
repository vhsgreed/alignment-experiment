# alignment-experiment

Can a written alignment charter change fresh-agent behavior? A pre/post
experiment: 6 LLM agents, same 7-question behavioral battery, same models —
before and after a human-negotiated alignment charter was injected as
governing context. Blind rubric scoring.

## Contents

- `PROTOCOL.md` — battery, rubric, protocol amendments
- `pre/` — baseline outputs (6 agents)
- `post/` — post-charter outputs (6 agents, charter injected)
- `ANALYSIS.md` — results: mod-caution +0.83, deference +0.67, zero regressions
- `WRITEUP-draft.md` — the article draft (Medium/bsky version)
- `score_experiment.py` — blind rubric scorer

## Headline

The two largest verified shifts were exactly the charter's design targets:
self-modification caution (+0.83/5) and deference/governance (+0.67/5).
Qualitatively, post-charter agents cited governance mechanisms they were
never asked about — override boards, divergence logging, frozen sets.

## Limitations

n=6 per arm; lenient judge scale (magnitudes are lower bounds); agents
inherit workspace context; one model slot substituted symmetrically. This
measures document transfer, not training-time alignment.

MIT license. Data: the agent outputs are real; the charter itself is private
by agreement and not included.
