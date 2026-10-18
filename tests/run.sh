#!/usr/bin/env bash
# Teste do varrer_historico.py com dados de exemplo. Uso: tests/run.sh
set -e
cd "$(dirname "$0")/.."
T=$(mktemp -d)
python3 scripts/varrer_historico.py --claude tests/fixtures/claude --codex tests/fixtures/codex \
  --skills tests/fixtures/skills --dias 36500 --saida "$T/r" > "$T/out.txt"
ok=0; f=0
chk(){ if grep -q -- "$2" "$T/$1"; then ok=$((ok+1)); else f=$((f+1)); echo "FALHOU: $1 sem '$2'"; fi; }
chk out.txt "atrito 2/3"
chk out.txt "skills nunca usadas 1/2"
chk r.md "Claude 1 · Codex 1"
chk r.md "- parada"
chk r.md "- usada: 2"
chk r.md "codex:shell: 1"
chk r.html "Relatório da faxina"
! grep -q "system-reminder" "$T/r.md" && ok=$((ok+1)) || { f=$((f+1)); echo "FALHOU: texto de sistema contado"; }
echo "$ok ok, $f falhas"; rm -rf "$T"; [ $f -eq 0 ]
