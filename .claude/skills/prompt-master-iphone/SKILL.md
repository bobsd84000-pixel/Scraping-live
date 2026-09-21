# Prompt Master iPhone Skill

Guide pour utiliser Prompt Master sur iPhone via Claude.ai directement, sans terminal.

## Méthode directe (iPhone)

### Étape 1 : Télécharge le repo
1. Ouvre Safari sur iPhone
2. Va sur https://github.com/nidhinjs/prompt-master
3. Clique sur **Code** (bouton vert)
4. Sélectionne **Download ZIP**
5. Attends que le ZIP soit téléchargé (dans l'app "Fichiers" ou "Downloads")

### Étape 2 : Importe la skill dans Claude.ai
1. Ouvre Claude.ai sur Safari ou l'app Claude
2. Appuie sur **Sidebar** ou le menu hamburger
3. Va dans **Customize** ou **Settings**
4. Cherche **Skills** ou **Upload a Skill**
5. Clique sur **Upload** ou **+**
6. Sélectionne le fichier ZIP téléchargé
7. Attends la confirmation

### Étape 3 : Utilise la skill
Une fois importée, tu peux l'utiliser de deux façons :

**Option A - Commande slash :**
```
/prompt-master
```

**Option B - Langage naturel :**
```
Write me a prompt for building a React component
```
ou
```
Generate a system prompt for a customer support chatbot
```

## Exemples d'utilisation

- `/prompt-master Tell me how to structure a project prompt`
- `Create a prompt template for a Python data analysis task`
- `Generate a detailed prompt for an AI writing assistant`
- `Help me refine this prompt: [paste your prompt]`

## Conseil : Utilise locale aussi
Si tu as un Mac ou PC, tu peux aussi utiliser via Claude Code CLI :
```bash
git clone https://github.com/nidhinjs/prompt-master
cd prompt-master
# Puis importer comme skill
```

## Troubleshooting

**La skill ne s'affiche pas après upload ?**
- Rafraîchis la page (iOS : balayage vers le bas)
- Vide le cache Claude.ai
- Réessaye de uploader le ZIP

**Le ZIP ne télécharge pas ?**
- Utilise une connexion WiFi stable
- Essaie avec une autre app de téléchargement (par ex. Documents by Readdle)

**La skill est trop lente ?**
- iPhone peut avoir des limitations
- La version desktop est plus rapide, mais ce workflow marche

## Alternative : Cloud directement

Sans télécharger, tu peux utiliser Claude.ai directement :
1. Claude.ai → New chat
2. Attache le dossier prompt-master (si tu as accès au fichier)
3. Dis : `Use prompt-master to help me generate a prompt for...`

---

**Version**: 1.0  
**Compatible**: iPhone, iPad, Safari, Claude.ai Web
