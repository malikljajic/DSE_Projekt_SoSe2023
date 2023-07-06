import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv('Datenbasis/Krebsdaten.csv', encoding="latin-1", sep=';', decimal=',')

# Filter für die gewünschten Infos erstellen
info =['Krebsart','Alter','Geschlecht','Prävalenzzeitraum']
# Filter für die gewünschten Jahre erstellen
jahre = ['2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']

#lamda bedeutet auf jede Spalte umsetzen
df[jahre] = df[jahre].apply(lambda x: pd.to_numeric(x, errors='coerce'))

# Die 5 höchsten Werte für jede Spalte ermitteln
top_5_values = df[jahre].max().sort_values(ascending=False)[:5]

# Ergebnis anzeigen
print(df[info],df[jahre])
