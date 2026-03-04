EPSILON = 0.1  # Technischer Schutzwert zur Vermeidung einer Division durch 0, Gross geschrieben, da eine Konstante (Python-Konvention, PEP 8)
T = 0.05 # Symmetrische Trend-Schwelle zur Bewertung von Verbesserungen oder Verschlechterungen

# Gewichtungen der Belastungsarten abhängig vom gewählten Profil
WEIGHTS = { 
    "general": {
        "work": 1.0,
        "learn": 0.0,
        "care": 1.0
    },
    "training": {
        "work": 1.0,
        "learn": 1.3,
        "care": 1.0
    },
    "care": {
        "work": 1.0,
        "learn": 0.0,
        "care": 1.5
    }
}

#Funktion zur Berechnung der Erholung
def calc_recovery(sleep_h, sport_h): 
    return sleep_h*2 + sport_h*1

# Berechnet die tägliche Belastung (Arbeit, Lernen, Care) mit den Gewichtungen des gewählten Profils
def calc_load(profile, work_h, learn_h, care_h): 
    w = WEIGHTS[profile]
    return work_h * w["work"] + learn_h * w["learn"] + care_h * w["care"]

# Berechnet die tägliche Balance als Verhältnis von Erholung zu Belastung (profilabhängig)       
def calc_balance(profile, sleep_h, sport_h, work_h, learn_h, care_h): 
    recovery = calc_recovery(sleep_h, sport_h)
    load = calc_load(profile, work_h, learn_h, care_h)
    return recovery / (load + EPSILON)

#Berechnet den Durchschnitt der eingegebenen Werte
def mean(values):
    return sum(values) / len(values)

# Bewertet den 14-Tage-Trend durch Vergleich zweier aufeinanderfolgender 7-Tage-Zeiträume
def trend_label(balances):
    if len(balances) < 14:
        return ("not_enough_data", len (balances))
    # Verwendet nur die letzten 14 Werte (falls mehr gespeichert sind)
    recent = balances[-14:] 
    week1 = recent[:7]
    week2 = recent[7:14]
    # Durchschnitt der beiden 7-Tage-Perioden speichern
    w1 = mean(week1)
    w2 = mean(week2)

    # Differenz der Wochenmittelwerte berechnen
    delta = w2 - w1
    # Trend anhand der Schwelle klassifizieren
    if delta > T:
        label = "better"
    # -T = delta kleiner als -T --> deutliche Verschlechterung
    elif delta < -T:
        label = "worse"
    else:
        label = "stable"
    # Werte werden als Tuple zurückgegeben, damit andere Teile des Programms damit arbeiten können.
    return label, w1, w2, delta
        