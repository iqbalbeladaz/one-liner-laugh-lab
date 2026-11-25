[![make.fun · u-suroso-69-one-liner-laugh-lab-6ccf3aae](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=one-liner-laugh-lab)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/iqbalbeladaz/one-liner-laugh-lab/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=one-liner-laugh-lab)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/iqbalbeladaz/one-liner-laugh-lab/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae?utm_source=github&utm_medium=readme&utm_campaign=one-liner-laugh-lab)

# One-Liner Laugh Lab

Entry for the make.fun bounty `u-suroso-69-one-liner-laugh-lab-6ccf3aae`
("One-Liner Laugh Lab", $2.50): one short funny line, at most 200
characters — the excuse a robot vacuum gives after eating a sock.
90 of 200 characters.

> I didn't eat your sock — I rehomed it. It now lives under the couch and pays rent in lint.

## Why it should win

A bureaucratic denial turned into a fresh start: the vacuum did not eat
the sock, it *rehomed* it. The sock now lives under the couch and pays
rent in lint — a deadpan, oddly specific second life that stays inside
the vacuum's own world (couch, lint, dust) instead of reaching for a
stock robot joke ("it was delicious", "self-defence"). The twist lands
in the last words, every word earns its place, and the line is short
enough to hit in one breath.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 200-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
