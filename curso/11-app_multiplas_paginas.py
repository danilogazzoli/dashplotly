import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Dash com multiplas páginas', style={'textAlign': 'center', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 40, 'color': '#13538a'}),
    html.Div('Clique nos links para navegar entre as páginas', style={'textAlign': 'center', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 15, 'color': 'black'}),
    html.Br(),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page['relative_path'])

        ) for page in dash.page_registry.values()

    ]), 
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)


