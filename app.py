# -*- coding: utf-8 -*-

# Import packages
import dash
from dash import dcc
from dash import html
from dash import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Incorporate data
df = pd.read_csv('Datenbasis/Krebsdaten.csv', encoding="latin-1", sep=';', decimal=',', index_col='Krebsart')

# Initialize the app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1('Krebsdashboard'),

    html.Div([
        html.Label('Filter:'),
        dcc.Input(id='filter-input', type='text', value='', placeholder='Enter  Filter'),
    ]),

    html.Div([
        html.Label('Sort by:'),
        dcc.Dropdown(
            id='sort-dropdown',
            options=[
                {'label': 'Krebsart', 'value': 'Krebsart'},
                {'label': 'Anzahl der Fälle', 'value': 'Anzahl der Fälle'},
                {'label': 'Todesfälle', 'value': 'Todesfälle'},
                {'label': 'Überlebensrate', 'value': 'Überlebensrate'}
            ],
            value='Krebsart',
            clearable=False
        ),
    ]),

    dash_table.DataTable(
        id='datatable',
        data=df.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in df.columns],
        page_size=10,
    ),

    dcc.Graph(id='graph')
])


# Callbacks
@app.callback(
    Output('datatable', 'data'),
    [Input('filter-input', 'value'), Input('sort-dropdown', 'value')]
)
def update_table(filter_value, sort_value):
    var = df[df['Krebsart'].str.contains(filter_value)]
    return var.to_dict('records')


    Output('graph', 'figure'),
    [Input('datatable', 'data')]

def update_graph(data):
    # Daten für das Liniendiagramm
    x_data = [row['Jahr'] for row in data]
    y_data = [row['Anzahl Gesamtkrebsfälle'] for row in data]

    # Plotly Trace erstellen
    trace = go.Scatter(
        x=x_data,
        y=y_data,
        mode='lines',
        name='Liniendiagramm'
    )

    # Layout für das Liniendiagramm
    layout = go.Layout(
        title='Liniendiagramm',
        xaxis=dict(title='Jahr'),
        yaxis=dict(title='Anzahl Gesamtkrebsfälle')
    )

    return {'data': [trace], 'layout': layout}


if __name__ == '__main__':
    app.run(debug=True, port=8053)

