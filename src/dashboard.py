import dash
from dash import dcc, html
import dash_table
import plotly.express as px

def create_dashboard(alerts_df):
    app = dash.Dash(__name__)
    
    # Create a histogram to display alert distribution by event type
    fig = px.histogram(alerts_df, x="event_type", title="Alert Distribution by Event Type")
    
    app.layout = html.Div(children=[
        html.H1(children='SOC Incident Response Dashboard'),
        html.Div(children='Overview of detected alerts.'),
        dash_table.DataTable(
            id='alerts-table',
            columns=[{"name": i, "id": i} for i in alerts_df.columns],
            data=alerts_df.to_dict('records'),
            page_size=10,
        ),
        dcc.Graph(figure=fig)
    ])
    
    return app

if __name__ == '__main__':
    from log_parser import parse_logs
    from alert_triage import triage_alerts
    logs = parse_logs()
    alerts = triage_alerts(logs)
    app = create_dashboard(alerts)
    app.run_server(debug=True)
