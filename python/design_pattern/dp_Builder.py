"""
Problemstellung:
Objekte, die zu erzeugen sind, sind komplex und haben viele optionale Parameter bzw. Bestandteile.
Dadurch sind mehrere Einzelschritte für die Erzeugung nötig, außerdem sind nicht alle Kombinationen zulässig.

Beispiele:
Ein Möbelgeschäft bietet seinen Kunden die Möglichkeit, Möbelstücke individuell zu konfigurieren.
Es gibt viele Wahlmöglichkeiten, einige Teile sind obligatorisch, andere optional.
Aber einige Teile schließen sich auch aus.

Kurze Erklärung:
Das Builder-Pattern kapselt die schrittweise Konstruktion eines komplexen Objekts.
Der Builder stellt Methoden bereit, um einzelne Eigenschaften zu setzen.
Am Ende wird das fertige Objekt mit einer Methode (z.B. build() oder konstruiere()) erzeugt.
Dadurch bleibt die Erstellung übersichtlich und nur gültige Kombinationen sind möglich.
Der Client ruft die einzelnen Methoden des Builders auf und erhält am Ende das fertige Objekt.

Nachteile:
- Erhöhter Aufwand durch zusätzliche Klassen.
- Kann zu vielen kleinen Klassen führen, wenn viele verschiedene Objekttypen gebaut werden müssen.
- Der Builder muss sorgfältig entworfen werden, um alle möglichen Kombinationen abzudecken.
"""

# Die Produktklasse: Schrank
class Schrank:
    def __init__(self, oberflaeche, metallschiene, einlegeboden, kleiderstange):
        # Initialisiert die Attribute des Schranks
        self.oberflaeche = oberflaeche
        self.metallschiene = metallschiene
        self.einlegeboden = einlegeboden
        self.kleiderstange = kleiderstange

    def __str__(self):
        # Gibt eine lesbare Beschreibung des Schranks zurück
        return (f"Schrank mit Oberfläche: {self.oberflaeche}, "
                f"Metallschiene: {'ja' if self.metallschiene else 'nein'}, "
                f"Einlegeboden: {'ja' if self.einlegeboden else 'nein'}, "
                f"Kleiderstange: {'ja' if self.kleiderstange else 'nein'}")

# Der Builder für den Schrank
class SchrankBuilder:
    def __init__(self):
        # Setzt Standardwerte für alle Attribute
        self.oberflaeche = "unbehandelt"
        self.metallschiene = False
        self.einlegeboden = False
        self.kleiderstange = False

    def mitOberflaeche(self, oberflaeche):
        # Setzt die Oberfläche des Schranks
        self.oberflaeche = oberflaeche
        return self  # Ermöglicht Method-Chaining

    def mitMetallschiene(self):
        # Fügt eine Metallschiene hinzu
        self.metallschiene = True
        return self

    def mitEinlegeboden(self):
        # Fügt einen Einlegeboden hinzu
        self.einlegeboden = True
        return self

    def mitKleiderstange(self):
        # Fügt eine Kleiderstange hinzu
        self.kleiderstange = True
        return self

    def konstruiere(self):
        # Erzeugt das fertige Schrank-Objekt mit den gewählten Optionen
        return Schrank(
            self.oberflaeche,
            self.metallschiene,
            self.einlegeboden,
            self.kleiderstange
        )

# Beispiel-Nutzung des Builders
builder = SchrankBuilder()                  # Erstellt einen neuen Builder
# Die runden Klammern ermöglichen die mehrzeilige Kettenbildung.
schrank = (builder
           .mitOberflaeche("lackiert")      # Setzt die Oberfläche auf "lackiert"
           .mitMetallschiene()              # Fügt eine Metallschiene hinzu
           .mitEinlegeboden()               # Fügt einen Einlegeboden hinzu
           .konstruiere())                  # Baut den fertigen Schrank

print(schrank)                              # Gibt die Beschreibung des Schranks aus