# Goal — faxina-agentes

- **Início:** 2026-10-18 · **Agente:** Claude Code (Opus 5.5)
- **Fonte:** vídeo https://www.youtube.com/watch?v=eXoBC1TY8m4 ("Your Claude + Codex Setup Is a Mess") — só inspiração; conteúdo, roteiro e arte próprios, sem citar o autor.
- **Pedido do Nei:** repo novo + explicavideo + r7e, muita apresentação visual; publicar no lives4, portal, Telegram INEMA.DEV e mandar no bot v3.
- **Tetos:** render/transcrição com `systemd-run --user --scope -p MemoryMax=16G -p MemorySwapMax=0`; HeyGen com `DISPLAY=:99`.

## Resultado
Repo `inematds/faxina-agentes` com guia PT/EN/ES (faxina do setup Claude + Codex: auditoria por prompt, um AGENTS.md torre de controle,
pastas com AGENTS.md aninhado, playbooks, filtro de 3 perguntas, faxina agendada) + prompt de auditoria + modelos de AGENTS.md + player;
explicavideo v2 PT 16:9 (modo aula, ilustrações próprias + shots animados) e reel r7e; publicados no lives4, portal, INEMA.DEV, bot v3.

## Critérios de pronto (verificáveis)

**Função**
- [ ] `ls ~/projetos/output/explica-faxina-agentes/v2/final/*-pt.mp4` → existe; duração 150–300 s
- [ ] `build_block.py 1 --strict` → 0 warnings; `validar_visual.py` → OK
- [ ] frame 0 mostra a capa do ganho com texto legível (recorte 3×)
- [ ] `ls ~/projetos/reel7etapas/edicoes/*faxina*/build/video.mp4` → existe; validar → aprovado
- [ ] `curl -sI https://inematds.github.io/faxina-agentes/guia/` (e `/guia/en/`, `/guia/es/`) → 200
- [ ] YouTube lives4: 2 ids (16:9 + reel) gravados em progress.md; links ao inemaytbot com o canal
- [ ] portal: `grep -n faxina-agentes ~/projetos/portal/src/...` → card do projeto + 2 vídeos; push no origin
- [ ] Telegram INEMA.DEV: id do tópico em progress.md + entrada no MENU
- [ ] bot v3: os 2 arquivos, legenda sem link

**Regressão**
- [ ] guia: `scrollWidth - innerWidth` = 0 de 390 a 1920 px, por HTTP; imagens `naturalWidth > 0` em PT/EN/ES

**Limite**
- [ ] nenhuma API além das liberadas (GitHub, Telegram, HeyGen leitura); avatar só pelo estúdio
- [ ] nenhum MP4 commitado; autor dos commits = inematds
- [ ] imagens sem texto desenhado, exceto capa/hero (texto conferido); robô (se houver) estilo Optimus com visor preto
- [ ] sem nome do autor da fonte em fala, tela, descrição ou repo
