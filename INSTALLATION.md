# Installation & Utilisation des 3 outils

## Prérequis
- Python 3.10+
- Claude Code / Codex / Cursor
- Ollama (optionnel, pour ScrapeGraphAI gratuit)

---

## 1. ScrapeGraphAI

### Installation
```bash
pip install scrapegraph-ai playwright
playwright install
```

### Pour utiliser gratuitement (sans API)
```bash
# Installe Ollama depuis https://ollama.ai
ollama pull llama3.2
```

### Utilisation
```bash
python example_scrapegraphai.py
```

Voir `example_scrapegraphai.py` pour les détails.

---

## 2. Agent Reach

### Installation
```bash
# Desde le site officiel
curl -sSL https://raw.githubusercontent.com/Pannianting/agent-reach/main/docs/install.md | bash

# Ou via pip (une fois disponible)
pip install agent-reach
```

### Configuration des plateformes
```bash
agent-reach doctor
```

Pour débloquer une plateforme (Reddit, X, LinkedIn, etc.), connecte d'abord un **compte secondaire**, jamais ton compte principal.

### Utilisation
```bash
python example_agent_reach.py
```

Voir `example_agent_reach.py` pour les détails.

---

## 3. Scraping (MCP Server)

### Installation
```bash
pip install "scrapling[all]"
scrapling install
```

### En tant que serveur MCP (Claude Code)
```bash
# Récupère le chemin
which scrapling  # Mac/Linux
where scrapling  # Windows

# Ajoute à Claude Code
claude mcp add ScrapingServer "<chemin-obtenu>"

# Redémarre Claude Code
```

### Utilisation directe
```bash
# Extract une page en Markdown
scrapling extract get 'https://example.com' output.md

# Ou programmatiquement
python example_scraping.py
```

---

## Accès réseau

L'environnement cloud bloque PyPI/GitHub. Pour installer:
1. Ouvre la session → **Edit** → **Network access**
2. Passe en **Unrestricted** OU ajoute à la whitelist:
   - `pypi.org`
   - `github.com`
   - `ollama.ai` (si tu utilises Ollama)

---

## Bonnes pratiques

✅ **À faire**
- Utilise un **compte secondaire** pour les plateformes (Reddit, X, LinkedIn)
- Espace les requêtes (pas de bombardement)
- Lis `robots.txt` avant de scraper

❌ **À ne pas faire**
- Ne recopie pas les articles entiers (analyse/résume seulement)
- Ne scrape pas les données personnelles sans consentement
- Ne fais pas du scraping sur compte personnel

---

## Exemples de demande à Claude Code

### Avec tous les 3 outils
```
Avec Agent Reach, récupère ce qu'on dit sur [marque] sur Reddit et X cette semaine.
Avec ScrapeGraphAI, extrais les avis clients de [URL du site].
Avec Scraping, sauvegarde les prix en Markdown chaque lundi.
Rassemble tout dans un tableau CSV.
```

### Juste ScrapeGraphAI
```
Écris et lance un script ScrapeGraphAI. Extrais le titre et le prix de chaque produit de https://example.com et enregistre en CSV.
```

### Juste Agent Reach
```
Configure Agent Reach pour Reddit (j'ai un compte secondaire prêt).
Cherche les 10 meilleurs posts de cette semaine sur r/Python.
```

---

## Dépannage

**PyPI/GitHub refusé?**
→ Modifie le **Network access** de l'environnement (voir plus haut)

**scrapling install ne marche pas?**
→ Vérifies que tu as les droits: `chmod +x $(which scrapling)`

**Agent Reach ne trouve pas une plateforme?**
→ Exécute `agent-reach doctor` pour déboguer

**ScrapeGraphAI timeout?**
→ Augmente `timeout` ou utilise un modèle plus léger que llama3.2
