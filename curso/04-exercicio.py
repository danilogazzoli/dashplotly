from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_excel('.\\dados\\vendas_ficticias.xlsx')

app = Dash(__name__)

app.layout = html.Div([
    html.Div('Hello World', style={'textAlign': 'center', 'fontSize': 20, 'color': 'red', 'width': '50%', 'margin': 'auto'}),
    html.Div('Hello World 2', style={'textAlign': 'left', 'fontSize': 30, 'color': 'blue', 'width': '50%', 'margin': 'auto'}),
    html.Div('Hello World 3', style={'textAlign': 'right', 'fontSize': 40, 'color': '#11E9E9 ', 'width': '50%', 'margin': 'auto'}),
    html.Br(),
    html.H1(children=html.B('Olá Mundo')),
    dcc.Dropdown(df.Categoria.unique(), 'Móveis', id='dropdown-selection'),
    #dash_table.DataTable(id='table', data=df.to_dict('records'), page_size=10),
    dash_table.DataTable(
        id='table',
        data=df.to_dict('records'),
        columns=[
            {"name": i, "id": i} for i in sorted(df.columns)
        ],

        filter_query=''
    ),

    dcc.Graph(id='graph-venda'),
], style={'width': '50%', 'margin': 'auto', 'marginTop': 100, 'border': '1px solid black', 'padding': 20, 'borderRadius': 10, 'textAlign': 'center', 'backgroundColor': '#f0f0f0'})


@callback(
    Output('graph-venda', 'figure'),
    Input('dropdown-selection', 'value'),
)
def update_graph(value):
    filtered_df = df[df.Categoria == value]
    fig = px.bar(filtered_df, x='Filial', y='Valor de venda', title='Valor de venda por filial', color='Filial')
    return fig


@callback(
    Output('table', "data"),
    Input('dropdown-selection', 'value')
    )
def update_table(filter):
    dff = df
    dff = dff.loc[dff['Categoria'].str.contains(filter)]
    return dff.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)