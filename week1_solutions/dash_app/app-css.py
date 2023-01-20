from dash import Dash, html
import dash_bootstrap_components as dbc


app = Dash(__name__, 
external_stylesheets=[dbc.themes.BOOTSTRAP],
meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

app.layout = dbc.Container(children=[
    html.H1(children='Hello, World!'),
    html.H1(children='Heading with Bootsrap "display-1" style', className="display-1"),
    html.P('My first Dash app')

])

if __name__ == '__main__':
    app.run_server(debug=True)
