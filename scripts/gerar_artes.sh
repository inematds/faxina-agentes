#!/usr/bin/env bash
# Gera capa do catálogo + 6 banners do guia (live e grade × PT/EN/ES) pelo Codex. Uso: scripts/gerar_artes.sh
cd "$(dirname "$0")/.."
R=$PWD; G=~/.claude/skills/projetos-landing-guia/assets/gerar-banner.sh
mkdir -p logs-tmp
node ~/.claude/skills/capa-inema/assets/gerar-capa.cjs --repo "$R" --title "Faxina no setup" --cat "Agentes" \
  --save-raw "$R/guia/assets/hero.png" --gerador auto > logs-tmp/capa.log 2>&1 &
SIDES="escritório moderno organizado: uma mulher de camisa azul-clara e um robô humanoide industrial estilo Tesla Optimus, cinza fosco, cabeça com visor preto, arrumando pastas coloridas numa estante limpa; ao fundo, uma pilha de papéis sendo varrida"
b(){ bash $G --repo "$R" --sides "$SIDES" --selo "faxina-agentes" "$@"; }
b --title "FAXINA NO SETUP" --destaque "SETUP" --sub "Claude + Codex: o agente obedece e gasta menos" \
  --line "auditoria com um prompt, um AGENTS.md e playbooks" \
  --tiles "Auditoria,Histórico,Torre de controle,Pastas,Playbooks,Filtro" > logs-tmp/b-pt.log 2>&1 &
b --title "FAXINA NO SETUP" --destaque "SETUP" --sub "Claude + Codex: o agente obedece e gasta menos tokens" \
  --line "auditoria com um prompt, um AGENTS.md e playbooks" \
  --tiles "Auditoria,Histórico,Torre de controle,Pastas,Playbooks,Filtro" --estilo grade --saida banner-grade > logs-tmp/g-pt.log 2>&1 &
wait
b --lang en --saida banner-en --title "CLEAN UP YOUR SETUP" --destaque "SETUP" --sub "Claude + Codex: your agent obeys and spends less" \
  --line "one audit prompt, one AGENTS.md and playbooks" \
  --tiles "Audit,History,Control tower,Folders,Playbooks,Filter" > logs-tmp/b-en.log 2>&1 &
b --lang en --saida banner-grade-en --estilo grade --title "CLEAN UP YOUR SETUP" --destaque "SETUP" --sub "Claude + Codex: your agent obeys and spends fewer tokens" \
  --line "one audit prompt, one AGENTS.md and playbooks" \
  --tiles "Audit,History,Control tower,Folders,Playbooks,Filter" > logs-tmp/g-en.log 2>&1 &
b --lang es --saida banner-es --title "LIMPIEZA DEL SETUP" --destaque "SETUP" --sub "Claude + Codex: tu agente obedece y gasta menos" \
  --line "una auditoría con un prompt, un AGENTS.md y playbooks" \
  --tiles "Auditoría,Historial,Torre de control,Carpetas,Playbooks,Filtro" > logs-tmp/b-es.log 2>&1 &
wait
b --lang es --saida banner-grade-es --estilo grade --title "LIMPIEZA DEL SETUP" --destaque "SETUP" --sub "Claude + Codex: tu agente obedece y gasta menos tokens" \
  --line "una auditoría con un prompt, un AGENTS.md y playbooks" \
  --tiles "Auditoría,Historial,Torre de control,Carpetas,Playbooks,Filtro" > logs-tmp/g-es.log 2>&1
ls -la guia/assets capa
echo FIM_ARTES
