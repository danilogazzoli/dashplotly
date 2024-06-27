from dash import Dash, html, callback, Output, Input, State
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = pd.DataFrame({"First Name": ['John', 'Paul', 'George', 'Ringo'],
                   "Last Name": ['Lennon', 'McCartney', 'Harrison', 'Starr'],
                   "Role": ['Guitar', 'Bass', 'Guitar', 'Drums']})

app.layout = html.Div([
    html.H1('The Beatles'),
    html.Br(),
    dbc.Card(
    [
        dbc.CardBody([
            html.H4('Select a Beatle:', className='card-title'),
            dbc.RadioItems(
                options=[
                    {'label': 'John', 'value': 'John'},
                    {'label': 'Paul', 'value': 'Paul'},
                    {'label': 'George', 'value': 'George'},
                    {'label': 'Ringo', 'value': 'Ringo'}
                ],
                value='John',
                id='beatle-selector'
            ),
        ]),    
    ]),
    html.Div(id='output')
])


if __name__ == '__main__':
    app.run_server(debug=True)