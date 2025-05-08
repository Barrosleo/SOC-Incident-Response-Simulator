import json
from datetime import datetime

def generate_response_report(alerts_df):
    report = {
        "report_generated": datetime.now().isoformat(),
        "total_alerts": len(alerts_df),
        "alerts_by_type": alerts_df["alert_type"].value_counts().to_dict(),
        "details": alerts_df.to_dict('records')
    }
    return report

if __name__ == '__main__':
    from log_parser import parse_logs
    from alert_triage import triage_alerts
    logs = parse_logs()
    alerts = triage_alerts(logs)
    report = generate_response_report(alerts)
    print("Incident Response Report:")
    print(report)
    
    # Save the report to the docs folder
    with open("docs/incident_report.json", "w") as f:
        json.dump(report, f, indent=4)
