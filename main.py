import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv('Datenbasis/Krebsdaten.csv', encoding="latin-1", sep=';', decimal=',')

# Filter für die gewünschten Jahre erstellen
jahre = ['2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
filtered_df = df.copy()

# Die 5 höchsten Werte für jede Spalte ermitteln
#lamda bedeutet auf jede Spalte umsetzen
filtered_df[jahre] = filtered_df[jahre].apply(lambda x: pd.to_numeric(x, errors='coerce'))

# Spalten in den Datentyp 'float' umwandeln
top_5_values = filtered_df[jahre].max().sort_values(ascending=False)[:5]

# Ergebnis anzeigen
print(top_5_values)
