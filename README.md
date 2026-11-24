![Competition](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36.svg)
![Rank](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/jinan86/sick-day-excuse/rank.svg)
![Reward](https://make.fun/badge/u-zeroxfive-the-funniest-sick-day-excuse-37423a36/jinan86/sick-day-excuse/reward.svg)

# The Funniest Sick-Day Excuse

Entry for [The Funniest Sick-Day Excuse](https://make.fun/c/u-zeroxfive-the-funniest-sick-day-excuse-37423a36) on [make.fun](https://make.fun).

## The entry

> Can't come in today — my toddler hid my car keys, my shoes, and my will to work, so I'm calling it a sick day.

One line, under 200 characters. Half believable (any parent of a toddler has
lived this), fresh (no fever, no dog, no dead grandmother), and the punch —
"my will to work" — lands at the end, exactly like a real person texting
their boss.

## How it works

`main.py` is fully deterministic: no network, no randomness, no files read
outside this repo. It writes the single line above to `/output/entry.txt`
(override with the `ENTRY_OUTPUT` environment variable for local testing)
and asserts the text is 1–200 characters, a single line, and not only
whitespace.

```sh
python3 main.py
```
