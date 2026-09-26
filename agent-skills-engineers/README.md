# Agent Skills Engineers

Kit indépendant pour Claude Code : 4 engineers et 7 commandes. Il n'est lié à aucun projet.

## Installation
```bash
./install.sh              # global : actif dans tous les projets
./install.sh ~/mon-projet # un seul projet
```
Ensuite, redémarre Claude Code.

## Workflow
| Commande | Rôle | Sortie |
|---|---|---|
| `/spec <feature>` | spec-driven-dev | `.specs/<slug>/spec.md` + `plan.md` |
| `/plan` | planning-task-breakdown | Tâches numérotées |
| `/build` · `/build auto` | incremental-implementation (TDD) | 1 slice = 1 commit · tout le plan après 1 validation |
| `/test` | test-engineer | Trous de couverture, Prove-It |
| `/review` | code-reviewer | 5 axes → APPROVE / CHANGES |
| `/webperf` | web-performance-auditor | LCP, INP, CLS → PASS / FAIL |
| `/ship` | les 4 en parallèle | GO / NO-GO |

Exemple : `/spec Dashboard temps réel avec graphiques, dark mode, export CSV` → `/build auto` → `/ship`
