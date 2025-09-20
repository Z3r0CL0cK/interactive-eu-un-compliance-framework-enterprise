#!/usr/bin/env python3
"""
Generate a compliance status report from check results.
"""
import json
import argparse
from datetime import datetime

def generate_report(eu_status, gdpr_status, intl_status):
    """Generate a markdown report from status data."""
    report = "# Compliance Status Report\n"
    report += f"Generated: {datetime.utcnow().isoformat()}Z\n\n"
    
    report += "## EU AI Act Compliance\n"
    report += f"- Status: `{eu_status.get('status', 'unknown')}`\n"
    if 'last_checked' in eu_status:
        report += f"- Last Checked: {eu_status['last_checked']}\n"
    report += "\n"
    
    report += "## GDPR Compliance\n"
    report += f"- Status: `{gdpr_status.get('status', 'unknown')}`\n"
    if 'last_audit' in gdpr_status:
        report += f"- Last Audit: {gdpr_status['last_audit']}\n"
    report += f"- Checks Passed: {gdpr_status.get('checks_passed', 0)}\n"
    report += "\n## International Standards\n"
    report += f"- Status: `{intl_status.get('status', 'unknown')}`\n"
    if 'sources_checked' in intl_status:
        report += f"- Sources Checked: {', '.join(intl_status['sources_checked'])}\n"
    return report

def main():
    """Main function to handle command line arguments."""
    parser = argparse.ArgumentParser(description='Generate Compliance Status Report')
    parser.add_argument('--eu-status', type=json.loads, help='EU AI Act status JSON')
    parser.add_argument('--gdpr-status', type=json.loads, help='GDPR status JSON')
    parser.add_argument('--intl-status', type=json.loads, help='International status JSON')
    parser.add_argument('--output', default='compliance_report.md', help='Output file path')
    
    args = parser.parse_args()
    
    report = generate_report(
        args.eu_status or {},
        args.gdpr_status or {},
        args.intl_status or {}
    )
    
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Report generated: {args.output}")

if __name__ == "__main__":
    main()
