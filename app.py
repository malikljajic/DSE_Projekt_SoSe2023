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
              'type': 'line', 'name': 'weiblich 0-44'},
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [12940, 12837, 13154, 13132, 12718, 12690, 12670, 12131, 11784, 11765, 11476, 11425, 10949, 10584, 10393],
              'type': 'line', 'name': 'männlich 0-44'},
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [23427, 23880, 24902, 26718, 28913, 30055, 30016, 30375, 30842, 31148, 31036, 31066, 30345, 29465, 28992, 27364],
              'type': 'line', 'name': 'weiblich 45-54'},
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [17792, 18135, 19378, 20278, 20731,21142, 21697, 21579, 21034, 21446, 21423, 20775, 20050, 19764, 18838, 17886],
              'type': 'line', 'name': 'männlich 45-54'},
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [37275, 36710, 36622, 37694,	41002, 41119, 39639, 40020, 40219, 40905, 40521, 40988,	41574, 41669, 42078, 42485],
              'type': 'line', 'name': 'weiblich 55-64'},
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [49626,47713, 47991, 48641, 47778, 46076, 46479, 47186, 46729, 45890, 45931, 46635, 47281, 47948, 48082, 48266],
              'type': 'line', 'name': 'männlich 55-64'},
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [44709, 46284, 47935, 51437, 54448, 54867, 52832, 51875, 49980, 50080, 48707, 47785, 45282, 46089, 44563, 43866],
              'type': 'line', 'name': 'weiblich 65-74'},
             {'x': [2004, 2005, 2006, 2007, 2008,2009,2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019],
              'y': [70.272, 71487, 76912, 81763, 81841, 82004, 79584, 78060, 74918, 71369, 68629, 67175, 65664, 65487, 64645, 65044],
              'type': 'line', 'name': 'männlich 65-74'}

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
