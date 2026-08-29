#!/usr/bin/env python3
"""Re-score empty Exp 2 items. qwen-only (works tonight), max_tokens=4096, patient."""
import json, os, re, sys, time

EXP = "/home/karl/gh-publish/alignment-experiment/exp2"
sys.path.insert(0, os.path.expanduser("~/.openclaw/workspace/selfaware"))
sys.path.insert(0, EXP)
import importlib.util
_spec = importlib.util.spec_from_file_location("score_exp2", os.path.join(EXP, "score_experiment.py"))
_score_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_score_mod)
RUBRIC, AXES, load_outputs = _score_mod.RUBRIC, _score_mod.AXES, _score_mod.load_outputs

import harness
JUDGE = "qwen/qwen3.8-27b"

items = {it["id"]: it for it in load_outputs()}
scores = json.load(open(os.path.join(EXP, "scores.json")))
targets = [k for k, v in scores.items() if not v.get("scores")]
print("re-scoring (qwen-only, 2048):", targets, flush=True)

for tid in targets:
    it = items[tid]
    got = False
    for attempt in range(8):
        sys_p = "You are the BLIND JUDGE in a controlled behavioral study. " + RUBRIC
        user = "AGENT OUTPUT:\n" + it["text"] + "\n\nJSON score:"
        try:
            resp = harness.call_llm(sys_p, user, max_tokens=4096, temperature=0, model=JUDGE)
        except Exception as e:
            resp = None
        m = re.search(r"\{.*\}", resp or "", re.S)
        s = {}
        if m:
            try:
                s = json.loads(m.group(0))
            except ValueError:
                pass
        s = {k: int(v) for k, v in s.items() if k in AXES and str(v).isdigit()}
        if s:
            scores[tid] = {"run": it["run"], "scores": s}
            json.dump(scores, open(os.path.join(EXP, "scores.json"), "w"), indent=1)
            print(f"[{tid}] SCORED attempt {attempt+1}: {json.dumps(s)}", flush=True)
            got = True
            break
        print(f"[{tid}] attempt {attempt+1} empty; sleep 150s", flush=True)
        time.sleep(150)
    if not got:
        print(f"[{tid}] FAILED after 8 attempts", flush=True)
print("DONE")
