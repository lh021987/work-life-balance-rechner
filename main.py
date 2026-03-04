from logic import calc_balance, trend_label


def choose_profile():

    profiles = {
        "1": "general",
        "2": "training",
        "3": "care"
    }

    print("Profil auswählen:")
    print("1 - General (klassisch)")
    print("2 - Training (Weiterbildung)")
    print("3 - Care")

    # Schleife läuft solange, bis eine gültige Auswahl getroffen wurde.
    while True:
        choice = input("Bitte eine Zahl eingeben (1-3): ").strip() # Tippfehler werden abgefangen.

        # Prüfen, ob die Eingabe als Key im Dicitionairy existiert.
        if choice in profiles:
            return profiles[choice]
        else:
            print("Ungültige Auswahl. Bitte erneut eingeben.")

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
            print("Bitte eine Zahl eingeben.")
            continue

        if value < min_val:
            print (f"Bitte einen Wert >= {min_val} eingeben.")
            continue

        if max_val is not None and value > max_val:
            print (f"Bitte einen Wert <= {max_val} eingeben")
            continue

        #Plausibilitätswarnung
        unusual = False
        if warn_below is not None and value < warn_below:
            unusual = True
        if warn_above is not None and value > warn_above:
            unusual = True

        if unusual:
            answer = input(f"Ungewöhnlicher Wert {value} Bitte bestätigen, falls korrekt. (j/n)").strip().lower()
            if answer not in ("j", "ja"):
                print("Okay, bitte erneut eingeben.")
                continue

        return value
    
work = ask_float("Arbeitszeit in Stunden: ", max_val=16, warn_above=12)
learn = ask_float("Lernzeit in Stunden: ", max_val=12, warn_above=10)
care = ask_float("Care-Zeit in Stunden: ", max_val=16, warn_above=10)
sleep = ask_float("Schlaf in Stunden: ", max_val=16, warn_below=3, warn_above=12)
sport = ask_float("Sport in Stunden: ",max_val=8, warn_above=4)

balance = calc_balance(profile, sleep, sport, work, learn, care)
print("\nBerechnete Tagesbalance: ", round(balance,3))