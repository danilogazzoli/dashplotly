from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import numpy as np

df = pd.read_csv('./dados/roteirizacao.csv', delimiter = ';', encoding = 'utf-8',  usecols=['CD_DIR', 'CD_FIL','BAND','CD_FUN_GER', 'CD_FUN_CAL'])

df['BAND'] = df['BAND'].str.upper()
df['Gerente'] = np.where(df['CD_FUN_GER'] == 0, 0, 1)
df['Coordenador'] = np.where(df['CD_FUN_CAL'] == 0, 0, 1)

df = df.groupby(by=['CD_DIR', 'BAND'])\
    .agg({'CD_FIL':'count', 
        'Gerente':'sum', 
        'Coordenador':'sum', 
        }).reset_index()

df.rename(columns={'CD_FIL':'QTD_FILIAIS'}, inplace=True)
filiais = ['TODOS']
filiais.extend(df['BAND'].unique().tolist())


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([ 
    html.H1('ROTEIRIZAÇÃO', style={'textAlign': 'center', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 40, 'color': '#13538a'}),
    html.Div('DADOS DE ORGANIZAÇÃO DAS LOJAS DO GRUPO BAHIA', style={'textAlign': 'center', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 15, 'color': 'black'}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div('FILTRO POR BANDEIRA', style={'textAlign': 'left', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 15, 'color': 'black'}),
            dcc.RadioItems(filiais, 'CASAS BAHIA', style={'textAlign': 'left', 'font-family':'Arial', "font-weight": "bold", 'fontSize': 15, 'color': 'black'}, id='radio-selection'),
        ]),
    ]),
    
    dbc.Row([
        dbc.Col([
            html.H4(children='QUANTIDADE DE LOJAS POR DIRETORIA', style={'textAlign': 'center', 'color':'#05237a', 'font-weight':'bold', 'font-family':'Arial'}),
            dcc.Graph(id='graph-dados', style={'height':'250px', 'width':'650px', 'textAlign': 'center'})
        ], width=6, align='center', style={'display':'flex', 'flex-direction':'column', 'align-items':'center'}),
        dbc.Col([
            html.H4(children ="% LOJAS COM GERENTES", style={'color':'#05237a', 'font-weight':'bold', 'font-family':'Arial'}),
            dbc.Progress(label="33%", value=33,id = 'progress_ger', color='#13538a', style={'width':'50%', 'height':'30px', 'border-radius':'15px'}),
            html.Br(),
            html.H4(children = "% LOJAS COM CAL", style={'color':'#05237a', 'font-weight':'bold', 'font-family':'Arial'}),
            dbc.Progress(label="33%", value=33, id = 'progress_cal',color='#13538a', style={'width':'50%', 'height':'30px', 'border-radius':'15px'})
        ], width=6)
    ]),

    ], style={'margin': 'auto', 'marginTop': 100, 'border': '1px solid grey', 'padding': 20, 'textAlign': 'center'}
)



def build_line_chart(filtered_df):
    fig = px.line(filtered_df, x='CD_DIR', y='QTD_FILIAIS')
   
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='white',
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(title="Diretoria"),
        yaxis=dict(title="Quantidade de lojas"),
        title={
                'text': "",
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
        linecolor='black',
        zeroline=False,
        showline=False,
        gridcolor='lightgrey',
    )   
    return fig

def filter_df(value):
    if value != 'TODOS':
        filtered_df = df[df['BAND'] == value]
    else:
        filtered_df = df
    return filtered_df

def calc_progress(filtered_df):
    value_ger = filtered_df['Gerente'].sum()/filtered_df['QTD_FILIAIS'].sum() * 100
    label_ger = str(int(value_ger)) + '%'

    value_cal = filtered_df['Coordenador'].sum()/filtered_df['QTD_FILIAIS'].sum() * 100
    label_cal = str(int(value_cal)) + '%'

    return value_ger, label_ger, value_cal, label_cal

@callback(
    [Output('graph-dados', 'figure'),
     Output('progress_ger', 'value'),
     Output('progress_ger', 'label'),
     Output('progress_cal', 'value'),
     Output('progress_cal', 'label')],        
    Input('radio-selection', 'value'),
)
def update_graph(value):
    filtered_df = filter_df(value)
    fig = build_line_chart(filtered_df)
    value_ger, label_ger, value_cal, label_cal = calc_progress(filtered_df)
    return fig, value_ger, label_ger, value_cal, label_cal

if __name__ == '__main__':
    app.run_server(debug=True)