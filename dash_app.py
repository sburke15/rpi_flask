import dash
import dash_core_components as dcc 
import dash_html_components as html 
from server import server

app = dash.Dash(name='mydash', sharing=True, server=server, url_base_pathname='/mydash')

app.layout = html.Div(children=[
    html.H1(children='Dash Test'),
    dcc.Graph(
        id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        }
    )
])

