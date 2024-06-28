import dash
from dash import html
import dash_mantine_components as dmc

dash.register_page(__name__)

layout = html.Div([
    html.Div(
        children= dmc.Image(src='https://www.creativefabrica.com/wp-content/uploads/2022/07/11/Error-404-page-not-found-illustration-Graphics-33990706-1-1-580x435.jpg',
                            )
    )
])  

