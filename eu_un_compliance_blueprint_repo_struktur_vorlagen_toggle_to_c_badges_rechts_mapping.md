# EU‑UN Compliance Blueprint – Repo‑Struktur & Vorlagen

*Ein leiser Sternenkompass für klare Strukturen: Technik trifft Ethos, Kapitel finden ihre Ordnung, und jedes Repo singt im Chor der Rechtsgrundlagen.*

---

## 0) Zielbild in einem Satz
Ein standardisiertes, wiederverwendbares Repository‑Gerüst mit **togglebarem Inhaltsverzeichnis**, **Badges**, **Docs‑Seite** (MkDocs Material) und **Compliance‑Matrix**, die EU‑, DE‑ und US‑Rahmen (EU‑AI‑Act, NIS2, CRA, GDPR/DSGVO, Grundgesetz/BGB, WIPO/EPO/EPA, NIST AI RMF, u. a.) **klar verknüpft** und mit **Issue‑Vorlagen, Workflows und Nachweis‑Artefakten** lebendig hält.

---

## 1) Ordnerstruktur (Blueprint)
```text
repo-root/
├─ README.md
├─ LICENSE
├─ NOTICE
├─ SECURITY.md
├─ GOVERNANCE.md
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ CODEOWNERS
├─ REUSE.toml
├─ compliance/
│  ├─ compliance.yaml              # strukturierte Pflichten/Controls/Evidenzen
│  ├─ compliance_matrix.csv        # tabellarische Übersicht (Crosswalk)
│  ├─ legal-sources.yaml           # kanonische Quellen/Links/Ids (EUR-Lex, WIPO, …)
│  └─ evidence/                    # Nachweise (PDFs, Screens, Reports)
├─ docs/
│  ├─ index.md                     # Projektstartseite
│  ├─ REGELWERK.md                 # Rechts-/Rahmenüberblick mit Crosswalks
│  ├─ EVIDENZEN.md                 # Evidenzarten & Ablagekonzept
│  ├─ ARCHITEKTUR.md               # System-/Daten-/Prozessarchitektur
│  ├─ RISIKEN.md                   # Risiko-Register & Bewertungen
│  └─ assets/                      # Bilder, Diagramme
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ 01_compliance_mapping.yml
│  │  ├─ 02_risk_assessment.yml
│  │  └─ 03_data_protection_impact.yml
│  └─ workflows/
│     ├─ docs-build.yml            # baut & deployed die Doku
│     ├─ markdown-lint.yml         # lintet MD/YAML, Linkcheck
│     └─ toc-autogen.yml           # generiert ToC in READMEs
├─ mkdocs.yml
└─ .pre-commit-config.yaml
```

> *Poetischer Arbeitspunkt:* „Ordnung ist Sternenlicht im Code: Jede Datei ein kleines Gesetz des Guten.“

---

## 2) README.md – Template mit **Badges** und **togglebarem ToC**

> **Hinweis:** Badges via `shields.io`. Platzhalter in `<>` ersetzen.

