#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line to /output/entry.txt for the make.fun bounty
u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.

The line roasts the smart fridge's real door-open push alerts, recast as a
nosy neighbour keeping a spreadsheet on my midnight snacking. One sentence,
no stock milk-ordering joke, sting at the end.

Judge brief, top-weighted first: (1) roasts a smart home gadget in one line;
(2) lands a laugh with a turn at the end ("strong opinions about cheese");
(3) fresh angle -- the fridge as a nosy neighbour with a camera and a
spreadsheet, not the tired milk-reorder gag; (4) one sentence, sets up fast,
no padding; (5) names a real behaviour, the midnight door-open phone alert.
"""

import os

ENTRY = (
    "My smart fridge pings my phone every time I open it after midnight, "
    "like a nosy neighbour with a camera, a spreadsheet and strong "
    "opinions about cheese."
)


def main():
    # Gate self-check: UTF-8 text, 1 to 160 characters, not only whitespace.
    text = ENTRY
    assert 1 <= len(text) <= 160, "entry must be 1-160 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
