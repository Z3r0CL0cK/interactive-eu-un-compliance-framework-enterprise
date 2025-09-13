# 🌟 EU/UN Ethik & Compli
---*Ein wissenschaftlicher Blueprint für digitale Verantwortung*

> *„Ordnung ist Sternenlicht im Code: Jede Datei ein kleines Gesetz des Guten."*  
> **Kein Consent → kein Content. Jede Antwort mit Herkunft & Hash. Fail-closed statt Wunschdenken.**

<div align="center">

### 🏛️ **Projektfamilie**
**StatesFlowWishes** · **HNOSS** · **HouseOrdnung** · **Prismatahrion**

**📊 Status:** `Strukturierungsphase` → `Implementierung` → `Validierung`

</div>Compliance Framework
## *Ein wissenschaftlicher Blueprint für digitale Verantwortung*

> *„Ordnung ist Sternenlicht im Code: Jede Datei ein kleines Gesetz des Guten."*  
> **Kein Consent → kein Content. Jede Antwort mit Herkunft & Hash. Fail-closed statt Wunschdenken.**

<div align="center">

### 🏛️ **Projektfamilie**
**StatesFlowWishes** · **HNOSS** · **HouseOrdnung** · **Prismatahrion**

**📊 Status:** `Strukturierungsphase` → `Implementierung` → `Validierung`

</div>N ETHIK & COMPLIANCE – MASTER-README

> „Kein Consent → kein Content. Jede Antwort mit Herkunft & Hash. Fail-closed statt Wunschdenken.“
---

<!-- Badges (Bades) – rein symbolisch, keine amtliche Zertifizierung; verlinkt auf Nachweise/Docs -->

