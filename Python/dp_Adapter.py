"""
Problemstellung:
Die Schnittstelle eines Objekts entspricht nicht der Schnittstelle, die ein Client erwartet.
Änderungen an den beteiligten Klassen sind nicht möglich oder nicht erwünscht.

Beispiele:
Es soll eine andere Bibliothek verwendet werden, die zwar die selben Dienste anbietet, aber mit
anderen Klassen und Methoden.
Ein Client soll mit einem Altsystem kommunizieren, das demnächst durch ein neues System ersetzt wird.

Kurze Erklärung:
Ein Adapter passt die Schnittstelle eines Objekts an die Schnittstelle an, die ein Client erwartet.
Dadurch kann der Client mit dem Objekt interagieren, ohne dass Änderungen an den beteiligten Klassen
erforderlich sind.
"""

# Dummy-Klasse, deren Schnittstelle nicht zum Client passt
class OldService:
    def specific_request(self):
        # Dummy-Methode, die eine spezielle Aktion simuliert
        print("OldService: spezifische Anfrage ausgeführt.")

# Klassen-Adapter (Vererbung)
class ClassAdapter(OldService):
    """
    Klassen-Adapter:
    Nutzt Vererbung, um die Schnittstelle des Adaptees (OldService) an die erwartete Schnittstelle anzupassen.
    Vorteil: Direkter Zugriff auf Methoden des Adaptees.
    Nachteil: Funktioniert nur, wenn Mehrfachvererbung möglich und sinnvoll ist.
    """

    def request(self):
        # Übersetzt die erwartete Methode 'request' auf die Methode des Adaptees
        print("ClassAdapter: request wird auf specific_request gemappt.")
        self.specific_request()

# Objekt-Adapter (Komposition)
class ObjectAdapter:
    """
    Objekt-Adapter:
    Nutzt Komposition, um die Schnittstelle des Adaptees (OldService) an die erwartete Schnittstelle anzupassen.
    Vorteil: Flexibler, da keine Vererbung nötig ist. Kann mehrere Adaptees kombinieren.
    Nachteil: Kein direkter Zugriff auf protected/private Methoden des Adaptees.
    """

    def __init__(self, adaptee):
        # Speichert die Instanz des Adaptees
        # Die Bezeichnung 'adaptee' ist konventionell und beschreibt das Objekt,das angepasst wird.
        self.adaptee = adaptee 

    def request(self):
        # Übersetzt die erwartete Methode 'request' auf die Methode des Adaptees
        print("ObjectAdapter: request wird auf specific_request gemappt.")
        self.adaptee.specific_request()

# Beispiel-Nutzung
print("=== Klassen-Adapter ===")
class_adapter = ClassAdapter()
class_adapter.request()  # Client ruft die erwartete Methode auf

print("\n=== Objekt-Adapter ===")
old_service = OldService()
object_adapter = ObjectAdapter(old_service)
object_adapter.request()  # Client ruft die erwartete Methode auf
