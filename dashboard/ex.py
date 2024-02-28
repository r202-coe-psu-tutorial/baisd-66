import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output

import datetime

import pandas
import plotly.express as px

app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])


def get_bar_fruit():
    df = pandas.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
        }
    )

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    return fig


@app.callback(
    Output("current-time", "children"),
    Input("current-time-interval", "n_intervals"),
)
def get_current_time(n_intervals):
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


current_time_interval = dcc.Interval(
    id="current-time-interval", interval=1000, n_intervals=0
)

app.layout = html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.H1(children="Hello Dash"),
                        html.Div(
                            children="""
        Dash: A web application framework for your data.
    """
                        ),
                        dcc.Graph(id="example-graph", figure=get_bar_fruit()),
                    ]
                ),
                dbc.Col(
                    children=[
                        html.H1(children="Time"),
                        html.H2(id="current-time"),
                    ]
                ),
            ]
        ),
        current_time_interval,
    ]
)


# app.layout = dbc.Alert("Hello, Bootstrap!", className="m-5")

if __name__ == "__main__":
    app.run_server(debug=True)
