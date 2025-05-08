from log_generator import generate_logs
from log_parser import parse_logs
from alert_triage import triage_alerts
from dashboard import create_dashboard
from response_report import generate_response_report
import os

def main():
    # Ensure the data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Step 1: Generate synthetic logs
    print("Generating synthetic logs...")
    df_logs = generate_logs(200)
    df_logs.to_csv("data/synthetic_logs.csv", index=False)
    print("Synthetic logs generated.")

    # Step 2: Parse logs
    logs = parse_logs("data/synthetic_logs.csv")
    print("Logs parsed. Number of records:", len(logs))

    # Step 3: Triage alerts based on our rule-based logic
    alerts = triage_alerts(logs)
    print("Alerts identified:", len(alerts))

    # Step 4: Generate an incident response report
    report = generate_response_report(alerts)
    print("Response report generated. Details saved to docs/incident_report.json")

    # Step 5: Launch the dashboard for visualization
    app = create_dashboard(alerts)
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
