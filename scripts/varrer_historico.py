#!/usr/bin/env python3
"""varrer_historico.py — lê o histórico do Claude Code e do Codex na SUA máquina e mostra onde está a bagunça.

Só leitura. Não chama nenhuma API, não manda nada para fora, não apaga nada.

O que ele conta:
  - mensagens suas com sinais de atrito ("não foi isso", "de novo", "you ignored"...)
  - quais skills existem instaladas e quantas vezes cada uma foi usada (as nunca usadas = candidatas a sair)
  - quais ferramentas o agente mais chama
  - o tamanho dos arquivos de instrução que entram em toda sessão (CLAUDE.md, AGENTS.md, GEMINI.md)

Uso:
  python3 scripts/varrer_historico.py                     # usa ~/.claude e ~/.codex
  python3 scripts/varrer_historico.py --dias 90 --saida relatorio
  python3 scripts/varrer_historico.py --claude <pasta> --codex <pasta> --skills <pasta> [--skills <pasta>]

Saída: <saida>.md e <saida>.html (abra no navegador).
"""
import argparse, collections, datetime as dt, html, json, os, pathlib, re, sys

ATRITO = [
    r"n[ãa]o (foi|era) isso", r"de novo", r"j[áa] (te )?(disse|falei|pedi)", r"errad[oa]", r"n[ãa]o funcion",
    r"para de", r"pare de", r"voc[êe] (esqueceu|ignorou)", r"eu pedi", r"n[ãa]o pedi", r"refaz",
    r"that'?s not what", r"you ignored", r"i (already )?told you", r"again\b", r"wrong", r"stop doing",
    r"no es eso", r"otra vez", r"te dije",
]
ATRITO_RE = re.compile("|".join(ATRITO), re.I)
INSTRUCOES = ("CLAUDE.md", "AGENTS.md", "GEMINI.md", "soul.md", "SOUL.md")


def ler_jsonl(p):
    try:
        with open(p, encoding="utf-8", errors="replace") as f:
            for linha in f:
                try:
                    yield json.loads(linha)
                except ValueError:
                    continue
    except OSError:
        return


def texto_de(conteudo):
    if isinstance(conteudo, str):
        return conteudo
    if isinstance(conteudo, list):
        return " ".join(c.get("text", "") for c in conteudo if isinstance(c, dict) and c.get("type") in ("text", "input_text"))
    return ""


def eh_mensagem_humana(t):
    # descarta textos de sistema injetados (instruções, lembretes, resultados de comando)
    t = t.strip()
    return bool(t) and not t.startswith(("<", "#", "[Request", "Caveat:")) and len(t) < 4000


def recentes(raiz, dias):
    limite = dt.datetime.now().timestamp() - dias * 86400
    for p in pathlib.Path(raiz).expanduser().rglob("*.jsonl"):
        try:
            if p.stat().st_mtime >= limite:
                yield p
        except OSError:
            continue


def varrer_claude(raiz, dias, c):
    for p in recentes(raiz, dias):
        c["sessoes_claude"] += 1
        for ev in ler_jsonl(p):
            msg = ev.get("message") or {}
            if ev.get("type") == "user" and msg.get("role") == "user":
                t = texto_de(msg.get("content"))
                if eh_mensagem_humana(t):
                    c["msgs"] += 1
                    if ATRITO_RE.search(t):
                        c["atrito"].append(("claude", t[:160].replace("\n", " ")))
            if ev.get("type") == "assistant":
                for it in msg.get("content") or []:
                    if isinstance(it, dict) and it.get("type") == "tool_use":
                        nome = it.get("name", "?")
                        c["ferramentas"][nome] += 1
                        if nome == "Skill":
                            s = (it.get("input") or {}).get("skill", "")
                            c["skills_usadas"][s.split(":")[-1]] += 1


SKILL_RE = re.compile(r"skills/([A-Za-z0-9_.-]+)/SKILL\.md")


def varrer_codex(raiz, dias, c):
    for p in recentes(raiz, dias):
        c["sessoes_codex"] += 1
        for ev in ler_jsonl(p):
            pl = ev.get("payload") or {}
            if pl.get("type") == "message" and pl.get("role") == "user":
                t = texto_de(pl.get("content"))
                if eh_mensagem_humana(t):
                    c["msgs"] += 1
                    if ATRITO_RE.search(t):
                        c["atrito"].append(("codex", t[:160].replace("\n", " ")))
            if pl.get("type") in ("function_call", "custom_tool_call"):
                c["ferramentas"]["codex:" + pl.get("name", "?")] += 1
                for s in SKILL_RE.findall(str(pl.get("arguments") or pl.get("input") or "")):
                    c["skills_usadas"][s] += 1


def skills_instaladas(pastas):
    out = {}
    for pasta in pastas:
        base = pathlib.Path(pasta).expanduser()
        if not base.is_dir():
            continue
        for sk in base.glob("*/SKILL.md"):
            out.setdefault(sk.parent.name, str(sk.parent))
    return out


