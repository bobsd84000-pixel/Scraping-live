---
description: Code review 5 axes (correctness, readability, architecture, security, perf)
argument-hint: [fichier | branche | vide = diff courant]
---

Cible : $ARGUMENTS (vide = diff courant vs branche de base, commits + non commités).

Délègue à l'agent `code-reviewer` avec la cible.

Ensuite :
1. Vérifie toi-même chaque constat `blocker`/`major` (relis le code). Écarte ceux qui ne tiennent pas.
2. Affiche les constats retenus, du plus grave au moins grave, format : `fichier:ligne — problème → fix`.
3. Verdict final : **APPROVE** ou **CHANGES REQUESTED**.
4. Ne corrige rien sauf si l'utilisateur le demande.