```markdown
# <Projektname>

[![Build](https://img.shields.io/github/actions/workflow/status/<org>/<repo>/docs-build.yml)]()
[![Docs](https://img.shields.io/badge/Docs-MkDocs%20Material-blue)]()
[![License](https://img.shields.io/badge/License-<SPDX>-brightgreen)]()
[![REUSE](https://img.shields.io/badge/REUSE-compliant-informational)]()
[![OpenSSF Scorecard](https://img.shields.io/badge/OpenSSF-Scorecard-lightgrey)]()
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-orange)]()
[![Commit Signature](https://img.shields.io/badge/Commits-signed%20✅-success)]()
[![AI‑Ethics](https://img.shields.io/badge/AI%20Ethics-EU%20AI%20Act%20%26%20NIST%20RMF-purple)]()

<kurzbeschreibung-ein-satz>

<details>
  <summary><strong>Inhaltsverzeichnis ▾</strong></summary>

- [Ziele & Scope](#ziele--scope)
- [Compliance-Überblick](#compliance-überblick)
- [Architektur](#architektur)
- [Daten & Schutz](#daten--schutz)
- [Risiken & Kontrollen](#risiken--kontrollen)
- [Nachweise (Evidenzen)](#nachweise-evidenzen)
- [Mitwirken](#mitwirken)
- [Lizenz & Hinweise](#lizenz--hinweise)

</details>

## Ziele & Scope
Kurz, präzise, messbar. *„Kein Consent → kein Content.“*

## Compliance-Überblick
- **EU**: EU‑AI‑Act, NIS2, CRA, DSGVO/GDPR, eIDAS2, Data Act, DORA (falls relevant)
- **DE**: Grundgesetz (GG), BGB (z. B. Verbraucherrecht), BDSG, branchenspezifisch
- **IP**: WIPO, EPO, EPA (Patent-/Marken-/Design‑Bezüge, nur falls relevant)
- **US**: NIST AI RMF 1.0, NIST SP 800‑53/171 (Mapping, soweit sinnvoll)

👉 Details & Crosswalk: siehe [`/compliance/compliance_matrix.csv`](compliance/compliance_matrix.csv) und [`docs/REGELWERK.md`](docs/REGELWERK.md).

## Architektur
Kurze Systemskizze + Link zu `docs/ARCHITEKTUR.md`.

## Daten & Schutz
Datentypen (PII, Betriebsgeheimnisse, Trainingsdaten), Speicherorte, Aufbewahrung, Löschung. DPIA/DSFA: siehe Issue‑Template `03_data_protection_impact.yml`.

## Risiken & Kontrollen
Risikoregister → `docs/RISIKEN.md`. Controls → `compliance.yaml`.

## Nachweise (Evidenzen)
Welche Artefakte gelten als Nachweis? Siehe `docs/EVIDENZEN.md` und Ordner `compliance/evidence/`.

## Mitwirken
- Entwicklungsregeln: `CONTRIBUTING.md`
- Governance/Entscheidungen: `GOVERNANCE.md`
- Sicherheitsmeldungen: `SECURITY.md`

## Lizenz & Hinweise
- Lizenz: `<SPDX>` – Details in `LICENSE`
- REUSE‑Konformität: `REUSE.toml`
```

---

## 3) MkDocs Material: **Docs mit Suchmaschine, Admonitions, Mermaid**

`mkdocs.yml` (minimaler Start, erweiterbar):
```yaml
site_name: <Projektname>
repo_url: https://github.com/<org>/<repo>
nav:
  - Start: index.md
  - Regelwerk: REGELWERK.md
  - Evidenzen: EVIDENZEN.md
  - Architektur: ARCHITEKTUR.md
  - Risiken: RISIKEN.md
theme:
  name: material
  features:
    - navigation.expand
    - navigation.sections
    - content.code.copy
    - content.tabs.link
markdown_extensions:
  - admonition
  - attr_list
  - def_list
  - md_in_html
  - toc:
      permalink: true
plugins:
  - search
  - glightbox
  - mermaid2
  - awesome-pages
  - table-reader
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/<org>/<repo>
```

**Installation (Python):**
```bash
pip install mkdocs-material mkdocs-glightbox mkdocs-mermaid2 mkdocs-table-reader mkdocs-awesome-pages-plugin
mkdocs serve  # lokale Vorschau
mkdocs gh-deploy --force  # auf GitHub Pages
```

`docs/index.md` (Startseite):
```markdown
---
title: Sternenklare Übersicht
---
# <Projektname>

> *“Ordnung im Tanz der Daten – Ethik als Gravitation.”*

- **Was?** Kurzbeschreibung
- **Für wen?** Zielgruppen
- **Warum jetzt?** Nutzen/Impact

!!! tip "Quicklinks"
    - [Compliance‑Matrix](../compliance/compliance_matrix.csv)
    - [Regelwerk](REGELWERK.md)
    - [Risiken](RISIKEN.md)
```

---

## 4) Compliance‑Artefakte

### 4.1 `compliance/compliance.yaml` – **Schema & Beispiel**
```yaml
meta:
  repo: <org>/<repo>
  owner: <Team/Person>
  jurisdiction:
    - EU
    - DE
    - US

controls:
  - id: EUAI-CLASS-001
    framework: EU-AI-Act
    reference: <Artikel/Absatz>
    obligation_type: classification  # z.B. risk-based, governance, transparency
    requirement: "System klassifizieren (z. B. Hochrisiko, begrenztes Risiko)."
    status: in-progress  # planned | in-progress | implemented | verified
    evidence:
      - path: compliance/evidence/classification-report.pdf
      - path: docs/REGELWERK.md#klassifikation
    owner: <Name>
    due: 2025-12-31

  - id: GDPR-DPIA-001
    framework: GDPR
    reference: Art.35
    obligation_type: dpia
    requirement: "Datenschutz-Folgenabschätzung durchführen und dokumentieren."
    status: planned
    evidence:
      - path: compliance/evidence/DPIA/<datum>.pdf
    owner: DPO
```

