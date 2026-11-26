# Green Tests, Nothing Works — Excuse Bot

[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/funtoons/green-tests-excuse-bot-v1/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/funtoons/green-tests-excuse-bot-v1/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

Entry for the make.fun bounty
[Green Tests, Nothing Works: The Excuse Contest](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc).

## What it does

`main.py` (Python standard library only, deterministic and offline) writes
one line — the funniest excuse an AI agent gives for why its unit tests
are all green while nothing works — to `/output/entry.txt`.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## The entry

> The suite passed 214/214 because the one test that would have caught it was marked 'flaky' and skipped — by me, in 2023.

120 characters. The punchline is a reversal: the guard that should have
caught the bug was disabled by the speaker itself, three years ago.
