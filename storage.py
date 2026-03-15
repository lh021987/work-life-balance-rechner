from pathlib import Path
import csv
from datetime import date

BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "balances.csv"

# Speichert den berechneten Balance-Wert zusammen mit dem heutigen Datum in einer CSV-Datei. Jeder Programmaufruf erzeugt eine neue Zeile
def save_balance(balance):

    # aktuelles Datum ermitteln (ohne Uhrzeit)
    today = date.today()

    # Datei im "append"-Modus öffnen
    # Falls die Datei existiert -> neue Zeile anhängen
    # Falls nicht -> Datei automatisch erstellen
    with open(FILE_PATH,"a", newline="") as file:

        # CSV-Writer erzeugen, der Daten in CSV-Format schreibt
        writer = csv.writer(file)

        # Eine neue Zeile schreiben: [Datum, Balancewert]
        writer.writerow([today, balance])


# Lädt alle gespeicherten Balancewerte aus der CSV-Datei und gibt sie als Liste zurück
def load_balances():

     # Leere Liste erstellen, in der später alle Balancewerte gespeichert werden
    balances = []

    # Wenn die Datei nicht vorhanden ist, wird eine leere Liste zurückgegeben
    if not FILE_PATH.exists():
        return balances

    # Datei im Lesemodus öffnen
    with open(FILE_PATH,"r", newline="") as file:

        # CSV_Reader erzeugen, um die Datei zeilenweise zu lesen
        reader = csv.reader(file)

        # Jede Zeile der CSV-Datei durchlaufen
        for row in reader:
            if len(row) < 2:
                continue
            # Der Balancewert steht in der zweiten Spalte (Index)
            # CSV liest Werte automatisch als String -> deshalb Umwandlung zu float
            try:
                balance = float(row[1])
            except ValueError:
                continue

            #Balancewert zur Liste hinzufügen
            balances.append(balance)

        # Liste mit allen Balancewete zurückgeben
        return balances
    