# -*- coding: utf-8 -*-

# Import packages
import dash
from dash import dcc
from dash import html
from dash import dash_table
import pandas as pd
from dash.dependencies import Input, Output

# Incorporate data
df = pd.read_csv('Datenbasis/Krebsdaten.csv', encoding="latin-1", sep=';', decimal=',')

# Initialize the app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1('Krebsdashboard Deutschland'),
    html.H2('Zahlen pro 100 000 Einwohner'),

dash_table.DataTable(
        id='datatable',
        data=df.to_dict('records'),
        columns=[{'name': col, 'id': col} for col in df.columns],
        page_size=5,
    ),
])


# Callbacks
@app.callback(
    Output('datatable', 'data'),
    [Input('filter-input', 'value'), Input('sort-dropdown', 'value')]
)
def update_table(filter_value, sort_value):
    var = df[df['Krebsart'].str.contains(filter_value)]
    return var.to_dict('records')


if __name__ == '__main__':
    app.run(debug=True, port=8051)
