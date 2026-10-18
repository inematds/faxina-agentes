# Clean up your Claude and Codex setup

[![Setup cleanup](guia/assets/banner-en.jpg)](https://inematds.github.io/faxina-agentes/guia/en/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## What it is

This is a free guide to cleaning up the setup of anyone who uses Claude Code and Codex. Over time, duplicate instruction files, downloaded but unused skills, old memories, and conflicting rules pile up; they all enter the context before the first request, and the agent starts ignoring rules and using more tokens. The guide covers an audit with a prompt, a script that reads your history, one AGENTS.md, folders for each business, playbooks, and a three-question filter. All you need is Claude Code or Codex installed and Python 3.

## 📖 User guide

Complete guide (landing page + walkthrough): **https://inematds.github.io/faxina-agentes/guia/en/**

## 🎬 Videos

- Explainer 16:9: https://github.com/inematds/faxina-agentes/releases/download/video-v1.0.0/faxina-agentes-16x9.mp4
- Reel 9:16: https://github.com/inematds/faxina-agentes/releases/download/video-v1.0.0/faxina-agentes-reel.mp4
- Players in the guide: https://inematds.github.io/faxina-agentes/guia/en/#video

## The 6 steps

1. **Audit with a prompt** — say what to audit, what to compare it against, and what criteria to use: [`prompts/auditoria.en.md`](prompts/auditoria.en.md).
2. **A script reads your history** — counts friction in your messages and lists unused skills, no API: `python3 scripts/varrer_historico.py --dias 60`.
3. **One AGENTS.md as a control tower** — shared rules go in one file; CLAUDE.md only points to it (`@AGENTS.md`): [`modelos/AGENTS-raiz.md`](modelos/AGENTS-raiz.md).
4. **One folder per business or client** — each with its own AGENTS.md: [`modelos/AGENTS-pasta.md`](modelos/AGENTS-pasta.md).
5. **Playbooks instead of another skill** — your process, dictated and written down: [`modelos/playbook-modelo.md`](modelos/playbook-modelo.md).
6. **Scheduled cleanup** — the same audit every week; automatic cleanup is limited to low-risk items.

**Filter before installing anything new:** Is it useful for almost every task? Is it only useful sometimes (then keep it local)? Who cleans it up?

## Run the script

```bash
git clone https://github.com/inematds/faxina-agentes
cd faxina-agentes
python3 scripts/varrer_historico.py --dias 60      # generates relatorio-faxina.md and relatorio-faxina.html
tests/run.sh                                        # test with sample data
```

Options: `--claude <folder>` (default `~/.claude/projects`), `--codex <folder>` (default `~/.codex/sessions`),
`--skills <folder>` (repeatable; defaults `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`), `--projeto <folder>`, `--saida <name>`.
The script only reads local files: it does not call an API, send anything, or delete anything.

## License

MIT. From [INEMA.CLUB](https://inema.club).
