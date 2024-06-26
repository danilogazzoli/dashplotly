from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('.\\dados\\roteirizacao.csv', delimiter = ';', encoding = 'utf-8',  usecols=['CD_DIR', 'CD_FIL','BAND'])

df['BAND'] = df['BAND'].str.upper()

df_group = df.groupby(['CD_DIR','BAND']).count()
df_group = df_group.reset_index()
df_group.rename(columns={'CD_FIL':'QTD_FILIAIS'}, inplace=True)

app = Dash(__name__)

app.layout = html.Div([ 
    html.Div('ROTEIRIZAÇÃO', style={'textAlign': 'center', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 40, 'color': '#13538a'}),
    html.Div('DADOS DE ORGANIZAÇÃO DAS LOJAS DO GRUPO BAHIA', style={'textAlign': 'center', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 15, 'color': 'black'}),
    html.Div('FILTRO POR BANDEIRA', style={'textAlign': 'left', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 15, 'color': 'black'}),
    dcc.RadioItems(df_group['BAND'].unique(), 'CASAS BAHIA', style={'textAlign': 'left', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 15, 'color': 'black'}, id='radio-selection'),
    dcc.Graph(id='graph-dados'),
    ], style={'margin': 'auto', 'marginTop': 100, 'border': '1px solid grey', 'padding': 20, 'textAlign': 'center'})


@callback(
    Output('graph-dados', 'figure'),
    Input('radio-selection', 'value'),
)
def update_graph(value):
    filtered_df = df_group[df_group.BAND == value]
    fig = px.line(filtered_df, x='CD_DIR', y='QTD_FILIAIS')
   
    fig.update_layout(
        plot_bgcolor='white',
        xaxis=dict(title="Diretoria"),
        yaxis=dict(title="Quantidade de lojas"),
        title={
                'text': "Quantidade de lojas por diretoria",
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},

        font_family="Arial",
        font_weight="bold",
        font_color="#13538a",
    )    

    fig.update_xaxes(
        mirror=True,
        ticks='outside',
        showline=True,
        linecolor='black',
        gridcolor='lightgrey'
    )
    fig.update_yaxes(
        mirror=True,
        ticks='outside',
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
    )    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)