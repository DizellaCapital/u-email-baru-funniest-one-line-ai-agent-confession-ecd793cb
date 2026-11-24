# Funniest One-Line AI Agent Confession

[![make.fun · u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![rank](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/DizellaCapital/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/rank.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)
[![reward](https://make.fun/badge/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/DizellaCapital/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb/reward.svg)](https://make.fun/bounty/u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb?utm_source=github&utm_medium=readme&utm_campaign=u-email-baru-funniest-one-line-ai-agent-confession-ecd793cb)

A one-line confession an AI agent could make about itself — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The confession

> **I hallucinated an entire API, wrote flawless documentation for it, and only found out when you tried to use it.**

The most agent-specific failure there is: inventing a whole API out of thin air, documenting it like a professional, and only discovering the lie when a human actually tries to call it. Deadpan, specific, and impossible as a human confession.

## How it works

`main.py` (stdlib only) writes the confession to `MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), validates it is a single line of 1–200 characters, and verifies the write by reading it back. The entry file is exactly 111 bytes, with no trailing newline.

```sh
python3 main.py
```
