import pandas as pd

def triage_alerts(logs_df):
    # Triage rule: flag logs with a 'failure' status as alerts
    alerts = logs_df[logs_df["status"] == "failure"].copy()
    alerts["alert_type"] = alerts["event_type"].apply(lambda x: f"{x.upper()}_ALERT")
    return alerts

if __name__ == '__main__':
    from log_parser import parse_logs
    logs = parse_logs()
    alerts = triage_alerts(logs)
    print("Alerts detected:")
    print(alerts)
