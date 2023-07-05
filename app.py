# Import packages
import pandas as pd
from dash import Dash, html, dash_table

# Incorporate data
df = pd.read_csv('Datenbasis\Krebsdaten.csv', encoding="latin-1", sep=';', decimal=',', index_col='Krebsart')

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Krebsdashboard'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
