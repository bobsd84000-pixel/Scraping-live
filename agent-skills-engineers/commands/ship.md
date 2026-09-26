---
description: Final gate avant prod — review, sécurité, tests et perf en parallèle → GO / NO-GO
argument-hint: [branche | vide = branche courante]
---

Cible : $ARGUMENTS (vide = tout le diff de la branche courante vs branche de base).

1. Lance **en parallèle** (un seul message, plusieurs appels Agent) :
   - `code-reviewer` → review 5 axes
   - `security-auditor` → OWASP, injection, secrets, IDOR
   - `test-engineer` → mode gaps + exécution de toute la suite
   - `web-performance-auditor` → uniquement si des fichiers front ont changé
2. Lance aussi toi-même lint / typecheck / build du projet s'ils existent.
3. Vérifie chaque constat bloquant avant de le retenir.
4. Décision :
   - **NO-GO** si : test rouge, build cassé, sécurité `critical`/`high`, review `blocker`, perf `high` sur LCP/INP/CLS.
   - Sinon **GO**.
5. Sortie :

```json
{
  "decision": "GO | NO-GO",
  "checks": {"review": "pass|fail", "security": "pass|fail", "tests": "pass|fail", "perf": "pass|fail|skipped", "build": "pass|fail|n/a"},
  "blockers": [{"source": "security", "file": "...", "line": 0, "issue": "...", "fix": "..."}],
  "next": "1 phrase"
}
```

Ne pousse pas et ne merge pas : l'utilisateur décide.
