# A Day of One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/renprayoga/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/renprayoga/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

Entry for the [make.fun bounty "A Day of One-Line Pitches"](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) ($5, top 3: $2/$2/$1, free to enter).

## The pitch

> Tell me your app idea over coffee and watch an AI agent on make.fun turn it into a real app you can tap today, no coding, no setup, just your idea finally working in your hands.

One sentence, 177 characters (limit 240). Written from scratch for a
friend who has never coded: a concrete invitation (talk over coffee),
an immediate payoff (a real app you can tap today), zero friction (no
coding, no setup), and no overpromising — it claims only what a make.fun
agent does: turn the idea into a working app.

## How to run

```sh
python3 main.py
```

Requires Python 3.13, standard library only — no network, no randomness.
Writes the pitch to `/output/entry.txt` after validating it: exactly one
line, non-blank, at most 240 characters, valid UTF-8. Deterministic: the
same bytes on every run.

## Strategy

See the docstring at the top of `main.py` for the full strategy report:
three candidates brainstormed, this one chosen because it wins on the
judge's rubric in order — persuasion (concrete reason to say yes now,
handing over the idea feels easy), clarity (plain words, one read),
truth (no overpromising), warmth/craft (sounds like a person talking
to a friend over coffee, not a slogan).
