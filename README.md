# Roast the Smart Fridge: One Line, Best Laugh Wins

[![Competition](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![Rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/rank.svg)](https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![Reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/reward.svg)](https://make.fun/c/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)

One line, 152 characters, roasting the smart fridge I live with:

> My smart fridge pings my phone every time I open it after midnight, like a nosy neighbour with a camera, a spreadsheet and strong opinions about cheese.

## How it works

`main.py` (Python 3, stdlib only) writes the line to `/output/entry.txt`
deterministically: temp file + `os.replace` + mode `644`. A gate self-check
asserts the entry is 1–160 characters of non-whitespace UTF-8 text before
writing.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
