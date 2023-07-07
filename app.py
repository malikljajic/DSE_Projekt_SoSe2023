# -*- coding: utf-8 -*-

# Import packages
import dash
from dash import dcc, Dash
from dash import html
from dash import dash_table
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go


# Incorporate data
df = pd.read_csv('Datenbasis/Krebsdaten.csv', encoding="latin-1", sep=';', decimal=',', index_col='Krebsart')

# Initialize the app
app: Dash = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1('Krebsdashboard Deutschland'),
    html.H2('Zahlen pro 100 000 Einwohner'),

    html.Div([
        html.Label('Sort by:'),
        dcc.Dropdown(
            id='sort-dropdown',
            options=[
                {'label': 'Krebsart', 'value': 'Krebsart'},
                {'label': 'Alter', 'value': 'Alter'},
                {'label': 'Jahr', 'value': 'Jahr'},
                {'label': 'Geschlecht', 'value': 'Geschlecht'}
            ],
            value='Krebsart',
            clearable=False
        ),
    ]),

    dash_table.DataTable(
        id='datatable',
        data=df.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in df.columns],
        page_size=5,
    ),


    dcc.Graph(
        figure={
          'data': [
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [19067, 19428, 19345, 20059, 20072, 19832, 19827, 19199, 18851, 18456, 17921, 17759, 17256, 17123, 16789, 16429],
              'type': 'line', 'name': 'Gesamtkrebs'},

           ],
           'layout': {
             'title': 'Gesamtkrebs'
          }
      }
)
])

# Callbacks
@app.callback(
    Output('datatable', 'data'),
    [Input('filter-input', 'value'), Input('sort-dropdown', 'value')]
)
def update_table(filter_value, sort_value):
    var = df[df['Krebsart'].str.contains(filter_value)]
    return var.to_dict('records')

dcc.Graph('data')

if __name__ == '__main__':
    app.run(debug=True, port=8053)
