from dash import Dash, html, dash_table
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Exemplo com dados', style={'textAlign': 'center'}),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
])



if __name__ == '__main__':
    app.run_server(debug=True)