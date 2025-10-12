"""
Selection Sort Implementierung
=============================

Dieser Code demonstriert den Selection-Sort-Algorithmus.

FUNKTIONSWEISE:
- Der Algorithmus sucht in jedem Durchlauf das kleinste (oder größte) Element im unsortierten Teil der Liste.
- Dieses Element wird an die aktuelle Position (i) gesetzt.
- Nach jedem Durchlauf ist das nächste kleinste Element an der richtigen Stelle.

SCHLEIFENVARIABLEN:
- i (äußere Schleife): Steuert die aktuelle Position, an die das nächste Minimum gesetzt wird.
- j (innere Schleife): Durchsucht den unsortierten Bereich nach dem kleinsten Element.

VORTEILE:
- Einfach zu verstehen und zu implementieren.
- Benötigt keine zusätzlichen Datenstrukturen.

NACHTEILE:
- Relativ langsam bei großen Listen (O(n²) Laufzeit).
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

# Länge des "Arrays" bestimmen
laenge = len(input_list)

# Äußere Schleife: Durchläufe für jeden zu platzierenden Wert (-1, da letzter Wert automatisch sortiert ist)
for i in range(laenge - 1):
    # Index des aktuell kleinsten Elements annehmen
    min_index = i
    # Innere Schleife: Vergleiche benachbarte Elemente (Ende verkürzt sich mit jedem Durchlauf um bereits sortierte Elemente)
    for j in range(i + 1, laenge):
        # Prüfen, ob das aktuelle Element kleiner als das bisher kleinste gefundene ist
        if input_list[j] < input_list[min_index]:
            # Index des neuen kleinsten Elements merken
            min_index = j
    # Wenn ein neues Minimum gefunden wurde, tauschen wir es mit dem aktuellen Element an Position i
    if min_index != i:
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    # Bisher sortierten Teil der Liste und den unsortierten Teil ausgeben
    print(f"Durchlauf {i + 1}: {input_list[:i + 1]} | {input_list[i + 1:]}")

# Sortierte Liste ausgeben
print("Sortierte Liste:", input_list)