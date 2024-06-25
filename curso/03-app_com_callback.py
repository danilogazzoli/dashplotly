from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Exemplo com callback', style={'textAlign': 'center'}),
    dcc.Dropdown(df.country.unique(), 'Brazil', id='dropdown-selection'),
    dcc.Graph(id='graph-gdpPercap'),
    dcc.Graph(id='graph-pop')
], style={'width': '50%', 'margin': 'auto', 'marginTop': 100, 'border': '1px solid black', 'padding': 20, 'borderRadius': 10, 'textAlign': 'center', 'backgroundColor': '#f0f0f0'})

@callback(
    Output('graph-gdpPercap', 'figure'),
    Input('dropdown-selection', 'value'),
)
def update_graph(selected_country):
    filtered_df = df[df.country == selected_country]
    fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'Renda per capita em {selected_country}')
    return fig

@callback(
    Output('graph-pop', 'figure'),
    Input('dropdown-selection', 'value'),
)
def update_graph(selected_country):
    filtered_df = df[df.country == selected_country]
    fig = px.line(filtered_df, x='year', y='pop', title=f'População em {selected_country}')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)