import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv('Datenbasis\Krebsdaten.csv', encoding="latin-1", sep=';', decimal=',', index_col='Krebsart')
# Report erstellen
# report = df.describe()
df.sort_index()
# größte Werte ausgeben
# fivelargestvalues=df.nlargest(5,['2008'])
fivelargestvalues = df.sort_values(by=['2008'])
# Report anzeigen
print(fivelargestvalues.head(5))
print('TestArezo')

