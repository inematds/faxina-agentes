# Audit prompt (paste into Claude Code or Codex)

Use in a terminal opened in the folder where you work. The agent only **reads** and **proposes**: nothing is deleted without your OK.

```text
I use Claude Code and Codex. Audit my setup in both.

WHAT TO AUDIT
- instruction files: CLAUDE.md, AGENTS.md, GEMINI.md, and similar (global and per project)
- skills, rules, memory, settings, hooks, plugins, MCP, and connected tools
- agents and subagents, scheduled tasks, and each project that works as its own system

WHAT TO COMPARE IT AGAINST
- my actual usage: run `python3 scripts/varrer_historico.py --dias 60` (or write a similar script)
  to count signs of friction in my messages and the skills/tools I’ve never called.
  Don’t read entire conversations: use the script.

CRITERIA
For each item, say:
1. what works and should stay;
2. what is dead weight (unused, old, duplicated) and can be removed;
3. what is missing;
4. which rules conflict or exist in one tool but not the other (Claude × Codex);
5. which configuration, automation, or project is getting in my way instead of helping.

DELIVERABLE
- one HTML page I can read in a browser, with a score from 0 to 10 for each area,
  the 10 most important changes, and evidence (file and line) and risk for each;
- separate “low risk, I can do now” from “needs my decision”;
- don’t change anything yet. Wait for my OK.
```

## After the report

1. Approve only the **low-risk** list (dead hook, temporary file, skill unused for months).
2. Read the list that needs a decision carefully; cross out anything you want to keep.
3. Schedule the same audit **every week** (a scheduled Codex task or `/schedule` in Claude Code),
   with this rule: automatically clean up only low-risk items; put everything else on a list for you.
