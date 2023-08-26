import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Label("Your Plan:"),
    dcc.Input(id="your-plan", type="number", value=2500),
    html.Label("Average Plan Referral:"),
    dcc.Input(id="avg-plan-ref", type="number", value=2500),
    html.Label("Referral Payout Percentage:"),
    dcc.Input(id="ref-payout-perc", type="number", value=0.1),
    html.Label("Sales Conversion Rate:"),
    dcc.Input(id="sales-conv-rate", type="number", value=0.4),
    html.Label("Response Rate:"),
    dcc.Input(id="response-rate", type="number", value=0.6),
    html.Div(id="output")
])

@app.callback(
    Output("output", "children"),
    [
        Input("your-plan", "value"),
        Input("avg-plan-ref", "value"),
        Input("ref-payout-perc", "value"),
        Input("sales-conv-rate", "value"),
        Input("response-rate", "value")
    ]
)
def calculate_values(your_plan, avg_plan_ref, ref_payout_perc, sales_conv_rate, response_rate):
    payout = ref_payout_perc * avg_plan_ref
    referrals_needed_to_be = your_plan / payout
    conversions_needed = referrals_needed_to_be / sales_conv_rate
    touch_points_needed = conversions_needed / response_rate

    return f"Touch Points Needed: {touch_points_needed}"

if __name__ == "__main__":
    app.run_server(debug=True)