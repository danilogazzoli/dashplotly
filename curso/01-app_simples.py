from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div([
    html.Div('Hello World', style={'textAlign': 'center', 'fontSize': 40, 'color': 'blue', 'width': '50%'}),
    html.Br(),
    html.H1(children=html.B('Olá Mundo'))

], style={'width': '50%', 'margin': 'auto', 'marginTop': 100, 'border': '1px solid black', 'padding': 20, 'borderRadius': 10, 'textAlign': 'center', 'backgroundColor': '#f0f0f0'})


if __name__ == '__main__':
    app.run_server(debug=True)