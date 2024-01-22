import pathlib
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import json, urllib

app = Dash(__name__, title="sankey_app")

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

app.layout = html.Div([
    html.H4('Supply chain of the energy production'),
    dcc.Graph(id="graph"),
    html.P("Opacity"),
    dcc.Slider(id='slider', min=0, max=1, 
               value=0.5, step=0.1)
])

# def load_data(data_file: str) -> pd.DataFrame:
#     '''
#     Load data from /data directory
#     '''
#     PATH = pathlib.Path(__file__).parent
#     DATA_PATH = PATH.joinpath("data").resolve()
#     return pd.read_csv(DATA_PATH.joinpath(data_file))

# app.layout = html.Div([
#     html.H4('Simple stock plot with adjustable axis'),
#     html.Button("Switch Axis", n_clicks=0,
#                 id='button'),
#     dcc.Graph(id="graph"),
# ])

# @app.callback(
#     Output("graph", "figure"),
#     Input("button", "n_clicks"))
# def display_graph(n_clicks):
#     # replace with your own data source
#     df = load_data("2014_apple_stock.csv")

#     if n_clicks % 2 == 0:
#         x, y = 'AAPL_x', 'AAPL_y'
#     else:
#         x, y = 'AAPL_y', 'AAPL_x'

#     fig = px.line(df, x=x, y=y)
#     return fig

@app.callback(
    Output("graph", "figure"), 
    Input("slider", "value"))
def display_sankey(opacity):
    url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read()) # replace with your own data source

    node = data['data'][0]['node']
    node['color'] = [
        f'rgba(255,0,255,{opacity})' 
        if c == "magenta" else c.replace('0.8', str(opacity)) 
        for c in node['color']]

    link = data['data'][0]['link']
    link['color'] = [
        node['color'][src] for src in link['source']]

    fig = go.Figure(go.Sankey(link=link, node=node))
    fig.update_layout(font_size=10)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
