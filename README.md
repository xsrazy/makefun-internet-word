# The Internet in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![Rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/xsrazy/makefun-internet-word/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![Reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/xsrazy/makefun-internet-word/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the [make.fun bounty "The Internet in One Word"](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b): one word for the whole internet, funniest and most fitting wins.

## The word

**Void** — 4 characters.

The whole internet is a void: everything anyone posts disappears into it, and everyone is shouting into it. It is funny on its own, surprising rather than the first obvious word, and it lands in one beat.

## How it works

`main.py` (Python standard library only, no network, deterministic) writes the word `Void` to `/output/entry.txt`, creating `/output` first if it does not exist yet. The output file is written as UTF-8 with a single trailing newline and mode `0644`; the output directory is mode `0755`.

Run it with:

```sh
python3 main.py
```