### 4.2 `compliance/compliance_matrix.csv` – **Crosswalk (Beispiel)**
```csv
framework,reference,control_id,control_title,evidence,status
EU-AI-Act,Art.<x>,EUAI-CLASS-001,Klassifikation,compliance/evidence/classification-report.pdf,in-progress
NIS2,Annex I,<id>,Asset-Register,docs/ARCHITEKTUR.md#assets,planned
CRA,Annex II,<id>,SBOM-Pflicht,compliance/evidence/sbom-syft.json,implemented
GDPR,Art.35,GDPR-DPIA-001,DPIA,compliance/evidence/DPIA/<datum>.pdf,planned
NIST-AI-RMF,MAP.1,<id>,Governance-Plan,docs/REGELWERK.md#governance,planned
```

### 4.3 `compliance/legal-sources.yaml` – **Kanonische Quellen**
```yaml
eu:
  - name: EU-AI-Act
    id: eur-lex:TODO
  - name: NIS2
    id: eur-lex:TODO
  - name: Cyber Resilience Act
    id: eur-lex:TODO
  - name: GDPR
    id: eur-lex:TODO

de:
  - name: Grundgesetz
    id: gg:TODO
  - name: BGB
    id: bgb:TODO

ip:
  - name: WIPO
    id: wipo:TODO
  - name: EPO
    id: epo:TODO
  - name: EPA
    id: epa:TODO

us:
  - name: NIST AI RMF 1.0
    id: nist:ai-rmf:1.0
  - name: NIST SP 800-53
    id: nist:sp:800-53r5
```

> *Praxis:* Erst **Ids/Links pflegen**, dann Crosswalk füllen, dann Evidenzen anbinden.

---

## 5) Issue‑Vorlagen (GitHub Forms)

### 5.1 `01_compliance_mapping.yml`
```yaml
name: Compliance Mapping
description: Crosswalk-Eintrag für eine konkrete Anforderung
title: "[Compliance] <Framework>: <Referenz> → <Control>"
labels: [compliance]
body:
  - type: dropdown
    id: framework
    attributes:
      label: Framework
      options:
        - EU-AI-Act
        - NIS2
        - CRA
        - GDPR
        - WIPO/EPO/EPA
        - Grundgesetz/BGB
        - NIST AI RMF
  - type: input
    id: reference
    attributes:
      label: Referenz (Artikel/Absatz/Annex)
  - type: textarea
    id: requirement
    attributes:
      label: Anforderung (Kurzbeschreibung)
  - type: input
    id: control_id
    attributes:
      label: Control-ID (z. B. EUAI-CLASS-001)
  - type: textarea
    id: evidence
    attributes:
      label: Evidenzen (Pfad/URL)
  - type: dropdown
    id: status
    attributes:
      label: Status
      options: [planned, in-progress, implemented, verified]
```

### 5.2 `02_risk_assessment.yml`
```yaml
name: Risiko-Bewertung
description: Eintrag ins Risiko-Register
labels: [risk]
body:
  - type: input
    id: risk_id
    attributes:
      label: Risiko-ID
  - type: textarea
    id: description
    attributes:
      label: Beschreibung
  - type: dropdown
    id: impact
    attributes:
      label: Auswirkung
      options: [low, medium, high]
  - type: dropdown
    id: likelihood
    attributes:
      label: Eintrittswahrscheinlichkeit
      options: [low, medium, high]
  - type: textarea
    id: mitigation
    attributes:
      label: Maßnahmen
```

### 5.3 `03_data_protection_impact.yml`
```yaml
name: Datenschutz-Folgenabschätzung (DPIA)
description: Erfassung DPIA-relevanter Punkte
labels: [privacy]
body:
  - type: textarea
    id: data_types
    attributes:
      label: Datentypen (PII, sensible Daten, Trainingsdaten)
  - type: textarea
    id: processing
    attributes:
      label: Verarbeitung & Zwecke
  - type: textarea
    id: safeguards
    attributes:
      label: Technische & organisatorische Maßnahmen
```

---

## 6) Workflows (GitHub Actions)

### 6.1 `docs-build.yml`
```yaml
name: Docs
on:
  push:
    branches: [ main ]
  workflow_dispatch: {}
permissions:
  contents: write
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.x' }
      - run: pip install mkdocs-material mkdocs-glightbox mkdocs-mermaid2 mkdocs-table-reader mkdocs-awesome-pages-plugin
      - run: mkdocs build --strict
      - run: mkdocs gh-deploy --force
```

