# Prompt da auditoria (cole no Claude Code ou no Codex)

Use num terminal aberto na pasta onde você trabalha. O agente só **lê** e **propõe**: nada é apagado sem o seu OK.

```text
Eu uso o Claude Code e o Codex. Faça uma auditoria do meu setup nos dois.

O QUE AUDITAR
- arquivos de instrução: CLAUDE.md, AGENTS.md, GEMINI.md e parecidos (globais e por projeto)
- skills, regras, memória, configurações (settings), hooks, plugins, MCP e ferramentas conectadas
- agentes e subagentes, tarefas agendadas e cada projeto que funciona como um sistema próprio

CONTRA O QUÊ
- o meu uso real: rode `python3 scripts/varrer_historico.py --dias 60` (ou escreva um script parecido)
  para contar sinais de atrito nas minhas mensagens e as skills/ferramentas que eu nunca chamei.
  Não leia as conversas inteiras: use o script.

COM QUE CRITÉRIO
Para cada item, diga:
1. o que funciona e deve ficar;
2. o que é peso morto (não usado, velho, duplicado) e pode sair;
3. o que está faltando;
4. que regras se contradizem ou existem num e não no outro (Claude × Codex);
5. que configuração, automação ou projeto está me atrapalhando em vez de ajudar.

COMO ENTREGAR
- uma página HTML que eu leia no navegador, com nota de 0 a 10 por área,
  as 10 mudanças mais importantes e, para cada uma, a prova (arquivo e linha) e o risco;
- separe "baixo risco, posso fazer agora" de "precisa da sua decisão";
- não mude nada ainda. Espere o meu OK.
```

## Depois do relatório

1. Aprove só a lista de **baixo risco** (hook morto, arquivo temporário, skill parada há meses).
2. Leia a lista que pede decisão com calma; risque o que quer manter.
3. Agende a mesma auditoria **toda semana** (tarefa agendada do Codex ou `/schedule` no Claude Code),
   com a regra: limpar sozinho só o que é de baixo risco; o resto vira lista para você.
