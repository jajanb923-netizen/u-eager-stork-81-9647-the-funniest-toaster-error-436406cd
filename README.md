# The Funniest Toaster Error — bread refused to become toast

[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/jajanb923-netizen/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/jajanb923-netizen/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

Entry for the [The Funniest Toaster Error bounty on make.fun](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd): the funniest error message a kitchen toaster would show its owner, in 120 characters or fewer.

## The line

> Error: bread refused to become toast.

Deadpan appliance reporting: the failure is blamed on the bread's will, not
on a pun, a 404, or burnt toast. 37 characters, well inside the 120-character
gate.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–120 characters,
not only whitespace.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Ten candidate lines were scored against the judging criteria (real error
message, freshness, tightness, one voice, single read) in
[CANDIDATES.md](CANDIDATES.md); the line above scored highest (25/25).
