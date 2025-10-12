"""
Bubble Sort Implementierung
===========================

Dieser Code demonstriert den Bubble-Sort-Algorithmus in zwei Varianten.

FUNKTIONSWEISE:
- Der Algorithmus vergleicht benachbarte Elemente paarweise
- Größere Elemente "blubbern" nach rechts (wie Blasen im Wasser)
- Nach jedem Durchlauf steht das größte verbleibende Element am Ende

SCHLEIFENVARIABLEN:
- i (äußere Schleife): Zählt die Durchläufe (0 bis n-1)
  -> Steuert, wie oft die Liste komplett durchlaufen wird
  -> Bei 6 Elementen: 5 Durchläufe (nach 5 Durchläufen sind alle Elemente sortiert)
  -> Verkürzt die innere Schleife durch `len(input_list) - (1 + i)`:
    - Durchlauf 1 (i=0): 5 Vergleiche → größtes Element wandert ans Ende
    - Durchlauf 2 (i=1): 4 Vergleiche → zweitgrößtes Element an vorletzte Position
    - Durchlauf 3 (i=2): 3 Vergleiche → drittgrößtes Element an drittletzte Position
    - usw.

- j (innere Schleife): Index für den paarweisen Vergleich (0 bis n-1-i)
  -> Vergleicht input_list[j] mit input_list[j+1]
  -> Bereich wird mit jedem Durchlauf kleiner (bereits sortierte Elemente überspringen)

ZWEI IMPLEMENTIERUNGEN:
1. Mit pop()/insert() - anschaulich, aber langsamer (Listenoperationen)
2. Mit "Drei-Wege-Tausch" - klassische Variante, effizienter (direkter Zugriff)
"""

# TODO: Zeitmessung mittels Zeitstempel implementieren (z.B. mit time.time() vor/nach Sortierung)

# Ausgangsliste mit Umsortieren Wortern definieren
#input_list = ["Banane", "Apfel", "Orange", "Mango", "Birne", "Kirsche"]

# Ausgangsliste mit Umsortieren Ganzzahlen definieren
input_list = [10, 2, 5, 4, 80, 43, 10, 2, 5, 4, 80, 43]

# Zusätzliche eindeutige Werte ergänzen
input_list += [17, 23, 1, 99, 7, 56]
input_list += [34, 65, 12, 88, 3, 77]

# Unsortierte Liste zur Kontrolle ausgeben
print("Unsortierte Liste:", input_list)

# Äußere Schleife: Durchläufe für jeden zu platzierenden Wert (-1, da letzter Wert automatisch sortiert ist)
for i in range (len(input_list) - 1):
    # Innere Schleife: Vergleiche benachbarte Elemente (Ende verkürzt sich mit jedem Durchlauf um bereits sortierte Elemente)
    for j in range(len(input_list) - (1 + i)):
        # Prüfen, ob das aktuelle Element größer als Nächstes ist (aufsteigende Sortierung)
        if input_list[j] > input_list[j + 1]:
            # Größeres Element aus Liste entfernen und temporär speichern
            temp = input_list.pop(j)
            # Entferntes Element an nächster Position einfügen (Tausch abgeschlossen)
            input_list.insert(j + 1, temp)

# Sortierte Liste ausgeben
print("Sortierte Liste:", input_list)


# Alternative Implementierung mit klassischem Variablen-Tausch (effizienter als pop/insert)
input_list = [10, 2, 5, 4, 80, 43]
print("Unsortierte Liste:", input_list)

# Äußere Schleife: Anzahl der Durchläufe
for i in range(len(input_list) - 1):
    # Innere Schleife: Paarweiser Vergleich benachbarter Elemente
    for j in range(len(input_list) - (1 + i)):
        # Wenn aktuelles Element größer als Nachfolger, dann tauschen
        if input_list[j] > input_list[j + 1]:
            # Nachfolger-Element in temporäre Variable speichern
            temp = input_list[j +1]
            # Aktuelles (größeres) Element nach rechts verschieben
            input_list[j + 1] = input_list[j]
            # Gespeichertes (kleineres) Element an aktuelle Position setzen
            input_list[j] = temp
# Sortiertes Ergebnis ausgeben
print("Sortierte Liste:", input_list)
