from dash import Dash, html, callback, Output, Input
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

#Link dos icones >> https://icon-sets.iconify.design/

#aplicativo
app = Dash(__name__)

TimeLineItemNewBranch = dmc.TimelineItem(
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
        )

TimeLinePush = dmc.TimelineItem(
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
        )

TimeLineSubmitted =  dmc.TimelineItem(
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
        )

TimeLineCommit =  dmc.TimelineItem(
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
        )



Timeline = dmc.Timeline(
    id='timeline-git',
    active=1,
    bulletSize=15,
    lineWidth=2,
    children=[
        TimeLineItemNewBranch,
        TimeLinePush,
        TimeLineSubmitted,
        TimeLineCommit
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

container_pag2 = dmc.Prism(
    language="python",
    children="""# Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, summ = nums[0], nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            summ = max(summ, curr)
        return summ""",
)

app.layout = html.Div([
    dmc.Tabs(
    [
        dmc.TabsList(
            [
                dmc.Tab("Git", value="git"),
                dmc.Tab("Código", value="messages"),
            ]
        ),
        dmc.TabsPanel(container_pag1, value="git", pb="xs"),
        dmc.TabsPanel(container_pag2, value="messages", pb="xs"),
    ],
    value="git",
    inverted=False,
),
    
])


@callback(
    [Output('timeline-git', 'active'),
     Output('fade', 'is_in')],
    Input('button_next', 'n_clicks')
)
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