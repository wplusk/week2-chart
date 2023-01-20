from pathlib import Path

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

DATA_PATH = Path(__file__).parent.joinpath('data')

app = Dash(__name__, 
external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

app.layout = dbc.Container(
    [
        html.H1("Paralympic Medals Dashboard"),

    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
