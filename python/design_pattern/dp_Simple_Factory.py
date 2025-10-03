"""
Problemstellung:
Der Client soll von den Details der Objekterzeugung entkoppelt werden. Außerdem soll er nicht entscheiden
müssen, welches konkrete Objekt benötigt wird.

Beispiele:
- Einlesen von Dateien in verschiedenen Formaten (PDF, CSV, JSON) basierend auf Dateierweiterung
- Logger-Erstellung je nach Konfiguration (FileLogger, ConsoleLogger, DatabaseLogger)
- Datenbank-Verbindungen für verschiedene Systeme (MySQL, PostgreSQL, SQLite)
- GUI-Elemente für verschiedene Betriebssysteme (WindowsButton, MacButton, LinuxButton)

Kurze Erklärung:
Das Simple Factory-Pattern stellt eine Schnittstelle zur Verfügung, um Objekte zu erzeugen, ohne die konkreten Klassen
der zu erzeugenden Objekte angeben zu müssen. Stattdessen wird die Entscheidung, welches Objekt erzeugt wird,
an eine Factory-Klasse oder -Methode delegiert. Dies ermöglicht eine lose Kopplung zwischen dem Client und den konkreten
Objektklassen.

Nachteile:
- Erhöhter Aufwand durch zusätzliche Klassen und Methoden.
"""

# Einfaches Factory Pattern Beispiel mit Mahlzeiten.
# In C# würde man hier ein Interface verwenden: public interface IMahlzeit

# Basis-Klasse für alle Mahlzeiten (Interface-Ersatz in Python)
# In C# wäre das: public class Mahlzeit oder besser public interface IMahlzeit
class Mahlzeit:
    # Konstruktor der Basis-Klasse
    def __init__(self, name):
        # Name der Mahlzeit als Instanzvariable speichern
        self.name = name
    
    # Basis-Methode für Zubereitung (kann überschrieben werden)
    def zubereiten(self):
        # Standard-Methode für Zubereitung - gibt einfachen Text zurück
        return f"{self.name} wird zubereitet"

# Konkrete Mahlzeit-Klassen - erben von der Basis-Klasse Mahlzeit
# In C# wäre das: public class Fruehstueck : IMahlzeit

# Erste konkrete Implementierung: Frühstück
class Fruehstueck(Mahlzeit):
    # Konstruktor der Frühstück-Klasse
    def __init__(self):
        # Ruft Basis-Konstruktor auf und übergibt den Namen
        # In C# wäre das: base("Frühstück")
        super().__init__("Frühstück")
    
    # Überschreibt die zubereiten-Methode der Basis-Klasse
    def zubereiten(self):
        # Spezifische Zubereitung für Frühstück - detaillierte Beschreibung
        return "Müsli mit Milch und Obst zubereiten"

# Zweite konkrete Implementierung: Mittagessen
class Mittagessen(Mahlzeit):
    # Konstruktor der Mittagessen-Klasse
    def __init__(self):
        # Ruft Basis-Konstruktor auf und übergibt den Namen
        super().__init__("Mittagessen")
    
    # Überschreibt die zubereiten-Methode der Basis-Klasse
    def zubereiten(self):
        # Spezifische Zubereitung für Mittagessen - warme Hauptmahlzeit
        return "Schnitzel mit Pommes braten"

# Dritte konkrete Implementierung: Abendessen
class Abendessen(Mahlzeit):
    # Konstruktor der Abendessen-Klasse
    def __init__(self):
        # Ruft Basis-Konstruktor auf und übergibt den Namen
        super().__init__("Abendessen")
    
    # Überschreibt die zubereiten-Methode der Basis-Klasse
    def zubereiten(self):
        # Spezifische Zubereitung für Abendessen - meist kalte/leichte Kost
        return "Brot mit Aufschnitt richten"

# Vierte konkrete Implementierung: Keine Mahlzeit (Null-Object Pattern)
class KeineMahlzeit(Mahlzeit):
    # Konstruktor für "Keine Mahlzeit"
    def __init__(self):
        # Ruft Basis-Konstruktor auf mit entsprechendem Namen
        super().__init__("Keine Mahlzeit")
    
    # Überschreibt die zubereiten-Methode der Basis-Klasse
    def zubereiten(self):
        # Keine Zubereitung nötig - leere Aktion
        return "Nichts zubereiten"

# Die Factory-Klasse - Herzstück des Factory Patterns
# Erstellt die richtigen Mahlzeit-Objekte basierend auf einem String-Parameter
# In C# wäre das: public class MahlzeitFactory
class MahlzeitFactory:
    
    # Statische Methode (gehört zur Klasse, nicht zu einer Instanz)
    # In C# wäre das: public static IMahlzeit ErstelleMahlzeit(string typ)
    @staticmethod
    def erstelle_mahlzeit(typ):
        # Factory-Methode: erstellt Objekt basierend auf Typ-String
        # Parameter typ: String der den gewünschten Mahlzeit-Typ angibt
        # Rückgabe: Instanz einer konkreten Mahlzeit-Klasse
        
        # If-Elif-Else Struktur zur Objekterzeugung (in C# wäre das ein switch)
        if typ == "morgens":
            # String "morgens" → Frühstück-Objekt erstellen und zurückgeben
            return Fruehstueck()
        elif typ == "mittags":
            # String "mittags" → Mittagessen-Objekt erstellen und zurückgeben
            return Mittagessen()
        elif typ == "abends":
            # String "abends" → Abendessen-Objekt erstellen und zurückgeben
            return Abendessen()
        else:
            # Fallback für alle unbekannten Strings → Keine Mahlzeit
            # Verhindert Crashes bei falschen Eingaben
            return KeineMahlzeit()

# Client-Code - nutzt die Factory ohne die konkreten Klassen zu kennen
# Demonstriert die Entkopplung zwischen Client und konkreten Implementierungen
def main():
    # Ausgabe der Überschrift
    print("=== Einfaches Factory Pattern Beispiel ===\n")
    
    # Liste der gewünschten Mahlzeiten (verschiedene Tageszeiten)
    # Enthält auch einen ungültigen Wert ("nachts") zum Testen
    mahlzeit_wuensche = ["morgens", "mittags", "abends", "nachts"]
    
    # For-Schleife: iteriert über alle Mahlzeit-Wünsche
    for wunsch in mahlzeit_wuensche:
        # Ausgabe des aktuellen Wunsches
        print(f"Wunsch: {wunsch}")
        
        # Factory nutzen um Mahlzeit-Objekt zu erstellen
        # WICHTIG: Client muss nicht wissen welche konkreten Klassen existieren
        # Er kennt nur die Factory und den String-Parameter
        mahlzeit = MahlzeitFactory.erstelle_mahlzeit(wunsch)
        
        # Methode der erstellten Mahlzeit aufrufen
        # Polymorphismus: jede Mahlzeit-Klasse hat ihre eigene zubereiten()-Implementierung
        zubereitung = mahlzeit.zubereiten()
        
        # Ergebnis ausgeben
        print(f"Ergebnis: {zubereitung}")
        
        # Leere Zeile für bessere Lesbarkeit
        print()

# Programm-Einstiegspunkt - wird nur ausgeführt wenn Datei direkt gestartet wird
# In C# wäre das: public static void Main(string[] args)
if __name__ == "__main__":
    # Hauptfunktion aufrufen um das Beispiel zu starten
    main()