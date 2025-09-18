"""
Problemstellung:
Ein Shopsystem ermöglicht es Kunden, Bestellungen aufzugeben.

Die Verarbeitung der Bestellung besteht aus vielen Einzelschritten.

Es muss mit unterschiedlichen Teilsystemen in einer bestimmten Reihenfolge kommuniziert werden.

Beispiele:
1. Rechnungsstelle: Auf offene Rechnungen prüfen
2. Lagerhaltung: Verfügbarkeit der Artikel prüfen
3. Lieferdienst: Versand der Artikel organisieren
4. Lagerhaltung: Lagerbestand aktualisieren
5. Rechnungsstelle: Bezahlvorgang abwickeln
6. E-Mail-Service: Bestätigungs-E-Mail an den Kunden senden

Kurze Erklärung:
Eine Facade bietet eine vereinfachte Schnittstelle zu einem komplexen System.
Die Facade kapselt die Komplexität des Systems und stellt nur die notwendigen Methoden für den
Client bereit. Sprich sie wird zwischen Client und komplexem System geschaltet.

Nachteile:
Die Facade kann zu einer "God Class" werden, wenn sie zu viele Verantwortlichkeiten übernimmt.
Dies kann die Wartbarkeit erschweren.
"""

# Dummy-Subsysteme, die jeweils eine Aufgabe übernehmen
class BillingSystem:
    def check_open_invoices(self):
        # Dummy-Methode für Rechnungsprüfung
        print("BillingSystem: Offene Rechnungen geprüft.")

class InventorySystem:
    def check_availability(self):
        # Dummy-Methode für Verfügbarkeitsprüfung
        print("InventorySystem: Artikelverfügbarkeit geprüft.")
    def update_stock(self):
        # Dummy-Methode für Lagerbestandsaktualisierung
        print("InventorySystem: Lagerbestand aktualisiert.")

class ShippingSystem:
    def organize_shipping(self):
        # Dummy-Methode für Versandorganisation
        print("ShippingSystem: Versand organisiert.")

class EmailService:
    def send_confirmation(self):
        # Dummy-Methode für Bestätigungs-E-Mail
        print("EmailService: Bestätigungs-E-Mail gesendet.")

# Die Facade kapselt die Komplexität und bietet eine einfache Schnittstelle
class OrderFacade:
    """
    Facade:
    Diese Klasse kapselt die komplexen Abläufe der Bestellung und bietet dem Client eine einfache Methode.
    Der Client muss sich nicht um die Reihenfolge und Details der einzelnen Teilsysteme kümmern.
    """

    def __init__(self):
        # Initialisiert alle benötigten Subsysteme
        self.billing = BillingSystem()
        self.inventory = InventorySystem()
        self.shipping = ShippingSystem()
        self.email = EmailService()

    def place_order(self):
        # Fassade-Methode, die alle Einzelschritte in richtiger Reihenfolge ausführt
        print("OrderFacade: Starte Bestellprozess.")
        self.billing.check_open_invoices()    # Schritt 1: Rechnungsprüfung
        self.inventory.check_availability()   # Schritt 2: Verfügbarkeit prüfen
        self.shipping.organize_shipping()     # Schritt 3: Versand organisieren
        self.inventory.update_stock()         # Schritt 4: Lagerbestand aktualisieren
        # Schritt 5: Bezahlvorgang abwickeln (Dummy, hier als Rechnungsprüfung nochmal)
        self.billing.check_open_invoices()
        self.email.send_confirmation()        # Schritt 6: Bestätigungs-E-Mail senden
        print("OrderFacade: Bestellprozess abgeschlossen.")

# Beispiel-Nutzung der Facade
facade = OrderFacade()       # Erzeugt die Facade und initialisiert die Subsysteme
facade.place_order()         # Client ruft nur eine Methode auf, die alles erledigt