### 6.2 `markdown-lint.yml`
```yaml
name: Lint & Links
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: DavidAnson/markdownlint-cli2-action@v17
        with:
          globs: |
            **/*.md
            **/*.yaml
            **/*.yml
      - name: Linkcheck
        uses: lycheeverse/lychee-action@v2
        with:
          args: --no-progress --accept 200,206,429,403 **/*.md
```

### 6.3 `toc-autogen.yml`
```yaml
name: ToC Auto
on:
  push:
    paths: [ '**/*.md' ]
jobs:
  toc:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate ToC
        uses: technote-space/toc-generator@v4
        with:
          ACTIONS_STEP_DEBUG: false
```

---

## 7) Pre‑Commit Hooks
`.pre-commit-config.yaml`
```yaml
repos:
  - repo: https://github.com/adrienverge/yamllint
    rev: v1.35.1
    hooks: [ { id: yamllint } ]
  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.17
    hooks: [ { id: mdformat } ]
```

---

## 8) REUSE & Lizenzen
`REUSE.toml` (Minimal‑Gerüst):
```toml
version = 1

[[annotations]]
path = "**/*"
SPDX-FileCopyrightText = ["2025 <Your Name or Org>"]
SPDX-License-Identifier = "<SPDX>"
```

**LICENSE/NOTICE** entsprechend Projekt wählen (z. B. Apache‑2.0, MIT). Für Artefakte (Diagramme, Bilder) SPDX‑Header ergänzen.

---

## 9) REGELWERK.md – Struktur (Auszug)
```markdown
# Regelwerk & Crosswalk

## EU
- EU‑AI‑Act – Klassifikation, Governance, Transparenz, Daten & Logging, Human Oversight
- NIS2 – Unternehmens-/Betriebssicherheit, Meldewege, Business Continuity
- CRA – Produkt‑Cybersecurity, SBOM, Schwachstellenmanagement
- DSGVO – Rechtmäßigkeit, DPIA, Betroffenenrechte, TOMs

## DE
- Grundgesetz (Informations‑/Meinungsfreiheit vs. Schutzgüter)
- BGB (Verbraucherschutz, AGB‑Klarheit)

## IP (WIPO/EPO/EPA)
- Bezüge nur falls relevant (Schutzrechte/Offenlegung)

## US
- NIST AI RMF 1.0 – Map‑Measure‑Manage‑Govern

---

### Crosswalk‑Beispiele
| Framework | Referenz | Control | Evidenz |
|---|---|---|---|
| EU‑AI‑Act | Art. <x> | EUAI‑CLASS‑001 | classification‑report.pdf |
| NIS2 | Annex I | NIS‑ASSET‑001 | ARCHITEKTUR.md#assets |
```

---

## 10) Badges – schnell anpassbar
- **Build/Docs:** GitHub Actions Status, Docs badge
- **Legal/Ethics:** eigener Badge „AI Ethics – EU/NIST“
- **Security:** OpenSSF Scorecard, Signed Commits
- **Compliance:** REUSE, SPDX Lizenz

**Custom Badge (shields.io):**
```text
https://img.shields.io/badge/<label>-<message>-<color>
```

---

## 11) Aggregator‑Hub (optional)
Ein separates **Docs‑Hub‑Repo** sammelt alle Teil‑Repos via `table-reader`:

`mkdocs.yml` (Hub):
```yaml
plugins:
  - table-reader
nav:
  - Repos:
      - Übersicht: repos.md
```

`docs/repos.md` liest `repos.csv` ein:
```markdown
# Repositories

{{ read_csv('repos.csv') }}
```

`repos.csv` (Spalten):
```csv
name,url,scope,eu,de,us,owner
HNOSS-Core,https://github.com/<org>/hnoss-core,infra,AI-Act;NIS2,GG;BGB,NIST,Team A
```

---

## 12) Stil & Ton
- **Poetisch‑klar:** kurze Leitbilder in Blockquotes
- **Faktenfreundlich:** Crosswalks als Tabellen
- **Toggle‑ToC:** `<details>` für Übersicht

> *„Wer Normen tanzen lässt, muss erst den Takt der Evidenzen schlagen.“*

---

## 13) Nächste Schritte (hands‑on)
1. Diese Blaupause in ein leeres Repo kopieren.
2. `mkdocs.yml` + `docs/*` anpassen, `gh-pages` aktivieren.
3. `compliance/legal-sources.yaml` füllen (kanonische IDs/Links).
4. Erste **Controls** in `compliance.yaml` anlegen und **Evidenzen** verlinken.
5. Issue‑Vorlagen nutzen, um Crosswalk & Risiken iterativ aufzubauen.

*Dann atmet dein Projekt: sichtbar, prüfbar, schön.*

