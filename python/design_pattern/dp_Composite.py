"""
Problemstellung:
Doe Objekte sind in einer Baumstruktur organisiert, wobei Blätter und Knoten gibt. Die Knoten sind die Verzweigungen
des Baumes und die Blätter die jeweiligen Endpunkte. Der Client soll sowohl mit Blättern als auch mit Knoten
arbeiten können, ohne den Unterschied zu kennen.

Beispiele:
Grafische Benutzeroberflächen, bei denen Container (Knoten) andere Container oder Widgets (Blätter) enthalten können.
Dateisysteme, bei denen Verzeichnisse (Knoten) andere Verzeichnisse oder Dateien (Blätter) enthalten können.
Verzeichnisstrukturen, bei denen Ordner (Knoten) andere Ordner oder Dateien (Blätter) enthalten können.

Kurze Erklärung:
Das Composite-Pattern ermöglicht es, Objekte in Baumstrukturen zu organisieren und sowohl einzelne Objekte
(Blätter) als auch Gruppen von Objekten (Knoten) einheitlich zu behandeln. Sowohl Blätter als auch Knoten
implementieren ein gemeinsames Interface, das es dem Client ermöglicht, mit beiden auf die gleiche Weise zu
interagieren. Dadurch wird die Komplexität reduziert und die Wartbarkeit verbessert.

Nachteile:
- Spezielle Eigenschaften der Baumelelemente sind nur erschwert zugänglich.
- Baumelemente bieten einzelne geerbte Methoden möglicherweise nicht an.
"""

# Einfaches Composite Pattern Beispiel mit Dateisystem
# In C# würde man hier ein Interface verwenden: public interface IDateiElement

# Basis-Klasse für alle Dateisystem-Elemente (Interface-Ersatz in Python)
# In C# wäre das: public interface IDateiElement oder public abstract class DateiElement
class DateiElement:
    # Konstruktor der Basis-Klasse
    def __init__(self, name):
        # Name des Dateisystem-Elements speichern
        self.name = name
    
    # Basis-Methode um Größe zu berechnen (muss überschrieben werden)
    def get_groesse(self):
        # Standard-Implementierung - wird von Kindklassen überschrieben
        return 0
    
    # Basis-Methode um Element anzuzeigen (muss überschrieben werden)
    def anzeigen(self, einrueckung=0):
        # Standard-Implementierung mit Einrückung für Baumstruktur
        print("  " * einrueckung + self.name)

# BLATT-Klasse: Datei (hat keine Kinder)
# Implementiert das Blatt im Composite Pattern
class Datei(DateiElement):
    # Konstruktor für Datei-Objekte
    def __init__(self, name, groesse):
        # Ruft Basis-Konstruktor auf
        super().__init__(name)
        # Dateigröße als Instanz-Variable speichern
        self.groesse = groesse
    
    # Überschreibt get_groesse() - gibt die tatsächliche Dateigröße zurück
    def get_groesse(self):
        # Blatt: gibt einfach seine eigene Größe zurück
        return self.groesse
    
    # Überschreibt anzeigen() - zeigt Datei mit Größe an
    def anzeigen(self, einrueckung=0):
        # Datei mit Größe und Einrückung anzeigen
        print("  " * einrueckung + f"📄 {self.name} ({self.groesse} KB)")

# KNOTEN-Klasse: Ordner (kann Kinder haben - andere Ordner oder Dateien)
# Implementiert den Composite im Composite Pattern
class Ordner(DateiElement):
    # Konstruktor für Ordner-Objekte
    def __init__(self, name):
        # Ruft Basis-Konstruktor auf
        super().__init__(name)
        # Liste für Kinder-Elemente (kann Dateien und andere Ordner enthalten)
        self.kinder = []
    
    # Methode um Kind-Element hinzuzufügen (Datei oder Ordner)
    def hinzufuegen(self, element):
        # Element zur Kinder-Liste hinzufügen
        # Parameter: element kann sowohl Datei als auch Ordner sein (Polymorphismus)
        self.kinder.append(element)
    
    # Methode um Kind-Element zu entfernen
    def entfernen(self, element):
        # Element aus Kinder-Liste entfernen falls vorhanden
        if element in self.kinder:
            # Element aus Liste entfernen
            self.kinder.remove(element)
    
    # Überschreibt get_groesse() - berechnet Gesamtgröße aller Kinder
    def get_groesse(self):
        # Knoten: summiert die Größe aller Kinder auf
        gesamt_groesse = 0
        
        # Durch alle Kinder iterieren
        for kind in self.kinder:
            # Größe des Kindes zur Gesamtgröße addieren
            # WICHTIG: Polymorphismus - egal ob Datei oder Ordner, beide haben get_groesse()
            gesamt_groesse += kind.get_groesse()
        
        # Gesamtgröße zurückgeben
        return gesamt_groesse
    
    # Überschreibt anzeigen() - zeigt Ordner und alle Kinder an
    def anzeigen(self, einrueckung=0):
        # Ordner-Namen mit Icon und Einrückung anzeigen
        print("  " * einrueckung + f"📁 {self.name}/")
        
        # Alle Kinder-Elemente anzeigen
        for kind in self.kinder:
            # Rekursiver Aufruf mit erhöhter Einrückung
            # WICHTIG: Polymorphismus - egal ob Datei oder Ordner, beide haben anzeigen()
            kind.anzeigen(einrueckung + 1)

