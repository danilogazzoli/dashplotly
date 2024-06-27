from dash import Dash, html, Output, Input, State, callback
import dash_bootstrap_components as dbc
import pandas as pd

#https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

df = pd.DataFrame(
    {
        "First Name": ["Leandro", "Gabriel", "Luana", "Marilza"],
        "Last Name": ["Pastura", "Nunes", "Oliveira", "Toniato"],
    }
)

app.layout = html.Div([
    html.H1("Essa página contém Bootstrap!", id='title-hello'),
    html.Br(),
    dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Card", className="card-title"),
                html.P(
                    "Esse é um exemplo de um card ",
                    className="card-text",
                ),
                dbc.Button("Clique aqui para ver mais", id = 'fade-button', color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
    ),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div("Barra de progresso na coluna 1"),
            dbc.Progress(label="33%", value=25)
        ], width=4),
        dbc.Col([
            html.Div("Barra de progresso na coluna 2"),
            dbc.Progress(label="33%", value=25)
        ], width=4),
        dbc.Col([
            html.Div("Barra de progresso na coluna 3"),
            dbc.Progress(label="33%", value=25)
        ], width=4),
    ]),
    html.Br(),
    html.Br(),
    dbc.Fade([
    html.Div("Esses são os contribuidores dessa página:"),
    dbc.Row([
        dbc.Col([
            dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
        ], width=6),
        dbc.Col([
            html.Div(
            [
                dbc.Label("Nome"),
                dbc.Input(type="nome", id="example-nome", placeholder="Ex: Marilza Toniato"),
                dbc.FormText(
                    "Qual o seu nome?",
                color="secondary",
                ),
            ],
            className="mb-3",
        )
    ], width=6)
    ])
    ],id="fade",is_in=False,appear=False)
], style={'padding-left':40, 'padding-right':40})


@app.callback(
    [Output("fade", "is_in")],
    [Input("fade-button", "n_clicks")],
    [State("fade", "is_in")],
)
def toggle_fade(n, is_in):
    if not n:
        # Button has never been clicked
        return False
    return not is_in

@app.callback(Output("fade", "is_in"),     
              [Input("fade-button", "n_clicks")], 
              [State("fade", "is_in")] )
def toggle_fade(n, is_in):     
    if not n:         # Button has never been clicked
        return False
    return not is_in



@callback(
    Output("title-hello", "children"),
    Input("example-nome", "value"),
)

def check_validity(value):
    if value == None or value == '':
        return "Olá Visitante!"
    elif value in ['Marilza', 'Leandro', 'Gabriel', 'Luana']:
        return  'Oi {}, você é um contribuidor!'.format(value)
    else:
        return  'Oi {}, essa página contém Bootstrap!'.format(value)


if __name__ == "__main__":
    app.run_server()