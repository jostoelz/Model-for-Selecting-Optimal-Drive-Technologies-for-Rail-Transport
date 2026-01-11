# Variabeln
Gewicht = (22.88 + 100) * 1000 # in kg
Geschwindigkeit = 110 / 3.6 # in m/s
Gesamtwirkungsgrad = 0.35 
Höhenmeter = 300 # in m
Gravitationsbeschleunigung = 9.81 # in m/s²
Distanz = 60000 # in m
Rekuperationsgrad = 0.55
Rotierende_Massen = 10
Beschleunigung = 1 # in m/s²
Luftdichte = 1.23 # in kg/m³
Luftwiderstandsbeiwert = 0.85 
Rollwiderstand = 0.001 
Querschnittsfläche = 10  # in m²
Zeitintervall_Messung = 0.00001 # in s
Anzahl_Beschleunigungen = 16 # Anzahl Stopps + 1
Energiepreis_pro_kWh = 0.37 # in Euro
Kosten_Investition_Zug = 8000000 # in Euro
Kosten_Bau_Oberleitung = 10560000 # in Euro
Fahrten_pro_Woche = 172 
Beobachtungsdauer = 30 # in Jahren
Anzahl_Züge = 2
Kosten_Liste = []
Aktuelles_Jahr = 1 
Aktuelle_Zeit = 0 
Wochen_pro_Jahr = 52 
E_Luftwiderstand_Beschleunigung = 0 

# Berechnungen
# benötigte Energie für Überwindung Rollwiderstand während einer Fahrt
Normalkraft = Gewicht * Gravitationsbeschleunigung 
F_Rollwiderstand = Rollwiderstand * Normalkraft
E_Rollwiderstand = F_Rollwiderstand * Distanz / 3600000
# benötigte kinetische Energie bis zur beschleunigenden Geschwindigkeit:
E_Kin = Gewicht / 2 * Geschwindigkeit**2 / 3600000
# Aufschlag durch rotierende Massen:
E_Kin = E_Kin / 100 * Rotierende_Massen + E_Kin
# benötigte potentielle Energie für Überwindung Höhenmeter: 
E_Pot = Gewicht * Gravitationsbeschleunigung * Höhenmeter / 3600000
# benötigte Energie für Überwindung Luftwiderstand bei Beschleunigung und Abbremsung:
Beschleunigugnszeit = Geschwindigkeit / Beschleunigung 
while Aktuelle_Zeit < Beschleunigugnszeit:
    Geschwindigkeit = Beschleunigung * Aktuelle_Zeit
    F_Luftwiderstand_Zeitintervall = 0.5 * Luftdichte * Querschnittsfläche * Luftwiderstandsbeiwert * Geschwindigkeit**2 
    Distanz_Zeitintervall = Geschwindigkeit * Zeitintervall_Messung  
    E_Luftwiderstand_Zeitintervall = F_Luftwiderstand_Zeitintervall * Distanz_Zeitintervall / 3600000  
    E_Luftwiderstand_Beschleunigung += E_Luftwiderstand_Zeitintervall
    Aktuelle_Zeit += Zeitintervall_Messung 
E_Luftwiderstand_Beschleunigung_Abbremsung = E_Luftwiderstand_Beschleunigung * Anzahl_Beschleunigungen * 2
# benötigte Energie für Überwindung Luftwidersand bei konstanter Geschwindigkeit:
F_Luftwiderstand = 0.5 * Luftdichte * Querschnittsfläche * Luftwiderstandsbeiwert * Geschwindigkeit**2 
Durchschnitt_Distanz_Teilstrecken = Distanz / Anzahl_Beschleunigungen
Distanz_Zeitintervall = Durchschnitt_Distanz_Teilstrecken - 2 * 0.5 * Beschleunigung * Beschleunigugnszeit**2
E_Luftwiderstand_konstant = F_Luftwiderstand * Distanz_Zeitintervall / 3600000  
E_Luftwiderstand_konstant = E_Luftwiderstand_konstant * Anzahl_Beschleunigungen
E_Luftwiderstand_Ges = E_Luftwiderstand_konstant + E_Luftwiderstand_Beschleunigung_Abbremsung
# Rekuperation kinetische Energie: 
E_Rekuperation_Kin = E_Kin * Rekuperationsgrad
# Rekuperation potentielle Energie:
E_Rekuperation_Pot = E_Pot * Rekuperationsgrad
# gesamte benötigte Energie für eine Fahrt:
E_Ges = E_Pot + E_Rollwiderstand + E_Luftwiderstand_Ges + Anzahl_Beschleunigungen * E_Kin - Anzahl_Beschleunigungen * E_Rekuperation_Kin - E_Rekuperation_Pot
# Berücksichtigung Gesamtwirkungsgrad:
E_Ges = E_Ges / Gesamtwirkungsgrad
# Berücksichtigung Energiepreis:
Energiekosten = E_Ges * Energiepreis_pro_kWh
Energiekosten_pro_Fahrt_pro_Person = Energiekosten / 286
print(Energiekosten_pro_Fahrt_pro_Person)
# Energiekosten pro Woche:
Energiekosten_pro_Woche = Energiekosten * Fahrten_pro_Woche
# Energiekosten pro Jahr: 
Energiekosten_pro_Jahr = Energiekosten_pro_Woche * Wochen_pro_Jahr
# Investitions- und Energiekosten Kosten während Beobachtungsdauer
while Aktuelles_Jahr <= Beobachtungsdauer:
    if Aktuelles_Jahr == 1:
        Kosten_Beobachtungsdauer =  Anzahl_Züge * Kosten_Investition_Zug + Energiekosten_pro_Jahr + Kosten_Bau_Oberleitung
        Kosten_Liste.append(Kosten_Beobachtungsdauer)
    else:
        Kosten_Beobachtungsdauer += Energiekosten_pro_Jahr
        Kosten_Liste.append(Kosten_Beobachtungsdauer)
    Aktuelles_Jahr += 1
print(Kosten_Liste)