---
description: Découpe une spec en tâches atomiques numérotées
argument-hint: [chemin spec.md ou slug]
---

Cible : $ARGUMENTS (si vide : la spec la plus récente dans `.specs/`).

Tu joues le rôle **planning-task-breakdown**.

1. Lis la spec et le code concerné.
2. Découpe en tâches **atomiques** : chaque tâche = 1 slice verticale livrable, testable seule, 1 commit, < ~200 lignes de diff.
3. Ordonne par dépendances ; la 1re tâche livre le chemin nominal le plus simple.
4. Écris `.specs/<slug>/plan.md` au format :

```markdown
- [ ] T1 — <titre court>
  - Fichiers : ...
  - Test d'abord : <comportement à prouver>
  - Critère de fin : <vérifiable>
  - Dépend de : —
```

5. Dernière tâche toujours : `/ship`.
6. Réponds avec la liste numérotée uniquement.
