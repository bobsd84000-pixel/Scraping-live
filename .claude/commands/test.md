---
description: Analyse la couverture, comble les trous, ou prouve un bug (Prove-It)
argument-hint: [fichier | "bug: <description>"]
---

Cible : $ARGUMENTS

Délègue à l'agent `test-engineer` :
- Si l'argument commence par `bug:` → mode **Prove-It** : test rouge qui reproduit le bug, sans le corriger.
- Si un fichier/dossier est donné → mode **gaps** sur cette cible.
- Si vide → mode **gaps** sur les fichiers modifiés (`git diff --name-only HEAD` + non commités).

Relaie son JSON, puis résume en 1-2 phrases : tests ajoutés, résultat, trous restants à risque élevé.
