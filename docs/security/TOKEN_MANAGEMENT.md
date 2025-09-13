# Token & Secrets Management

## Sicherheitsprinzipien
- **Fail-closed:** Keine Token/Secrets im Git-Verlauf
- **Separation:** .env-Dateien für lokale Entwicklung, GitHub Secrets für CI/CD
- **Rotation:** Regelmäßiger Token-Wechsel
- **Least Privilege:** Minimale Berechtigungen pro Token

## Setup
1. Kopiere `.env.example` zu `.env`
2. Fülle deine Token ein (siehe Anleitung unten)
3. Prüfe: `.env` steht in `.gitignore`

## GitHub Token
- Gehe zu GitHub Settings → Developer Settings → Personal Access Tokens
- Scope: `repo`, `workflow`, `write:packages` (je nach Bedarf)
- Format: `ghp_...`

## Docker Hub Token
- Gehe zu Docker Hub → Account Settings → Security → Access Tokens
- Format: `dckr_pat_...`

## Verwendung in GitHub Actions
```yaml
env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  DOCKER_TOKEN: ${{ secrets.DOCKER_TOKEN }}
```

## Compliance Notes
- Token-Nutzung wird geloggt (ohne Token-Werte)
- Regelmäßige Security-Reviews
- DPIA-relevant falls personenbezogene Daten verarbeitet werden