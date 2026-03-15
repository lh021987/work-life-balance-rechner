from logic import calc_balance, trend_label
from storage import save_balance, load_balances

def choose_profile():

    profiles = {
        "1": "general",
        "2": "training",
        "3": "care"
    }

    print("Willkommen beim Work-Life-Balance-Rechner")
    print()
    print("Bitte wähle das Profil, das am besten zu deiner aktuellen Situation passt:")
    print("1 - Klassischer Alltag")
    print("2 - Weiterbildung oder intensives privates Lernen")
    print("3 - Care-Verantwortung")
    print()

    # Schleife läuft solange, bis eine gültige Auswahl getroffen wurde.
    while True:
        choice = input("Deine Auswahl (1-3): ").strip() # Tippfehler werden abgefangen.

        # Prüfen, ob die Eingabe als Key im Dicitionairy existiert.
        if choice in profiles:
            return profiles[choice]
        else:
            print("Dieses Profil gibt es nicht. Bitte erneut (1-3) eingeben.")

profile = choose_profile()
print("Gewähltes Profil:", profile)
       

def ask_float(prompt, min_val=0.0, max_val=None, warn_below=None, warn_above=None):
    while True:
        raw = input(prompt).strip()
        #Komma akzeptieren
        raw = raw.replace(",",".")

        try:
            value = float(raw)
        except ValueError:
            print("Ungültige Eingabe: Bitte gib eine Zahl ein.")
            continue

        if value < min_val:
            print (f"Bitte gib einen Wert ab >= {min_val} ein.")
            continue

        if max_val is not None and value > max_val:
            print (f"Bitte gib einen Wert bis höchstens <= {max_val} ein.")
            continue

        #Plausibilitätswarnung
        unusual = False
        if warn_below is not None and value < warn_below:
            unusual = True
        if warn_above is not None and value > warn_above:
            unusual = True

        if unusual:
            answer = input(f"Der eingegebene Wert {value} ist eher ungewöhnlich. Möchtest du ihn trotzdem übernehmen? (j/n) ").strip().lower()
            if answer not in ("j", "ja"):
                print("Okay, bitte erneut eingeben.")
                continue

        return value
    
work = ask_float("Arbeitszeit heute (in Stunden): ", max_val=16, warn_above=12)
learn = ask_float("Lernzeit heute (in Stunden): ", max_val=12, warn_above=10)
care = ask_float("Care-Verantwortung heute (in Stunden): ", max_val=16, warn_above=10)
sleep = ask_float("Schlaf heute (in Stunden): ", max_val=16, warn_below=3, warn_above=12)
sport = ask_float("Sport heute (in Stunden): ",max_val=8, warn_above=4)

# Balance berechnen
balance = calc_balance(profile, sleep, sport, work, learn, care)
print("\nDeine Tagesbalance beträgt: ", round(balance,3))

# Balance speichern
save_balance(balance)
2
# Alle bisherigen Balances laden
balances = load_balances()

# Trend berechnen
result = trend_label (balances)

if result[0] == "Nicht genug Daten für eine Trendanalyse":
    print ("Trendanalyse noch nicht möglich.")
    print(f"Bisher erfasst: {result[1]} von 14 benötigten Tagen.")
    print("Bitte erfasse weitere Tage, um eine Trendanalye zu erhalten.")
else:
    label, w1, w2, delta = result

    if label == "better":
        trend_text = "Verbesserung"
        hint_text ="Die zweite Woche zeigt ein besseres Verhältnis zwischen Erholung und Belastung. Weiter so."
    elif label == "worse":
        trend_text = "Die Balance hat sich leicht verschlechtert"
        hint_text = "Vielleicht lohnt es sich, in den nächsten Tagen wieder bewusst Zeit für Erholung einzuplanen."
    else:
        trend_text = "Die Balance ist stabil geblieben"
        hint_text = "Zwischen den beiden Wochen gab es keine grösseren Veränderungen."

    # Ergebnisse ausgeben
    print("\nAuswertung der letzten 14 Tage:")
    print("Trend: ", trend_text)
    print("Durchschnitt Woche 1: ", round(w1,3))
    print("Durchschnitt Woche 2: ", round(w2, 3))
    print("Differenz:", round(delta, 3))