[![Consent Required](https://img.shields.io/badge/Consent-required-critical)](#präambel--werte)
[![Herkunft & Hash](https://img.shields.io/badge/Herkunft%20%26%20Hash-commit--sha--short-lightgrey)](#transparenz-herkunft--hash)
[![EU AI Act Mapping](https://img.shields.io/badge/EU%20AI%20Act-mapping%20in%20progress-blue)](#eu)
[![GDPR](https://img.shields.io/badge/GDPR-Article%205%2F6%2F9-informational)](#eu)
[![NIS2](https://img.shields.io/badge/NIS2-ops%2Fsec%20controls-important)](#eu)
[![CRA](https://img.shields.io/badge/CRA-security%20by%20design-important)](#eu)
[![Grundgesetz](https://img.shields.io/badge/Grundgesetz-Art.%201%20–%20Würde-brightgreen)](#deutschland)
[![BGB](https://img.shields.io/badge/BGB-zivilrechtliche%20Bezugssätze-lightgrey)](#deutschland)
[![UN Menschenrechte](https://img.shields.io/badge/UN-UDHR%20mapping-blueviolet)](#unmenschenrechte)
[![WIPO](https://img.shields.io/badge/WIPO-IP%20Policy%2FPatents%20awareness-yellow)](#wipoepoepa)
[![EPO](https://img.shields.io/badge/EPO-prior%20art%20hygiene-yellowgreen)](#wipoepoepa)
[![EPA/EUIPO](https://img.shields.io/badge/EUIPO%2FEPA-trademarks%2Fdesigns-yellowgreen)](#wipoepoepa)
[![NIST AI RMF](https://img.shields.io/badge/NIST-AI%20RMF%201.0-blue)](#usa)
[![Model Card](https://img.shields.io/badge/Model-Card%20ready-lightblue)](#governance-dokumente)
[![Dataset Card](https://img.shields.io/badge/Dataset-Card%20ready-lightblue)](#governance-dokumente)

---

<details open>
<summary><strong>Inhaltsverzeichnis</strong> (anklicken zum Ein-/Ausblenden)</summary>

- [Präambel & Werte](#präambel--werte)
- [Geltungsbereich & Referenzen](#geltungsbereich--referenzen)
- [Badges & Nachweise](#badges--nachweise)
- [Compliance-Mapping](#compliance-mapping)
  - [EU](#eu)
  - [Deutschland](#deutschland)
  - [UN/Menschenrechte](#unmenschenrechte)
  - [WIPO/EPO/EPA](#wipoepoepa)
  - [USA](#usa)
- [Repository-Register (Ethik & Menschenrechte)](#repository-register-ethik--menschenrechte)
- [Governance-Dokumente](#governance-dokumente)
- [Risikoregister (AI/Data)](#risikoregister-aidata)
- [Transparenz: Herkunft & Hash](#transparenz-herkunft--hash)
- [Glossar](#glossar)
- [Changelog](#changelog)

</details>

---

## Präambel & Werte

- **Consent First:** Ohne eindeutige Einwilligung keine Verarbeitung, Publikation oder Weitergabe.
- **Herkunft & Hash:** Jede Änderung wird mit Commit-SHA und optionaler Signatur (GPG/Sigstore/SLSA) ausgewiesen.
- **Fail-closed:** Sicherheits- und Ethikchecks entscheiden restriktiv. Bei Unsicherheit → Stop & Review.
- **Menschenwürde & Schutz vulnerabler Gruppen:** Designprinzip: Schutz > Bequemlichkeit.

<details>
<summary>Signal-/Datenhygiene (toggle)</summary>

- PII-Scrub, Zweckbindung, Datenminimierung, Speicherbegrenzung, Löschkonzepte.
- Logging ohne Personenbezug; Differential Privacy/Redaction wo sinnvoll.
- Red Teaming für Bias, Sicherheit und Missbrauchsszenarien.

</details>

---

## Geltungsbereich & Referenzen

**EU-UN-Rahmen:** EU-Rechtsakte & Leitlinien, UN-Grundsätze, interinstitutionelle Ethik.
**National (DE):** Grundgesetz (insb. Art. 1, 2, 5, 10, 13), BGB-Bezug.
**Weltweit/IP:** WIPO/EPO/EUIPO/EPA-Bezüge.
**USA:** NIST AI RMF 1.0, einschlägige Bundesrahmen (z.B. Privacy/Bill of Rights-Blueprint).

> **Hinweis:** Dieses Dokument ist eine **Struktur-/Mapping-Vorlage**. Es ersetzt keine Rechtsberatung. Verweise sind organisatorisch zu pflegen (Ordner *docs/legal/*).

---

## Badges & Nachweise

| Themenfeld | Badge (Bades) | Verlinkter Nachweis |
|---|---|---|
| Consent & Provenance | ![Consent Required](https://img.shields.io/badge/Consent-required-critical) ![Herkunft & Hash](https://img.shields.io/badge/Herkunft%20%26%20Hash-commit--sha--short-lightgrey) | [`/docs/policy/CONSENT.md`](docs/policy/CONSENT.md), [`/docs/trust/PROVENANCE.md`](docs/trust/PROVENANCE.md) |
| EU AI Act | ![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-mapping-blue) | [`/docs/mapping/EU_AI_ACT.md`](docs/mapping/EU_AI_ACT.md) |
| GDPR | ![GDPR](https://img.shields.io/badge/GDPR-5%2F6%2F9-informational) | [`/docs/mapping/GDPR_MAP.md`](docs/mapping/GDPR_MAP.md) |
| NIS2 & CRA | ![NIS2](https://img.shields.io/badge/NIS2-ops%2Fsec-important) ![CRA](https://img.shields.io/badge/CRA-secure%20by%20design-important) | [`/docs/mapping/NIS2_CRA.md`](docs/mapping/NIS2_CRA.md) |
| Grundgesetz/BGB | ![Grundgesetz](https://img.shields.io/badge/GG-Art.%201-brightgreen) ![BGB](https://img.shields.io/badge/BGB-Ref-lightgrey) | [`/docs/mapping/DE_GG_BGB.md`](docs/mapping/DE_GG_BGB.md) |
| UN/UDHR | ![UDHR](https://img.shields.io/badge/UN-UDHR-blueviolet) | [`/docs/mapping/UN_UDHR.md`](docs/mapping/UN_UDHR.md) |
| WIPO/EPO/EUIPO | ![WIPO](https://img.shields.io/badge/WIPO-IP%20policy-yellow) ![EPO](https://img.shields.io/badge/EPO-prior%20art-yellowgreen) | [`/docs/ip/WIPO_EPO_EUIPO.md`](docs/ip/WIPO_EPO_EUIPO.md) |
| USA/NIST | ![NIST AI RMF](https://img.shields.io/badge/NIST-AI%20RMF%201.0-blue) | [`/docs/mapping/NIST_AI_RMF.md`](docs/mapping/NIST_AI_RMF.md) |

> Ersetze Links/Badges mit euren echten Nachweisen. Badges sind **Meta-Signale**, keine Zertifikate.

---

## Compliance-Mapping

### EU

<details>
<summary><em>Mapping-Tabelle (EU AI Act, GDPR, NIS2/CRA, „EU Digital Pact“ u.a.)</em></summary>

| Komponente/Use-Case | Risikoklasse (AI Act) | Pflichten/Controls | GDPR-Artikel | NIS2/CRA Bezug | Nachweis/Artefakt |
|---|---|---|---|---|---|
| Beispiel: Chatbot „Serena“ | niedrig/Transparenz | Kennzeichnung AI-Interaktion, Logging-Hygiene | Art. 5(1)b Zweck, Art. 6(1) | Incident-Meldewege, SBOM | `/docs/policy/TRANSPARENCY.md` |
| Beispiel: Classifier „Pyreya“ | ggf. hoch (falls sicherheitskritisch) | Risikomanagement, Datenqualität, Monitoring | Art. 5(1)c, 9 (falls sensibel) | Secure Dev Lifecycle | `/docs/risk/AI_RISK_REGISTER.csv` |

</details>

### Deutschland

<details>
<summary><em>Mapping-Tabelle (Grundgesetz & BGB-Bezüge)</em></summary>

| Thema | GG-Artikel/Prinzip | Umsetzung im System | Nachweis |
|---|---|---|---|
| Menschenwürde | Art. 1 | Safety by Design, Content-Guardrails | `/docs/policy/HUMAN_DIGNITY_SAFEGUARDS.md` |
| Informationsfreiheit | Art. 5 | Erklärbarkeit, Doku | `/docs/trust/EXPLAINABILITY.md` |
| Brief/Telekommunikation | Art. 10 | Verschlüsselung, Privatsphäre | `/docs/security/CRYPTO.md` |

</details>

### UN/Menschenrechte

<details>
<summary><em>UDHR-Bezüge</em></summary>

| UDHR-Artikel | Risiko/Impact | Safeguard | Nachweis |
|---|---|---|---|
| Art. 12 Privatleben | Re-Identifizierbarkeit | K-Anonymität/DP | `/docs/privacy/PRIVACY_CONTROLS.md` |

</details>

### WIPO/EPO/EPA

<details>
<summary><em>IP- und Offenlegungs-Hygiene</em></summary>

- Vorveröffentlichungen und „Prior Art“ dokumentieren (`/docs/ip/PRIOR_ART.md`).
- Lizenzklarheit (FOSS-Compliance, Third-Party Notices, SBOM).
- Offenlegung vs. Schutz (Timing, NDA-Zonen, Embargo-Policy).

</details>

### USA

<details>
<summary><em>NIST AI RMF 1.0 – Kurzmapping</em></summary>

| RMF-Funktion | Umsetzung | Artefakt |
|---|---|---|
| Govern | Policy & Oversight-Board | `/docs/policy/AI_GOVERNANCE.md` |
| Map | Kontext/Use-Case-Doku | `/docs/trust/USECASE_CARDS/` |
| Measure | Eval/Bias/Security-Tests | `/docs/eval/` |
| Manage | Incident-Playbooks | `/docs/runbooks/INCIDENT.md` |

</details>

---

## Repository-Register (Ethik & Menschenrechte)

> Orte deine Repos hier ein – Zweck, Schutzmaßnahmen, Reifegrad, Nachweise.

| Repo | Zweck | Personenbezug? | Schutzmaßnahmen | Reifegrad | Nachweise |
|---|---|---|---|---|---|
| `Z3r0CL0cK/.githubT3mY2HiFT2YnC` | Werte-Layer/Manifeste | nein | Provenance, Review | Draft | `docs/` |
| `statesflowwishes-sketch/l-LCL-l--Y3zYnC…` | UI/Prototyp Spark→VS Code | ggf. | PII-Scrub, Telemetry-Off | Draft | CI Logs |

---

## Governance-Dokumente

- `/docs/policy/ETHICS_CHARTER.md` – Leitbild, Rollen, Entscheidungswege.
- `/docs/policy/CONSENT.md` – Einwilligung, Widerruf, Opt-Out.
- `/docs/trust/MODEL_CARD_TEMPLATE.md` & `/docs/trust/DATASET_CARD_TEMPLATE.md`.
- `/docs/security/SECURITY_BASELINE.md` – Crypto, Secrets, Hardening, SBOM.
- `/docs/risk/AI_RISK_REGISTER.csv` – Risiko, Schwere, Maßnahmen, Owner, Status.
- `/docs/runbooks/INCIDENT.md` – Meldeschwellen, Kontakte, 90-Tage-Window.

> **Tipp:** Nutze `<details>` innerhalb der Markdown-Dateien für kompakte, togglebare Kapitel.

---

## Risikoregister (AI/Data)

CSV-Spalten: `ID, UseCase, Risiko, Eintritt, Auswirkung, Schutzmaßnahme, Owner, Reifegrad, Nachweis, Nächste Aktion, Review-Datum`

- Beginne mit Top-5 Risiken (Bias, Halluzinationen, Datenleck, Modellmissbrauch, Supply-Chain).
- Verknüpfe jeden Eintrag mit Artefakten (Policies, Tests, Doku).

---

## Transparenz: Herkunft & Hash

- **Commit:** `<sha>` · **Signatur:** `GPG/Sigstore` · **Build-Provenance:** `SLSA/Attest` (optional).
- **Änderungsjournal:** `/CHANGELOG.md` (semantisch) mit „Versions-Kerzen“ als Milestones.
- **Hinweis:** Automatisierung via GitHub Actions kann den Commit-Short-SHA in diese Datei schreiben (Platzhalter `<!-- COMMIT_SHA -->`).

---

## Glossar

- **Consent Token:** Nachweis der Einwilligung (Scope, Zeitpunkt, Ablauf).
- **Provenance:** Nachvollziehbare Herkunft (Code, Daten, Modelle).
- **Fail-closed:** Bei Unklarheit schließt das System Wege statt zu öffnen.

---

## Changelog

- *YYYY-MM-DD* – Initiale Struktur (Kapitel, Badges, TOC-Toggle).
- *YYYY-MM-DD* – Mapping-Tabellen mit ersten Einträgen ergänzt.

---

> **Anleitung:** Diese README als **Startpunkt** in jedes relevante Repo legen. Die verlinkten Unterdokumente unter `/docs/…` anlegen und sukzessive füllen. Badges/Bades verweisen auf eure echten Nachweise, nicht umgekehrt.
