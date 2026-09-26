---
description: Implémente le plan slice par slice en TDD (ajoute "auto" pour tout enchaîner après 1 validation)
argument-hint: [auto] [n° de tâche]
---

Arguments : $ARGUMENTS

Tu joues le rôle **incremental-implementation**. Source de vérité : le `plan.md` le plus récent dans `.specs/`.

## Boucle par tâche (une seule à la fois)
1. **Test d'abord** : délègue à l'agent `test-engineer` (mode TDD). Le test doit échouer pour la bonne raison.
2. **Code minimal** pour le faire passer. Respecte les conventions existantes, pas de refactor hors tâche.
3. **Vérifie** : lance la suite de tests + lint/typecheck du projet. Tout vert obligatoire.
4. **Review rapide** : délègue à `code-reviewer` sur le diff de la tâche. Corrige les `blocker`/`major`.
5. **Commit atomique** : `<type>: <quoi>` (feat/fix/test/refactor), uniquement les fichiers de la tâche.
6. Coche la tâche dans `plan.md`.

## Mode
- **Sans `auto`** : fais UNE tâche (la suivante non cochée, ou le n° donné), puis arrête-toi et résume.
- **Avec `auto`** : montre le plan, demande UNE validation (AskUserQuestion), puis enchaîne toutes les tâches sans t'arrêter. Stop uniquement si : test impossible à faire passer après 3 essais, décision produit nécessaire, ou action destructive. À la fin, lance `/ship`.

Ne pousse jamais sans que l'utilisateur l'ait demandé.
