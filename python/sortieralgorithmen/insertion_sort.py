"""
Insertion Sort Implementierung
=============================

Dieser Code demonstriert den Insertion-Sort-Algorithmus.

FUNKTIONSWEISE:
- Der Algorithmus baut die sortierte Liste schrittweise auf.
- Jedes Element wird an die richtige Stelle im bereits sortierten Bereich eingefügt.
- Dabei werden größere Elemente nach rechts verschoben, bis die passende Position gefunden ist.

SCHLEIFENVARIABLEN:
- i (äußere Schleife): Steuert das aktuelle Element, das einsortiert werden soll.
- j (innere Schleife): Vergleicht und verschiebt Elemente im sortierten Bereich nach rechts.

VORTEILE:
- Sehr effizient bei fast sortierten Listen.
- Einfach zu implementieren.

NACHTEILE:
- Relativ langsam bei großen, unsortierten Listen (O(n²) Laufzeit).
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

# Äußere Schleife: Durchläufe für jedes Element ab dem zweiten (Index 1)
for i in range(1, len(input_list)):
    # Aktuelles Element, das einsortiert werden soll
    key = input_list[i]
    # Innere Schleife: Vergleiche mit den vorherigen Elementen im sortierten Bereich
    j = i - 1
    # Verschiebe Elemente nach rechts, bis die richtige Position für 'key' gefunden ist
    while j >= 0 and input_list[j] > key:
        input_list[j + 1] = input_list[j]
        j -= 1
    # Füge 'key' an der richtigen Position ein
    input_list[j + 1] = key
    # Bisher sortierten Teil der Liste und den unsortierten Teil ausgeben
    print(f"Durchlauf {i}: {input_list[:i + 1]} | {input_list[i + 1:]}")