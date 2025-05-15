# SOC Incident Response Simulator and Dashboard

This project simulates the daily tasks of a SOC analyst. It ingests synthetic logs from different sources, triages alerts using automated rules (or a machine learning component), visualizes incidents on an interactive dashboard, and generates a structured incident response report.

## Features

- **Data Aggregation & Normalization:** Ingest and parse simulated logs.
- **Alert Triage Engine:** Rule-based (or ML-enhanced) alert prioritization.
- **Incident Visualization:** Interactive dashboard with timelines, correlated evidence, and metrics.
- **Automated Response Reporting:** Generation of incident reports mimicking real-world investigations.
- **Real-time Simulation (Optional):** Integration of live alert streaming using websockets.

## Folder Structure
```
SOC-Incident-Response-Simulator/
├── README.md
├── requirements.txt
├── docs/
│   └── incident_report.json
├── data/
│   └── synthetic_logs.csv
└── src/
    ├── main.py
    ├── log_generator.py
    ├── log_parser.py
    ├── alert_triage.py
    ├── dashboard.py
        └── response_report.py
```
## Installation & Usage

This project can be edited and run entirely using GitHub Codespaces or the web editor:
1. Use GitHub Codespaces to open a full IDE in your browser (if available).
2. Install dependencies listed in `requirements.txt`.
3. Run the application using:
```
   `python src/main.py`
```
