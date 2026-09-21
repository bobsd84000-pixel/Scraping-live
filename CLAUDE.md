# Scraping-live + Ruflo

## État actuel

### Agents, commandes, skills Ruflo intégrés

Depuis `github.com/ruvnet/ruflo`, ont été intégrés sous `.claude/` :
- **67 agents** (+ 41 retirés pour dépendance CLI/MCP)
- **35 commandes** (+ 133 retirés pour dépendance `npx`/MCP)
- **8 skills** (+ 30 retirés pour dépendance `npx`)

Tous les fichiers intégrés sont autonomes et ne requièrent aucune installation npm ni serveur MCP externe.

### Agents disponibles

- **analysis** : code-quality, patterns, performance
- **architecture** : system-design, scalability
- **database-specialist** : SQL, schema optimization
- **development** : code generation, testing
- **devops** : CI/CD, infrastructure
- **flow-nexus** : orchestration
- **python-specialist** : Python patterns
- **reasoning** : logic, problem-solving
- **security-auditor** : vulnerability scanning
- Et ~50 autres

### Commands disponibles

Catégories fonctionnelles :
- `automation/` : orchestration multi-tâches
- `coordination/` : swarms, agents
- `memory/` : apprentissage, logs
- `monitoring/` : observabilité
- `optimization/` : perf, cache
- `pair/` : pair programming
- `swarm/` : coordination agents
- `workflows/` : templates réutilisables

Chaque command est une `.md` avec stratégie et exemples.

### Skills disponibles

8 skills pour v3 du framework :
- `v3-core-implementation` : cœur
- `v3-cli-modernization` : CLI
- `v3-mcp-optimization` : MCP
- `v3-security-overhaul` : sécurité
- Autres : memory, integration, reasoning

## Limitations actuelles

**Blocage npm.org (403)** : `registry.npmjs.org` est inaccesible depuis cet environnement. Conséquences :

- ❌ Pas de CLI `npx ruflo`
- ❌ Pas de serveur MCP intégré (outils `mcp__claude-flow__*`)
- ❌ Pas d'auto-hooks ni daemon
- ✅ Agents/skills/commands définitions = OK (fichiers `.md` purs)

**Workaround** : Les definitions seules suffisent pour orchestration manuelle. Pour le full stack, installer localement :

```bash
git clone https://github.com/ruvnet/ruflo.git
cd ruflo
npm install  # sur machine avec accès npm
npx ruflo init
```

## Branches

- `main` : produit
- `claude/new-session-g0s5kr` : dev courant (Ruflo intégré)

## Structure

```
.
├── .claude/
│   ├── agents/         # 67 définitions
│   ├── commands/       # 35 commandes
│   └── skills/         # 8 skills
├── api/
├── index.html
└── README.md
```
