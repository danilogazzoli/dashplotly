import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Home page'),
    html.Div('This is the content of the home page'),
    html.Br()
])  

