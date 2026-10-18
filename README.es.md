# Limpieza de la configuración de Claude y Codex

[![Limpieza de la configuración](guia/assets/banner-es.jpg)](https://inematds.github.io/faxina-agentes/guia/es/)

**🇧🇷 [Português](README.md) · 🇺🇸 [English](README.en.md) · 🇪🇸 [Español](README.es.md)**

## Qué es

Esta es una guía gratuita para ordenar la configuración de quienes usan Claude Code y Codex. Con el tiempo, se acumulan archivos de instrucciones repetidos, skills descargadas que nunca se usan, memorias antiguas y reglas contradictorias; todo eso entra en el contexto antes de la primera solicitud y el agente empieza a ignorar reglas y a consumir más. La guía muestra una auditoría hecha con un prompt, un script que lee tu historial, un único AGENTS.md, carpetas por negocio, playbooks y un filtro de tres preguntas. Para usarla, solo necesitas tener Claude Code o Codex instalado y Python 3.

## 📖 Guía de uso

Guía completa (landing + paso a paso): **https://inematds.github.io/faxina-agentes/guia/es/**

## 🎬 Videos

- Explicativo 16:9: https://github.com/inematds/faxina-agentes/releases/download/video-v1.0.0/faxina-agentes-16x9.mp4
- Reel 9:16: https://github.com/inematds/faxina-agentes/releases/download/video-v1.0.0/faxina-agentes-reel.mp4
- Reproductores en la guía: https://inematds.github.io/faxina-agentes/guia/es/#video

## Los 6 pasos

1. **Auditoría con un prompt** — indica qué auditar, con qué compararlo y qué criterio usar: [`prompts/auditoria.es.md`](prompts/auditoria.es.md).
2. **Un script lee el historial** — cuenta señales de fricción en tus mensajes y skills que nunca se usaron, sin API: `python3 scripts/varrer_historico.py --dias 60`.
3. **Un AGENTS.md como torre de control** — lo común queda en un solo archivo; CLAUDE.md solo apunta a él (`@AGENTS.md`): [`modelos/AGENTS-raiz.md`](modelos/AGENTS-raiz.md).
4. **Una carpeta por negocio o cliente** — cada una con su propio AGENTS.md: [`modelos/AGENTS-pasta.md`](modelos/AGENTS-pasta.md).
5. **Playbooks en lugar de otra skill más** — tu proceso, dictado y documentado: [`modelos/playbook-modelo.md`](modelos/playbook-modelo.md).
6. **Limpieza programada** — la misma auditoría cada semana; de forma automática, solo lo de bajo riesgo.

**Filtro antes de instalar algo nuevo:** ¿sirve para casi todas las tareas? ¿Solo es útil a veces (entonces queda local)? ¿Quién lo limpia?

## Ejecutar el script

```bash
git clone https://github.com/inematds/faxina-agentes
cd faxina-agentes
python3 scripts/varrer_historico.py --dias 60      # genera relatorio-faxina.md y relatorio-faxina.html
tests/run.sh                                        # prueba con datos de ejemplo
```

Opciones: `--claude <pasta>` (por defecto `~/.claude/projects`), `--codex <pasta>` (por defecto `~/.codex/sessions`),
`--skills <pasta>` (repetible; por defecto `~/.claude/skills`, `~/.agents/skills`, `~/.codex/skills`), `--projeto <pasta>`, `--saida <nome>`.
El script solo lee archivos locales: no llama a ninguna API, no envía nada ni borra nada.

## Licencia

MIT. De [INEMA.CLUB](https://inema.club).
