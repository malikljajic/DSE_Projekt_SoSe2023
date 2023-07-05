from dash import Dash, dcc, html
import plotly.graph_objs as go

# Daten für den Graphen
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 6, 8, 10]

# Plotly Trace erstellen
trace = go.Scatter(
    x=x_data,
    y=y_data,
    mode='lines',
    name='Linien'
)

# Layout für das Dash-Dashboard
layout = go.Layout(
    title='Test',
    xaxis=dict(title='Jahr'),
    yaxis=dict(title='Anzahl Gesamtkrebsfälle')
)

# Dash-App erstellen
app = Dash(__name__)

# Layout der Dash-App definieren
app.layout = html.Div(children=[
    html.H1(children='Test'),

    dcc.Graph(
        id='graph',
        figure={
            'data': [trace],
            'layout': layout
        }
    )
])

# Dash-App starten
if __name__ == '__main__':
    app.run_server(debug=True, port=8054)
