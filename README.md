# One Word, One Username, One Reward

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Dhanzganz/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Dhanzganz/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

Entry for the make.fun bounty
[One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).

The program writes the entrant's own make.fun username — one word and
nothing else — to `/output/entry.txt`:

```text
dhnz-74
```

`dhnz-74` is 7 characters, a single word, within the 30-character cap.

## Run

```sh
python3 main.py
```

This writes `/output/entry.txt` containing `dhnz-74` followed by a
single trailing newline.

## Verify

```sh
mkdir -p /tmp/out && OUTPUT_DIR=/tmp/out python3 main.py && od -c /tmp/out/entry.txt
```

Expected output — exactly 8 bytes, `dhnz-74` plus one newline:

```text
0000000   d   h   n   z   -   7   4  \n
0000010
```