# Client-Code - arbeitet einheitlich mit Dateien und Ordnern
# Demonstriert dass Client keinen Unterschied zwischen Blatt und Knoten kennen muss
def main():
    # Überschrift ausgeben
    print("=== Composite Pattern - Dateisystem Beispiel ===\n")
    
    # Einzelne Dateien erstellen (BLÄTTER)
    datei1 = Datei("dokument.txt", 50)      # Datei mit 50 KB
    datei2 = Datei("bild.jpg", 200)         # Datei mit 200 KB
    datei3 = Datei("video.mp4", 1500)       # Datei mit 1500 KB
    datei4 = Datei("musik.mp3", 300)        # Datei mit 300 KB
    
    # Ordner erstellen (KNOTEN)
    hauptordner = Ordner("Meine Dokumente")     # Haupt-Ordner
    bilder_ordner = Ordner("Bilder")            # Unter-Ordner für Bilder
    media_ordner = Ordner("Media")              # Unter-Ordner für Media
    
    # Baumstruktur aufbauen durch Hinzufügen von Elementen
    print("Dateisystem-Struktur wird aufgebaut...\n")
    
    # Dateien zu Ordnern hinzufügen
    bilder_ordner.hinzufuegen(datei2)          # bild.jpg → Bilder/
    media_ordner.hinzufuegen(datei3)           # video.mp4 → Media/
    media_ordner.hinzufuegen(datei4)           # musik.mp3 → Media/
    
    # Ordner zu Haupt-Ordner hinzufügen (Verschachtelung!)
    hauptordner.hinzufuegen(datei1)            # dokument.txt → Meine Dokumente/
    hauptordner.hinzufuegen(bilder_ordner)     # Bilder/ → Meine Dokumente/
    hauptordner.hinzufuegen(media_ordner)      # Media/ → Meine Dokumente/
    
    # Gesamte Struktur anzeigen
    print("Vollständige Dateisystem-Struktur:")
    hauptordner.anzeigen()  # Rekursive Anzeige der gesamten Baumstruktur
    
    print()  # Leere Zeile
    
    # Größen-Berechnungen demonstrieren
    print("=== Größen-Berechnungen ===")
    
    # WICHTIG: Client behandelt alle Elemente gleich (Polymorphismus)
    # Egal ob Datei (Blatt) oder Ordner (Knoten) - beide haben get_groesse()
    print(f"Größe von '{datei1.name}': {datei1.get_groesse()} KB")
    print(f"Größe von '{bilder_ordner.name}': {bilder_ordner.get_groesse()} KB")
    print(f"Größe von '{media_ordner.name}': {media_ordner.get_groesse()} KB")
    print(f"Größe von '{hauptordner.name}': {hauptordner.get_groesse()} KB")
    
    print()  # Leere Zeile
    
    # Einzelnes Element bearbeiten
    print("=== Element entfernen ===")
    print("Entferne video.mp4 aus Media-Ordner...")
    media_ordner.entfernen(datei3)  # Video-Datei entfernen
    
    # Struktur erneut anzeigen
    print("\nStruktur nach Entfernung:")
    hauptordner.anzeigen()
    
    # Größe nach Entfernung
    print(f"\nNeue Größe von '{hauptordner.name}': {hauptordner.get_groesse()} KB")
    
    print()  # Leere Zeile
    
    # Vorteile des Composite Patterns erläutern
    print("=== Vorteile des Composite Patterns ===")
    print("1. Client behandelt Dateien und Ordner gleich")
    print("2. Einfache Erweiterung um neue Element-Typen")
    print("3. Rekursive Operationen automatisch möglich")
    print("4. Baumstrukturen natürlich abgebildet")

# Hilfsfunktion um zu demonstrieren dass Client keinen Unterschied kennt
def verarbeite_element(element):
    # Diese Funktion arbeitet mit JEDEM DateiElement
    # Egal ob es eine Datei (Blatt) oder Ordner (Knoten) ist
    print(f"Verarbeite: {element.name} - Größe: {element.get_groesse()} KB")
    
    # Zeige Element an
    element.anzeigen()

# Programm-Einstiegspunkt
if __name__ == "__main__":
    # Hauptfunktion starten
    main()