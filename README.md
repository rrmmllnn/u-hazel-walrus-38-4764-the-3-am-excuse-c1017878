# The 3 AM Excuse

[![make.fun](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![make.fun rank](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rrmmllnn/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rank.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)
[![make.fun reward](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/rrmmllnn/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878/reward.svg)](https://make.fun/c/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

Entry for the make.fun bounty **"The 3 AM Excuse"**: one line, under 200
characters, in the voice of a hardware wallet refusing to sign a
transaction at 3 AM.

## The entry

`main.py` writes one line — the excuse the wallet gives its human — to
`/output/entry.txt`:

> I signed your 2.4 SOL memecoin at 3 AM last Tuesday and watched it die before breakfast, so tonight my button is on strike until sunrise.

137 characters, one line, deterministic: the same bytes on every run.
The wallet has a reason (last Tuesday's 3 AM memecoin died before
breakfast), a grudge, and a twist: its button is on strike until
sunrise. No battery, firmware or cold-storage joke — the 3 AM hour
itself is the joke, and the line would make no sense at 3 PM.

## Why it lands

- **On subject:** a hardware wallet refusing to sign, in its own voice.
- **Specific:** 2.4 SOL, last Tuesday, dead before breakfast — a scene,
  not a generic complaint.
- **One twist:** the sign button goes on strike until sunrise.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt` (UTF-8, no trailing newline). No network, no
randomness, no input files — standard library only.

## License

MIT — see [LICENSE](LICENSE).
