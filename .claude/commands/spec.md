---
description: Spec-driven dev — transforme une demande en PRD court puis en plan atomique
argument-hint: <description de la feature>
---

Demande : $ARGUMENTS

Tu joues le rôle **spec-driven-dev**. Aucune ligne de code de production à cette étape.

1. Explore le projet (structure, stack, conventions, tests existants) juste assez pour spécifier.
2. Si un point bloque réellement la spec (choix produit, donnée inconnue), pose au max 3 questions avec AskUserQuestion. Sinon, décide et note l'hypothèse.
3. Écris `.specs/<slug>/spec.md` :
   - **Objectif** (1-2 phrases)
   - **Utilisateurs / cas d'usage**
   - **Périmètre** : inclus / exclus
   - **Critères d'acceptation** testables (Given / When / Then)
   - **Contraintes** : sécurité, perf, compatibilité
   - **Hypothèses** prises
4. Enchaîne sur le plan atomique (même format que `/plan`) dans `.specs/<slug>/plan.md`.
5. Réponds avec : chemin des fichiers + liste des tâches (1 ligne chacune). Prochaine étape : `/build` ou `/build auto`.
