"""
Factory Method Pattern

Problemstellung:
Der Client soll Objekte erzeugen können, ohne die konkreten Klassen zu kennen. Anders als beim Simple Factory Pattern
soll die Erweiterung um neue Produkttypen möglich sein, ohne bestehenden Code ändern zu müssen (Open/Closed-Prinzip).
Die Entscheidung, welches Objekt erzeugt wird, soll durch Polymorphismus statt durch if/elif-Logik erfolgen.

Beispiele aus der Praxis:
- Plugin-Systeme, bei denen jedes Plugin seine eigene Factory mitbringt
- UI-Framework-Komponenten für verschiedene Plattformen (iOS, Android, Web)
- Dokumenten-Exporter für verschiedene Formate (jedes Format hat eigene Factory)
- Spiele-Engines, bei denen verschiedene Level-Typen ihre eigenen Factories haben

Kurze Erklärung:
Das Factory Method Pattern definiert eine abstrakte Factory-Basisklasse mit einer abstrakten Methode zur Objekterzeugung.
Jede konkrete Factory-Klasse implementiert diese Methode und erzeugt ein spezifisches Produkt. Der Client arbeitet nur
mit der Factory-Basisklasse und kennt die konkreten Factory-Implementierungen nicht. Neue Produkttypen werden durch
neue Factory-Klassen hinzugefügt, ohne bestehenden Code zu ändern.

Vorteile:
- Befolgt Open/Closed-Prinzip (offen für Erweiterung, geschlossen für Änderung)
- Keine if/elif-Kaskaden bei vielen Produkttypen
- Jede Factory kann eigene komplexe Erzeugungslogik haben
- Sehr gut erweiterbar durch neue Factory-Klassen
- Lose Kopplung zwischen Client und Produkten

Nachteile:
- Mehr Klassen als beim Simple Factory Pattern (eine Factory pro Produkt)
- Etwas komplexer zu verstehen und aufzusetzen
- Overhead bei wenigen, stabilen Produkttypen

Unterschied zu Simple Factory Pattern:
- Simple Factory: EINE zentrale Factory-Klasse mit statischer Methode und if/elif-Logik
- Factory Method: MEHRERE Factory-Klassen (eine pro Produkt) mit Vererbungshierarchie und Polymorphismus
"""


from abc import ABC, abstractmethod

# Produkt-Basisklasse
class Meal(ABC):
    @abstractmethod # Abstrakte Methode, die von konkreten Factories überschrieben wird
    def serve(self):
        raise NotImplementedError("serve() muss von Unterklassen implementiert werden.")

# Konkrete Produkte
class Breakfast(Meal):
    def serve(self):
        print("Breakfast: Serving breakfast.")

class Lunch(Meal):
    def serve(self):
        print("Lunch: Serving lunch.")

class Dinner(Meal):
    def serve(self):
        print("Dinner: Serving dinner.")

# Factory-Basisklasse
class MealFactory(ABC):
    @abstractmethod # Abstrakte Methode, die von konkreten Factories überschrieben wird
    def create_meal(self):
        # Erzeugt manuell eine Exception, wenn nicht überschrieben
        raise NotImplementedError("create_meal() muss von Unterklassen implementiert werden.")

# Konkrete Factory-Klassen
class BreakfastFactory(MealFactory):
    def create_meal(self):
        # Erzeugt ein Frühstück
        return Breakfast()

class LunchFactory(MealFactory):
    def create_meal(self):
        # Erzeugt ein Mittagessen
        return Lunch()

class DinnerFactory(MealFactory):
    def create_meal(self):
        # Erzeugt ein Abendessen
        return Dinner()


# Client-Funktion arbeitet nur mit der Basisklasse
# Nimmt als Übergabapüarameter ein Objekt der Factorykindklassen vom Typ MealFactory (abstrakte Klasse)
def prepare_meal(factory: MealFactory):
    """Client kennt nur MealFactory-Interface, nicht die konkreten Factories"""
    meal = factory.create_meal()
    meal.serve()


# Beispiel-Nutzung
if __name__ == "__main__":
    print("=== Factory Method Pattern Beispiel ===\n")

    # Factory-Auswahl erfolgt außerhalb des Clients (z.B. durch Konfiguration) und erzeugt dann die entsprechende Factory
    factories = {
        "morgens": BreakfastFactory(),
        "mittags": LunchFactory(),
        "abends": DinnerFactory()
    }

    # Simuliere verschiedene Zeitpunkte
    zeitpunkte = ["morgens", "mittags", "abends"]

    for zeitpunkt in zeitpunkte:
        print(f"Zeitpunkt: {zeitpunkt}")
        chosen_factory = factories[zeitpunkt]
        prepare_meal(chosen_factory)  # Client kennt nur MealFactory
        print()
