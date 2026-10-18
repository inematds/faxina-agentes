# Faxina no setup do Claude e do Codex

[![Faxina no setup](guia/assets/banner.jpg)](https://inematds.github.io/faxina-agentes/guia/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## O que é

Este é um guia grátis para arrumar o setup de quem usa o Claude Code e o Codex. Com o tempo, juntam-se arquivos de instrução repetidos, skills baixadas e nunca usadas, memórias velhas e regras que se contradizem; tudo isso entra no contexto antes do primeiro pedido e o agente passa a ignorar regras e gastar mais. O guia mostra uma auditoria feita com um prompt, um script que lê o seu histórico, um AGENTS.md único, pastas por negócio, playbooks e um filtro de três perguntas. Para usar, basta ter o Claude Code ou o Codex instalado e Python 3.

## 📖 Guia de uso

Guia completo (landing + passo a passo): **https://inematds.github.io/faxina-agentes/guia/**

## 🎬 Vídeos

- Explicativo 16:9: https://github.com/inematds/faxina-agentes/releases/download/video-v1.0.0/faxina-agentes-16x9.mp4
- Reel 9:16: https://github.com/inematds/faxina-agentes/releases/download/video-v1.0.0/faxina-agentes-reel.mp4
- Players no guia: https://inematds.github.io/faxina-agentes/guia/#video

## Os 6 passos

1. **Auditoria com um prompt** — diga o que auditar, contra o quê e com que critério: [`prompts/auditoria.md`](prompts/auditoria.md).
2. **Um script lê o histórico** — conta atrito nas suas mensagens e skills nunca usadas, sem API: `python3 scripts/varrer_historico.py --dias 60`.
3. **Um AGENTS.md como torre de controle** — o comum fica num arquivo só; o CLAUDE.md só aponta (`@AGENTS.md`): [`modelos/AGENTS-raiz.md`](modelos/AGENTS-raiz.md).
4. **Uma pasta por negócio ou cliente** — cada uma com o seu AGENTS.md: [`modelos/AGENTS-pasta.md`](modelos/AGENTS-pasta.md).
5. **Playbooks no lugar de mais uma skill** — o seu processo, ditado e escrito: [`modelos/playbook-modelo.md`](modelos/playbook-modelo.md).
6. **Faxina agendada** — a mesma auditoria toda semana; sozinho, só o baixo risco.

**Filtro antes de instalar algo novo:** serve para quase toda tarefa? É útil só às vezes (então fica local)? Quem limpa?

## Rodar o script

```bash
git clone https://github.com/inematds/faxina-agentes
cd faxina-agentes
python3 scripts/varrer_historico.py --dias 60      # gera relatorio-faxina.md e relatorio-faxina.html
tests/run.sh                                        # teste com dados de exemplo
```

Opções: `--claude <pasta>` (padrão `~/.claude/projects`), `--codex <pasta>` (padrão `~/.codex/sessions`),
`--skills <pasta>` (repetível; padrão `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`), `--projeto <pasta>`, `--saida <nome>`.
O script só lê arquivos locais: não chama API, não envia nada e não apaga nada.

## Licença

MIT. Do [INEMA.CLUB](https://inema.club).
