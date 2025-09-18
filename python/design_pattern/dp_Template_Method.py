"""
Problemstellung:
Ein grundsätzlicher Ablauf (Algorithmus) ist fest vorgegeben und für einen konkreten Ablauf können sich einzelne
Schritte unterscheiden.
Die Struktur des Ablaufs darf jedoch nicht verändert werden.

Beispiele:
Ein Beispiel wären Sortieralgrithmen, die eine feste Struktur haben, aber unterschiedliche
Implementierungen für den Vergleich von Elementen nutzen (z.B. aufsteigend, absteigend, nach bestimmten Kriterien).
Ein anderes Beispiel wäre das versenden von Daten über eine Netzwerkverbindung, bei dem die
Verbindungsart (z.B. TCP, UDP) variiert, der Ablauf (Verbindung aufbauen, Daten senden, Verbindung schließen)
jedoch immer gleich bleibt.
Oder aber das Zeichnen von Komponenten in einer GUI, bei dem der Ablauf des Zeichnens
(vorbereiten, zeichnen, abschließen) gleich bleibt, die konkreten Zeichenoperationen (z.B. Kreis, Rechteck, Linie)
aber unterschiedlich sind.

Kurze Erklärung:
Das Template Method Pattern definiert das Grundgerüst eines Algorithmus in einer Methode (der Template Method).
Die einzelnen Schritte des Algorithmus werden in separaten Methoden definiert, die von Unterklassen
überschrieben werden können, um das Verhalten zu spezifizieren.
Mindestens eine Methode (z.B. paint) muss abstrakt sein, damit die Unterklassen gezwungen werden, diese zu implementieren.
In Python wird dies meist durch das Werfen einer Exception (NotImplementedError) gelöst, da Python keine echten abstrakten Methoden kennt,
außer man verwendet das abc-Modul. Im aktuellen Code wird dies durch raise NotImplementedError erreicht.

Nachteile:
- Erhöhter Aufwand für die Implementierung, da die Struktur des Algorithmus in der Template Method festgelegt ist.
- Eingeschränkte Flexibilität, da die Reihenfolge der Schritte nicht verändert werden kann.
"""

# Basisklasse mit Template Method
class GuiComponent:
    """
    Template Method Pattern:
    Diese Klasse definiert den festen Ablauf für das Zeichnen einer GUI-Komponente.
    Einzelne Schritte können von Unterklassen überschrieben werden.
    """

    def draw(self):
        # Template Method: Definiert den festen Ablauf
        self.prepare()   # Schritt 1: Vorbereitung
        self.paint()     # Schritt 2: Zeichnen (wird von Unterklassen überschrieben)
        self.finish()    # Schritt 3: Abschluss

    def prepare(self):
        # Standard-Vorbereitungsschritt
        print("GuiComponent: Vorbereitung abgeschlossen.")

    def paint(self):
        # Platzhalter für die konkrete Zeichenoperation
        # Soll von Unterklassen überschrieben werden
        raise NotImplementedError("paint() muss von der Unterklasse implementiert werden.")

    def finish(self):
        # Standard-Abschluss-Schritt
        print("GuiComponent: Zeichnen abgeschlossen.")

# Unterklasse für einen Kreis
class Circle(GuiComponent):
    def paint(self):
        # Überschreibt den paint-Schritt für einen Kreis
        print("Circle: Kreis wird gezeichnet.")

# Unterklasse für ein Rechteck
class Rectangle(GuiComponent):
    def paint(self):
        # Überschreibt den paint-Schritt für ein Rechteck
        print("Rectangle: Rechteck wird gezeichnet.")

# Beispiel-Nutzung
circle = Circle()         # Erstellt eine Kreis-Komponente
rectangle = Rectangle()   # Erstellt eine Rechteck-Komponente

circle.draw()             # Führt den festen Ablauf für Kreis aus
rectangle.draw()          # Führt den festen Ablauf für Rechteck aus