def instrucoes(raizes):
    achados = []
    for r in raizes:
        base = pathlib.Path(r).expanduser()
        for nome in INSTRUCOES:
            p = base / nome
            if p.is_file():
                achados.append((str(p), sum(1 for _ in open(p, errors="replace")), p.stat().st_size))
    return achados


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--claude", default="~/.claude/projects")
    ap.add_argument("--codex", default="~/.codex/sessions")
    ap.add_argument("--skills", action="append", help="pasta de skills (pode repetir)")
    ap.add_argument("--projeto", action="append", default=[], help="pasta de projeto para medir CLAUDE.md/AGENTS.md")
    ap.add_argument("--dias", type=int, default=60)
    ap.add_argument("--saida", default="relatorio-faxina")
    a = ap.parse_args()
    pastas_sk = a.skills or ["~/.claude/skills", "~/.agents/skills", "~/.codex/skills"]

    c = collections.defaultdict(int)
    c.update(atrito=[], ferramentas=collections.Counter(), skills_usadas=collections.Counter())
    varrer_claude(a.claude, a.dias, c)
    varrer_codex(a.codex, a.dias, c)
    inst = skills_instaladas(pastas_sk)
    nunca = sorted(n for n in inst if c["skills_usadas"][n] == 0)
    instr = instrucoes(["~/.claude", "~/.codex", "~", *a.projeto])
    linhas_instr = sum(l for _, l, _ in instr)

    md = [f"# Relatório da faxina — últimos {a.dias} dias", "",
          f"- Sessões lidas: Claude {c['sessoes_claude']} · Codex {c['sessoes_codex']}",
          f"- Mensagens suas: {c['msgs']} · com sinal de atrito: {len(c['atrito'])}",
          f"- Skills instaladas: {len(inst)} · nunca usadas no período: {len(nunca)}",
          f"- Arquivos de instrução globais: {len(instr)} ({linhas_instr} linhas entram antes do 1º prompt)", "",
          "## Arquivos de instrução", *[f"- `{p}` — {l} linhas" for p, l, _ in instr], "",
          "## Skills nunca usadas (candidatas a sair ou a virar uma linha no AGENTS.md)", *([f"- {n}" for n in nunca] or ["- nenhuma"]), "",
          "## Skills mais usadas", *([f"- {n}: {k}" for n, k in c["skills_usadas"].most_common(15)] or ["- nenhuma"]), "",
          "## Ferramentas mais chamadas", *[f"- {n}: {k}" for n, k in c["ferramentas"].most_common(15)], "",
          "## Mensagens com atrito (amostra)", *([f"- [{o}] {t}" for o, t in c["atrito"][-25:]] or ["- nenhuma"]), ""]
    pathlib.Path(a.saida + ".md").write_text("\n".join(md), encoding="utf-8")

    def card(titulo, valor, sub):
        return f'<div class="c"><b>{valor}</b><span>{html.escape(titulo)}</span><small>{html.escape(sub)}</small></div>'
    corpo = "".join(f"<li>{html.escape(l[2:])}</li>" if l.startswith("- ") else
                    (f"<h2>{html.escape(l[3:])}</h2>" if l.startswith("## ") else "") for l in md[7:])
    pag = f"""<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Relatório da faxina</title><style>
:root{{--bg:#0c0c10;--card:#16161e;--line:#272730;--txt:#e9e9ee;--mut:#9a9aa6;--amb:#FACC15}}
body{{margin:0;background:var(--bg);color:var(--txt);font:16px/1.6 Inter,system-ui,sans-serif;padding:24px 16px}}
main{{max-width:960px;margin:auto}}h1,h2{{font-family:Sora,system-ui,sans-serif}}h2{{margin-top:32px;border-bottom:1px solid var(--line);padding-bottom:6px}}
.g{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}}
.c{{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;display:flex;flex-direction:column}}
.c b{{font:700 2rem Sora,sans-serif;color:var(--amb)}}.c small{{color:var(--mut)}}li{{margin:2px 0;word-break:break-word}}</style>
<main><h1>Relatório da faxina — últimos {a.dias} dias</h1><div class="g">
{card("mensagens com atrito", len(c["atrito"]), f"de {c['msgs']} mensagens suas")}
{card("skills nunca usadas", len(nunca), f"de {len(inst)} instaladas")}
{card("linhas de instrução", linhas_instr, f"em {len(instr)} arquivos globais")}
{card("sessões lidas", c["sessoes_claude"] + c["sessoes_codex"], f"Claude {c['sessoes_claude']} · Codex {c['sessoes_codex']}")}
</div><ul>{corpo}</ul></main></html>"""
    pathlib.Path(a.saida + ".html").write_text(pag, encoding="utf-8")
    print(f"ok: {a.saida}.md e {a.saida}.html | atrito {len(c['atrito'])}/{c['msgs']} | skills nunca usadas {len(nunca)}/{len(inst)} | instruções {linhas_instr} linhas")


if __name__ == "__main__":
    sys.exit(main())
