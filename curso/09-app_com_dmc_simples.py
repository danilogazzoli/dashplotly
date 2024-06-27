from dash import Dash, html, callback, Output, Input
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

#Link dos icones >> https://icon-sets.iconify.design/
#Link da documentação >> https://www.dash-mantine-components.com/dash-iconify

#aplicativo
app = Dash(__name__)

Timeline = dmc.Timeline(
    id='timeline-git',
    active=1,
    bulletSize=15,
    lineWidth=2,
    children=[
        dmc.TimelineItem(
            title="New Branch",
            children=[
                dmc.Text(
                    [
                        "You've created new branch ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                        " from master",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Commits",
            children=[
                dmc.Text(
                    [
                        "You've pushed 23 commits to ",
                        dmc.Anchor("fix-notification", href="#", size="sm"),
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="Pull Request",
            lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "You've submitted a pull request ",
                        dmc.Anchor(
                            "Fix incorrect notification message (#178)",
                            href="#",
                            size="sm",
                        ),
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            [
                dmc.Text(
                    [
                        dmc.Anchor(
                            "Pastura",
                            href="https://github.com/",
                            size="sm",
                        ),
                        " left a comment on your pull request",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
            title="Code Review",
        ),
    ],
)


container_pag1=html.Div([
    html.H1("Git Hub - Eva"),
    html.Br(),
    dmc.Button(
            id='button_next',
            children="Próxima Etapa",
            leftIcon=DashIconify(icon="fluent:database-plug-connected-20-filled")
    ),
    html.Br(),
    html.Br(),
    Timeline,
    html.Br(),
    dbc.Fade([
        dmc.Alert("You finish!", title="Success!", color="green", icon=DashIconify(icon="mdi:sucess-outline")),
    ],id="fade",is_in=False,appear=False)
])


app.layout = html.Div([
    container_pag1    
])


@callback(
    [Output('timeline-git', 'active'),
     Output('fade', 'is_in')],
    Input('button_next', 'n_clicks')
)

#Função que gera o gráfico
def update(n_clicks):
    alert = False
    if n_clicks == None:
        n_clicks = 0
    elif n_clicks > 3:
        n_clicks = 3
        alert = True
    return n_clicks, alert


#Rodando o app localmente
if __name__ == '__main__':
    app.run(debug=True)