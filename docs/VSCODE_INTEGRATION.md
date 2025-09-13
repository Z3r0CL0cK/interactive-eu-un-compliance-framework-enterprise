# Interaktive VS Code Integration Dokumentation
## GitHub Spark kompatible UI/UX für Compliance Framework

### 🎯 VS Code Webview Integration

Diese Datei stellt eine interaktive Benutzeroberfläche bereit, die sowohl in VS Code als auch über GitHub Spark zugänglich ist.

## Live Preview Setup

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EU/UN Compliance Framework - Interactive Dashboard</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #2F81F7;
            --secondary-color: #0366d6;
            --success-color: #28a745;
            --warning-color: #ffc107;
            --danger-color: #dc3545;
            --info-color: #17a2b8;
            --light-color: #f8f9fa;
            --dark-color: #343a40;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .dashboard {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        .compliance-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 30px;
        }
        
        .compliance-card {
            background: var(--light-color);
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
        }
        
        .compliance-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }
        
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .card-icon {
            font-size: 2rem;
            margin-right: 15px;
            color: var(--primary-color);
        }
        
        .progress-bar {
            width: 100%;
            height: 10px;
            background: #e9ecef;
            border-radius: 5px;
            overflow: hidden;
            margin: 10px 0;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--success-color), var(--info-color));
            transition: width 0.5s ease;
        }
        
        .interactive-buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 15px;
        }
        
        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 5px;
        }
        
        .btn-primary { background: var(--primary-color); color: white; }
        .btn-success { background: var(--success-color); color: white; }
        .btn-warning { background: var(--warning-color); color: black; }
        .btn-danger { background: var(--danger-color); color: white; }
        .btn-info { background: var(--info-color); color: white; }
        
        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        
        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 8px;
        }
        
        .status-active { background: var(--success-color); }
        .status-warning { background: var(--warning-color); }
        .status-error { background: var(--danger-color); }
        
        .expandable {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.3s ease;
        }
        
        .expandable.expanded {
            max-height: 500px;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(47, 129, 247, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(47, 129, 247, 0); }
            100% { box-shadow: 0 0 0 0 rgba(47, 129, 247, 0); }
        }
        
        .pulse {
            animation: pulse 2s infinite;
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <div class="header">
            <h1><i class="fas fa-balance-scale"></i> EU/UN Compliance Framework</h1>
            <p>Interaktives Dashboard für digitale Verantwortung</p>
            <div class="interactive-buttons">
                <button class="btn btn-primary" onclick="openVSCode()">
                    <i class="fab fa-github"></i> Open in VS Code
                </button>
                <button class="btn btn-success" onclick="openCodespaces()">
                    <i class="fas fa-cloud"></i> Launch Codespaces
                </button>
                <button class="btn btn-info" onclick="viewDocs()">
                    <i class="fas fa-book"></i> Documentation
                </button>
            </div>
        </div>
        
        <div class="compliance-grid">
            <!-- EU Compliance Card -->
            <div class="compliance-card" onclick="toggleCard('eu-card')">
                <div class="card-header">
                    <div class="card-icon">🇪🇺</div>
                    <div>
                        <h3>Europäische Union</h3>
                        <span class="status-indicator status-warning"></span>
                        <span>In Bearbeitung (65%)</span>
                    </div>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 65%"></div>
                </div>
                <div class="expandable" id="eu-card">
                    <p><strong>Aktuelle Implementierungen:</strong></p>
                    <ul>
                        <li>✅ GDPR Art. 5-6 vollständig</li>
                        <li>🔄 EU AI Act Risikobewertung</li>
                        <li>📋 NIS2 Security Controls geplant</li>
                        <li>🏗️ CRA Security by Design</li>
                    </ul>
                    <div class="interactive-buttons">
                        <button class="btn btn-primary" onclick="openCompliance('eu')">
                            <i class="fas fa-eye"></i> Details
                        </button>
                        <button class="btn btn-success" onclick="runTests('eu')">
                            <i class="fas fa-play"></i> Tests
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- Deutschland Card -->
            <div class="compliance-card" onclick="toggleCard('de-card')">
                <div class="card-header">
                    <div class="card-icon">🇩🇪</div>
                    <div>
                        <h3>Deutschland</h3>
                        <span class="status-indicator status-active"></span>
                        <span>Abgeschlossen (80%)</span>
                    </div>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 80%"></div>
                </div>
                <div class="expandable" id="de-card">
                    <p><strong>Rechtliche Grundlagen:</strong></p>
                    <ul>
                        <li>⚖️ Grundgesetz Art. 1 (Menschenwürde)</li>
                        <li>📋 BGB Zivilrechtliche Bezüge</li>
                        <li>🔒 BDSG Datenschutz harmonisiert</li>
                    </ul>
                    <div class="interactive-buttons">
                        <button class="btn btn-success" onclick="viewLegalSources('de')">
                            <i class="fas fa-gavel"></i> Rechtsquellen
                        </button>
                        <button class="btn btn-info" onclick="generateReport('de')">
                            <i class="fas fa-file-alt"></i> Report
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- International Card -->
            <div class="compliance-card" onclick="toggleCard('int-card')">
                <div class="card-header">
                    <div class="card-icon">🌍</div>
                    <div>
                        <h3>International</h3>
                        <span class="status-indicator status-warning"></span>
                        <span>Entwicklung (45%)</span>
                    </div>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 45%"></div>
                </div>
                <div class="expandable" id="int-card">
                    <p><strong>Globale Standards:</strong></p>
                    <ul>
                        <li>🕊️ UN UDHR Art. 12, 19 Mapping</li>
                        <li>🏛️ WIPO IP Policy Integration</li>
                        <li>🔬 EPO Prior Art Hygiene</li>
                        <li>🇺🇸 NIST AI RMF 1.0 Framework</li>
                    </ul>
                    <div class="interactive-buttons">
                        <button class="btn btn-info" onclick="viewStandards('int')">
                            <i class="fas fa-globe"></i> Standards
                        </button>
                        <button class="btn btn-warning" onclick="assessRisk('int')">
                            <i class="fas fa-exclamation-triangle"></i> Risiken
                        </button>
                    </div>
                </div>
            </div>
            
            <!-- GitHub Spark Card -->
            <div class="compliance-card pulse" onclick="toggleCard('spark-card')">
                <div class="card-header">
                    <div class="card-icon">🚀</div>
                    <div>
                        <h3>GitHub Spark</h3>
                        <span class="status-indicator status-active"></span>
                        <span>Live Integration</span>
                    </div>
                </div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 100%"></div>
                </div>
                <div class="expandable" id="spark-card">
                    <p><strong>Integration Flow:</strong></p>
                    <ul>
                        <li>⚡ Spark Analysis → UI Generation</li>
                        <li>💻 VS Code Live Preview</li>
                        <li>🔄 Auto Deploy zu GitHub Pages</li>
                        <li>☁️ Codespaces Ready</li>
                    </ul>
                    <div class="interactive-buttons">
                        <button class="btn btn-primary" onclick="launchSpark()">
                            <i class="fas fa-rocket"></i> Launch Spark
                        </button>
                        <button class="btn btn-success" onclick="deployPages()">
                            <i class="fas fa-upload"></i> Deploy
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Interactive Functions
        function toggleCard(cardId) {
            const card = document.getElementById(cardId);
            card.classList.toggle('expanded');
        }
        
        function openVSCode() {
            window.open('https://vscode.dev/github/statesflowwishes-sketch/l-LCL-l--Y3zYnC-CnYz3Y2m1l3--l-LCL-l', '_blank');
        }
        
        function openCodespaces() {
            window.open('https://codespaces.new/statesflowwishes-sketch/l-LCL-l--Y3zYnC-CnYz3Y2m1l3--l-LCL-l', '_blank');
        }
        
        function viewDocs() {
            window.open('./docs/', '_blank');
        }
        
        function openCompliance(jurisdiction) {
            alert(`Öffne ${jurisdiction.toUpperCase()} Compliance Details...`);
            // In einer echten Implementierung würde dies zu spezifischen Dokumenten weiterleiten
        }
        
        function runTests(jurisdiction) {
            alert(`Führe ${jurisdiction.toUpperCase()} Compliance Tests aus...`);
            // Würde automatisierte Tests starten
        }
        
        function viewLegalSources(jurisdiction) {
            alert(`Zeige Rechtsquellen für ${jurisdiction.toUpperCase()}...`);
        }
        
        function generateReport(jurisdiction) {
            alert(`Generiere Compliance Report für ${jurisdiction.toUpperCase()}...`);
        }
        
        function viewStandards(jurisdiction) {
            alert(`Zeige internationale Standards für ${jurisdiction.toUpperCase()}...`);
        }
        
        function assessRisk(jurisdiction) {
            alert(`Führe Risikobewertung für ${jurisdiction.toUpperCase()} durch...`);
        }
        
        function launchSpark() {
            alert('Starte GitHub Spark Integration...');
            window.open('https://spark.github.com', '_blank');
        }
        
        function deployPages() {
            alert('Deploye zu GitHub Pages...');
            // Würde GitHub Actions Workflow auslösen
        }
        
        // Auto-update progress bars with animation
        document.addEventListener('DOMContentLoaded', function() {
            const progressBars = document.querySelectorAll('.progress-fill');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 500);
            });
        });
    </script>
</body>
</html>
```

### 🔧 VS Code Integration Guide

1. **Webview Panel erstellen:**
```typescript
const panel = vscode.window.createWebviewPanel(
    'complianceDashboard',
    'EU/UN Compliance Dashboard',
    vscode.ViewColumn.One,
    {
        enableScripts: true,
        retainContextWhenHidden: true
    }
);
```

2. **Live Preview mit Simple Browser:**
```json
{
    "command": "simpleBrowser.show",
    "args": ["./docs/VSCODE_INTEGRATION.html"]
}
```

3. **GitHub Spark Prompt:**
```markdown
Erstelle interaktive UI basierend auf EU/UN Compliance Framework.
Design: Wissenschaftlich, responsive, VS Code kompatibel.
Features: Badge-Tabellen, Progress-Tracking, Live-Updates.
Integration: GitHub Pages, Codespaces, Simple Browser.
```
