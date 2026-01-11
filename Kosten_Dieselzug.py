# Variabeln
gewicht_kg = (12.320 + 98) * 1000
v = 110 / 3.6 # zu beschleunigende Geschwindigkeit in m/s
n_ges = 0.22 # Gesamtwirkungsgrad
h = 300 # Höhenmeter
g = 9.81 # Gravitationskonstante
distanz_fahrt = 60000 # in m
rotierende_massen = 10
a = 1 # Beschleunigung in m/s^2
p = 1.23 # Luftdichte
Cd = 0.85 # Luftwiderstandsbeiwert
A = 10  # Querschnittsfläche in m^2
t_end = v / a  # Beschleunigugnszeit
t = 0  # Wechselvariabel 
dt = 0.00001 # Zeitintervall Messung
durchschnitt_distanz_stopps = 60 / 16 * 1000 
E_Luft_ges_eine_Beschleunigung = 0  
Cr = 0.001 # Rollwiderstand
Fn = gewicht_kg * g # Normalkraft
energie_gehalt = 9.8 # Energiegehalt an kWh pro Liter Diesel
preis_l = 1.74 # Preis pro Liter Diesel
stopps = 16 # Anzahl Stopps eine Fahrt
Fahrten_eine_woche = 172 # Anzahl Fahrten in einer Woche
Wochen_ein_Jahr = 52 # Anzahl Wochen in einem Jahr
Kosten_list = []
x = 1 # For-Schleife Variabel
dauer_beobachtung = 30 # Jahresdauer der Beobachtung
investitionskosten = 4650000 # Kosten für Anschaffung eines Zuges
Energie_kosten_komplett = 0
Anzahl_züge = 2
rekuperationswert = 0.3
Kosten_Bau_Tankstelle = 900000 

# Berechnungen
# Rollwiderstand über eine Fahrt:
F_Roll = Cr * Fn
E_Roll = F_Roll * distanz_fahrt / 3600000
# kinetische Energie bis zur beschleunigenden Geschwindigkeit:
E_kin = gewicht_kg / 2 * v**2 / 3600000
# Aufschlag rotierende Massen:
E_kin = E_kin / 100 * rotierende_massen + E_kin
# potentielle Energie für Höhenmeter: 
E_pot = gewicht_kg * g * h / 3600000
# Luftwiderstand bei Beschleunigung und Abbremsen:
while t < t_end:
    v = a * t  
    Fd = 0.5 * p * A * Cd * v**2 
    d = v * dt 
    E_Luft_zeitintervall = Fd * d / 3600000  
    E_Luft_ges_eine_Beschleunigung += E_Luft_zeitintervall
    t += dt  
E_Luft_ges_Beschleunigung_Abbremsen_eine_Fahrt = E_Luft_ges_eine_Beschleunigung * 32
# Luftwidersand bei konstanter Geschwindigkeit:
Fd = 0.5 * p * A * Cd * v**2 
d = durchschnitt_distanz_stopps - 2 * 0.5 * a * t_end**2
E_Luft_konstant = Fd * d / 3600000  
E_Luft_ges_konstant_eine_Fahrt = E_Luft_konstant * stopps
E_Luft_ges = E_Luft_ges_konstant_eine_Fahrt + E_Luft_ges_Beschleunigung_Abbremsen_eine_Fahrt
# Rekuperation kinetische Energie: 
E_rekuperation_kin = E_kin * rekuperationswert
# Rekuperation potentielle Energie:
E_rekuperation_pot = E_pot * rekuperationswert
# Energie für Instanthaltung Geschwindigkeit:
E_konstante_geschwindigkeit = E_Roll + E_Luft_ges
# gesamte Energie:
E_ges = E_pot + E_konstante_geschwindigkeit + stopps * E_kin - stopps * E_rekuperation_kin - E_rekuperation_pot
# Beücksichtigung Gesamtwirkungsgrad:
E_ges = E_ges / n_ges
# Berücksichtigung Energiegehalt:
E_ges = E_ges / energie_gehalt
# Berücksichtigung Dieselpreis:
Energie_kosten = E_ges * preis_l
# Energiekosten für eine Fahrt:
print(Energie_kosten)
# Kosten in einer Woche:
Energie_kosten = Energie_kosten * Fahrten_eine_woche
# Kosten in einem Jahr: 
Energie_kosten_ein_Jahr = Energie_kosten * Wochen_ein_Jahr
# Gesamtkosten
while x <= dauer_beobachtung:
    if x == 1:
        Energie_kosten_komplett =  Anzahl_züge * investitionskosten + Energie_kosten_ein_Jahr + Kosten_Bau_Tankstelle
        Kosten_list.append(Energie_kosten_komplett)
    else:
        Energie_kosten_komplett += Energie_kosten_ein_Jahr
        Kosten_list.append(Energie_kosten_komplett)
    x += 1
print(Kosten_list)