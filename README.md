# DSE_Projekt_SoSe2023
# Krebs Dashboard Readme

Dieses Krebs-Dashboard ist ein Projekt im Rahmen des Studiengangs Data Science Management an der Hochschule Neu Ulm. Es wurde im Rahmen der Vorlesung "Data Science Ecosystems" entwickelt. Das Ziel des Projekts ist es, die Prävalenzzahlen von Krebserkrankungen zu visualisieren, basierend auf den Daten, die von krebsdaten.de bereitgestellt werden.

## Technologien

Das Krebs-Dashboard wurde mit den folgenden Technologien entwickelt:

- Python: Die Programmiersprache Python wurde verwendet, um die Daten zu analysieren und das Dashboard zu erstellen.
- Pandas: Die Python-Bibliothek Pandas wurde genutzt, um die Daten aus der CSV-Datei zu laden und zu verarbeiten.
- Docker: Docker wurde verwendet, um das Dashboard in einem isolierten Container auszuführen und die Abhängigkeiten zu verwalten.
- Plotly Dash: Das Dashboard wurde mit Plotly Dash erstellt, einer Python-Bibliothek zur Erstellung interaktiver Webanwendungen.
- GitHub: Das Projekt und alle zugehörigen Unterlagen sind auf GitHub unter dem folgenden Link verfügbar: [https://github.com/malikljajic/DSE_Projekt_SoSe2023.git](https://github.com/malikljajic/DSE_Projekt_SoSe2023.git).

## Funktionen des Dashboards

Das Krebs-Dashboard bietet folgende Funktionen:

- Gesamttrendkurve: Das Dashboard zeigt eine Gesamttrendkurve der Krebserkrankungen im Verlauf.
- Top 5 Krebsarten: Über ein Dropdown-Menü können die Top 5 Krebsarten pro Jahr in einer Tabelle angezeigt werden.
- Prozentuale Verteilung: Das Dashboard berechnet die prozentuale Verteilung der Top 5 Krebsarten im Verhältnis zum Gesamtvorkommen und stellt sie in einem Balkendiagramm dar.

## Projektmitglieder

Das Projekt wird von folgenden Mitgliedern geleitet:

- Arezu Wafa (GitHub-Benutzername: arwa9526)
- Malik Ljajic (GitHub-Benutzername: malikljajic)

## Projekt-Repository

Das gesamte Projekt, einschließlich des Dashboards und der Unterlagen, ist im folgenden GitHub-Repository verfügbar: [https://github.com/malikljajic/DSE_Projekt_SoSe2023.git](https://github.com/malikljajic/DSE_Projekt_SoSe2023.git)

## Anleitung zur Verwendung

Folgen Sie diesen Schritten, um das Krebs-Dashboard lokal auszuführen:

1. Stellen Sie sicher, dass Python auf Ihrem System installiert ist (Version X.X oder höher).
2. Klonen Sie das Projekt-Repository von GitHub: `git clone https://github.com/malikljajic/DSE_Projekt_SoSe2023.git`.
3. Navigieren Sie in das Projektverzeichnis: `cd DSE_Projekt_SoSe2023`.
4. Erstellen Sie eine virtuelle Python-Umgebung (optional): `python -m venv venv`.
5. Aktivieren Sie die virtuelle Umgebung (optional): `source venv/bin/activate`.
6. Installieren Sie die erforderlichen Abhängigkeiten: `pip install -r requirements.txt`.
7. Führen Sie das Dashboard aus: `python app.py`.
8. Öffnen Sie einen Webbrowser und gehen Sie zur URL `http://localhost:8050`, um das Krebs-Dashboard anzuzeigen.

Bitte beachten Sie, dass für die Ausführung des Dashboards Docker und Docker Compose nicht erforderlich sind. Diese Anleitung geht davon aus, dass Sie das Dashboard lokal ausführen möchten.

## Beitragende

Wir freuen uns über Beiträge zur Verbesserung des Krebs-Dashboards. Wenn Sie einen Fehler gefunden haben oder eine Verbesserung vorschlagen möchten, können Sie gerne einen Issue erstellen oder uns einen Pull-Request senden.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der [Lizenzdatei](LICENSE) des Projekts.
