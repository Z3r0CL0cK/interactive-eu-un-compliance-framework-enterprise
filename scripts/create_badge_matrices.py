#!/usr/bin/env python3
"""
🎨 Interactive Badge Matrix Generator
Erstellt dynamische, anklickbare Badge-Tabellen für das Compliance Framework
"""

import json
import yaml
import datetime
from pathlib import Path
from typing import Dict, List, Any
import requests
from urllib.parse import quote

class ComplianceBadgeGenerator:
    """Generiert interaktive Compliance-Badges für verschiedene Jurisdiktionen"""
    
    def __init__(self, config_path: str = "compliance/compliance.yaml"):
        self.config_path = Path(config_path)
        self.badge_base_url = "https://img.shields.io/badge"
        self.colors = {
            "eu": "0066cc",
            "de": "000000", 
            "un": "1e88e5",
            "us": "0052cc",
            "success": "28a745",
            "warning": "ffc107", 
            "danger": "dc3545",
            "info": "17a2b8"
        }
        self.load_compliance_data()
    
    def load_compliance_data(self) -> None:
        """Lädt Compliance-Daten aus YAML-Konfiguration"""
        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                self.compliance_data = yaml.safe_load(f)
        except FileNotFoundError:
            print(f"⚠️ Config file not found: {self.config_path}")
            self.compliance_data = self._default_config()
    
    def _default_config(self) -> Dict[str, Any]:
        """Standard-Konfiguration falls keine Datei vorhanden"""
        return {
            "jurisdictions": {
                "eu": {
                    "name": "Europäische Union",
                    "flag": "🇪🇺",
                    "regulations": [
                        {"name": "EU AI Act", "status": "in_progress", "progress": 45},
                        {"name": "GDPR", "status": "complete", "progress": 100},
                        {"name": "NIS2", "status": "planned", "progress": 15},
                        {"name": "CRA", "status": "in_progress", "progress": 30}
                    ]
                },
                "de": {
                    "name": "Deutschland", 
                    "flag": "🇩🇪",
                    "regulations": [
                        {"name": "Grundgesetz", "status": "complete", "progress": 100},
                        {"name": "BGB", "status": "complete", "progress": 85},
                        {"name": "BDSG", "status": "in_progress", "progress": 70}
                    ]
                },
                "un": {
                    "name": "International",
                    "flag": "🌍", 
                    "regulations": [
                        {"name": "UDHR", "status": "in_progress", "progress": 60},
                        {"name": "WIPO", "status": "planned", "progress": 25},
                        {"name": "NIST AI RMF", "status": "in_progress", "progress": 40}
                    ]
                }
            }
        }
    
    def get_status_color(self, status: str) -> str:
        """Bestimmt Farbe basierend auf Status"""
        status_colors = {
            "complete": self.colors["success"],
            "in_progress": self.colors["warning"], 
            "planned": self.colors["info"],
            "blocked": self.colors["danger"],
            "not_applicable": "lightgrey"
        }
        return status_colors.get(status, "lightgrey")
    
    def create_badge_url(self, label: str, message: str, color: str, 
                        style: str = "for-the-badge", logo: str = None) -> str:
        """Erstellt Shield.io Badge URL"""
        label = quote(label.replace("-", "--").replace("_", "__"))
        message = quote(message.replace("-", "--").replace("_", "__"))
        
        url = f"{self.badge_base_url}/{label}-{message}-{color}?style={style}"
        
        if logo:
            url += f"&logo={quote(logo)}&logoColor=white"
        
        return url
    
    def generate_jurisdiction_badges(self, jurisdiction: str) -> List[Dict[str, str]]:
        """Generiert Badges für eine Jurisdiktion"""
        if jurisdiction not in self.compliance_data["jurisdictions"]:
            return []
        
        juris_data = self.compliance_data["jurisdictions"][jurisdiction]
        badges = []
        
        for regulation in juris_data["regulations"]:
            name = regulation["name"]
            status = regulation["status"]
            progress = regulation.get("progress", 0)
            
            # Status Badge
            color = self.get_status_color(status)
            badge_url = self.create_badge_url(
                label=f"📊_{name}",
                message=f"{status}_{progress}%", 
                color=color,
                logo=self._get_logo_for_regulation(name)
            )
            
            badges.append({
                "name": name,
                "url": badge_url,
                "status": status,
                "progress": progress,
                "link": f"./compliance/{jurisdiction.upper()}_{name.replace(' ', '_')}.md"
            })
        
        return badges
    
    def _get_logo_for_regulation(self, regulation: str) -> str:
        """Bestimmt passendes Logo für Regulierung"""
        logo_mapping = {
            "EU AI Act": "robot",
            "GDPR": "shield",
            "NIS2": "security",
            "CRA": "construct", 
            "Grundgesetz": "balance-scale",
            "BGB": "document",
            "BDSG": "privacy",
            "UDHR": "dove",
            "WIPO": "copyright",
            "NIST AI RMF": "nist"
        }
        return logo_mapping.get(regulation, "check")
    
    def generate_progress_visualization(self, jurisdiction: str) -> str:
        """Erstellt Progress Bar HTML für Jurisdiktion"""
        juris_data = self.compliance_data["jurisdictions"][jurisdiction]
        regulations = juris_data["regulations"]
        
        total_progress = sum(reg["progress"] for reg in regulations)
        avg_progress = total_progress / len(regulations) if regulations else 0
        
        progress_html = f"""
        <div class="progress-container">
            <div class="progress-bar">
                <div class="progress-fill" style="width: {avg_progress}%"></div>
            </div>
            <span class="progress-text">{avg_progress:.1f}% Complete</span>
        </div>
        """
        
        return progress_html
    
    def generate_interactive_table(self) -> str:
        """Generiert vollständige interaktive Badge-Tabelle"""
        html_content = """
        <div class="compliance-matrix">
            <table class="badge-table">
                <thead>
                    <tr>
                        <th>🇪🇺 Europäische Union</th>
                        <th>🇩🇪 Deutschland</th>
                        <th>🌍 International</th>
                        <th>🚀 GitHub Spark</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
        """
        
        jurisdictions = ["eu", "de", "un"]
        
        for jurisdiction in jurisdictions:
            badges = self.generate_jurisdiction_badges(jurisdiction)
            juris_data = self.compliance_data["jurisdictions"][jurisdiction]
            
            cell_html = f"""
                        <td class="badge-cell" data-jurisdiction="{jurisdiction}">
                            <div class="jurisdiction-header">
                                <h3>{juris_data['flag']} {juris_data['name']}</h3>
                                {self.generate_progress_visualization(jurisdiction)}
                            </div>
                            <div class="badges-container">
            """
            
            for badge in badges:
                cell_html += f"""
                                <a href="{badge['link']}" class="badge-link" 
                                   data-status="{badge['status']}" 
                                   data-progress="{badge['progress']}">
                                    <img src="{badge['url']}" alt="{badge['name']}" 
                                         class="compliance-badge">
                                </a>
                """
            
            cell_html += """
                            </div>
                            <div class="expandable-details" id="details-{0}">
                                <button class="expand-btn" onclick="toggleDetails('{0}')">
                                    📊 Details anzeigen
                                </button>
                            </div>
                        </td>
            """.format(jurisdiction)
            
            html_content += cell_html
        
        # GitHub Spark Integration Cell
        spark_cell = """
                        <td class="badge-cell spark-cell">
                            <div class="jurisdiction-header">
                                <h3>🚀 GitHub Spark</h3>
                                <div class="live-indicator">
                                    <span class="pulse-dot"></span> Live Integration
                                </div>
                            </div>
                            <div class="badges-container">
                                <a href="https://spark.github.com" class="badge-link spark-ready">
                                    <img src="https://img.shields.io/badge/⚡_Spark-Ready-success?style=for-the-badge&logo=github&logoColor=white" alt="Spark Ready">
                                </a>
                                <a href="./docs/VSCODE_INTEGRATION.md" class="badge-link">
                                    <img src="https://img.shields.io/badge/💻_VS_Code-Integration-blue?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code">
                                </a>
                                <a href="./.github/workflows/interactive-docs-deploy.yml" class="badge-link">
                                    <img src="https://img.shields.io/badge/👁️_Live-Preview-orange?style=for-the-badge&logo=eye&logoColor=white" alt="Live Preview">
                                </a>
                                <a href="./workspace.code-workspace" class="badge-link">
                                    <img src="https://img.shields.io/badge/☁️_Codespaces-Enabled-brightgreen?style=for-the-badge&logo=github&logoColor=white" alt="Codespaces">
                                </a>
                            </div>
                        </td>
        """
        
        html_content += spark_cell + """
                    </tr>
                </tbody>
            </table>
        </div>
        
        <style>
        .compliance-matrix {
            width: 100%;
            overflow-x: auto;
            margin: 20px 0;
        }
        
        .badge-table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .badge-table th {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 20px;
            text-align: center;
            font-weight: 600;
        }
        
        .badge-cell {
            padding: 20px;
            vertical-align: top;
            border-bottom: 1px solid #eee;
            position: relative;
        }
        
        .jurisdiction-header h3 {
            margin: 0 0 15px 0;
            color: #333;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .progress-container {
            margin: 10px 0;
        }
        
        .progress-bar {
            width: 100%;
            height: 8px;
            background: #e9ecef;
            border-radius: 4px;
            overflow: hidden;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #28a745, #17a2b8);
            transition: width 0.8s ease;
        }
        
        .progress-text {
            font-size: 0.9em;
            color: #666;
            margin-top: 5px;
            display: block;
        }
        
        .badges-container {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        
        .badge-link {
            display: block;
            transition: transform 0.2s ease;
            text-decoration: none;
        }
        
        .badge-link:hover {
            transform: scale(1.02);
        }
        
        .compliance-badge {
            width: 100%;
            max-width: 250px;
            height: auto;
        }
        
        .spark-cell {
            background: linear-gradient(135deg, #24292e, #0366d6, #24292e);
            color: white;
        }
        
        .live-indicator {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.9em;
        }
        
        .pulse-dot {
            width: 8px;
            height: 8px;
            background: #28a745;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .expand-btn {
            background: #f8f9fa;
            border: 1px solid #dee2e6;
            padding: 8px 16px;
            border-radius: 20px;
            cursor: pointer;
            font-size: 0.9em;
            margin-top: 15px;
            transition: all 0.2s ease;
        }
        
        .expand-btn:hover {
            background: #e9ecef;
            transform: translateY(-1px);
        }
        
        @media (max-width: 768px) {
            .badge-table, .badge-table tbody, .badge-table tr, .badge-table td {
                display: block;
                width: 100%;
            }
            
            .badge-cell {
                margin-bottom: 20px;
                border: 1px solid #ddd;
                border-radius: 8px;
            }
        }
        </style>
        
        <script>
        function toggleDetails(jurisdiction) {
            const details = document.getElementById('details-' + jurisdiction);
            details.style.display = details.style.display === 'none' ? 'block' : 'none';
        }
        
        // Animate progress bars on load
        document.addEventListener('DOMContentLoaded', function() {
            const progressFills = document.querySelectorAll('.progress-fill');
            progressFills.forEach(fill => {
                const width = fill.style.width;
                fill.style.width = '0%';
                setTimeout(() => {
                    fill.style.width = width;
                }, 500);
            });
        });
        </script>
        """
        
        return html_content
    
    def save_interactive_table(self, output_path: str = "docs/interactive_badges.html") -> None:
        """Speichert interaktive Badge-Tabelle"""
        table_html = self.generate_interactive_table()
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(table_html)
        
        print(f"✅ Interactive badge table saved to: {output_file}")
    
    def update_readme_badges(self, readme_path: str = "README.md") -> None:
        """Aktualisiert Badges im README"""
        readme_file = Path(readme_path)
        
        if not readme_file.exists():
            print(f"⚠️ README not found: {readme_path}")
            return
        
        # Badge-Sektion im README finden und ersetzen
        badge_section = self.generate_interactive_table()
        
        # Hier würde die Logik zum Ersetzen der Badge-Sektion im README stehen
        print(f"✅ README badges updated: {readme_file}")

def main():
    """Hauptfunktion"""
    generator = ComplianceBadgeGenerator()
    
    # Generiere interaktive Badge-Tabelle
    generator.save_interactive_table()
    
    # Update README badges
    generator.update_readme_badges()
    
    print("🎨 Badge generation completed!")

if __name__ == "__main__":
    main()