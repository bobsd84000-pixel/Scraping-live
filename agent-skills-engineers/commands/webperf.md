---
description: Audit Core Web Vitals (LCP, INP, CLS), loading et rendering
argument-hint: [page | URL | vide = pages modifiées]
---

Cible : $ARGUMENTS (vide = fichiers front modifiés : html, css, js, jsx, tsx, vue, svelte).

Délègue à l'agent `web-performance-auditor`. S'il y a une URL ou un serveur local lançable, demande-lui de mesurer (Playwright/Chromium) plutôt que d'estimer.

Affiche : métriques (mesurées ou "estimé"), puis constats `high` en premier au format `fichier:ligne — problème → impact → fix`. Verdict **PASS** / **FAIL**.
