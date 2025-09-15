"""
Problemstellung:
Wenn ein Objekt seinen Zustand ändert, sollen alle abhängigen Objekte automatisch benachrichtigt und
aktualisiert werden.

Beispiele:
Ein Temperatursensor liefert regelmäßig die aktuelle Temperatur. Je nach Temperatur soll eine Heizung bzw.
Kühlung ein- oder ausgeschaltet werden. Hierbei sind der Sensor und die Geräte voneinander unabhängig.
Ein weiteres Beispiel ist ein Nachrichtensystem, bei dem mehrere Benutzer (Clients)
über neue Nachrichten benachrichtigt werden sollen.


Kurze Erklärung:
Das Observer-Pattern definiert eine Eins-zu-viele-Abhängigkeit zwischen Objekten, so dass
wenn ein Objekt seinen Zustand ändert, alle abhängigen Objekte automatisch benachrichtigt werden.
Dies wird erreicht, indem das beobachtete Objekt (Subject) eine Liste von Beobachtern (Observers)
führt, die über Änderungen informiert werden.

Die Beobachter (Observers) implementieren ein gemeinsames Interface, das es ihnen ermöglicht,
Benachrichtigungen vom Subject zu empfangen. Wenn sich der Zustand des Subjects ändert, ruft
es eine Methode auf, die alle registrierten Beobachter informiert.

Nachteile:
- Erhöhter Aufwand für die Implementierung, da das Subject die Beobachter verwalten muss.
- Potenzielle Leistungseinbußen, wenn viele Beobachter registriert sind und häufige Änderungen
  am Subject stattfinden.
"""

# Beispiel OHNE Observer Pattern (Polling)
class SimpleTemperatureSensor:
    def __init__(self):
        # Initialisiert die Temperatur
        self.temperature = 20

    def set_temperature(self, value):
        # Setzt die Temperatur auf einen neuen Wert
        self.temperature = value

    def get_temperature(self):
        # Gibt die aktuelle Temperatur zurück
        return self.temperature

class SimpleHeater:
    def check_and_heat(self, sensor):
        # Prüft die Temperatur und schaltet ggf. die Heizung ein
        if sensor.get_temperature() < 18:
            print("SimpleHeater: Heizung eingeschaltet.")
        else:
            print("SimpleHeater: Heizung ausgeschaltet.")

class SimpleCooler:
    def check_and_cool(self, sensor):
        # Prüft die Temperatur und schaltet ggf. die Kühlung ein
        if sensor.get_temperature() > 25:
            print("SimpleCooler: Kühlung eingeschaltet.")
        else:
            print("SimpleCooler: Kühlung ausgeschaltet.")

# Beispiel-Nutzung ohne Observer
print("=== Ohne Observer ===")
sensor = SimpleTemperatureSensor()   # Erstellt einen Temperatursensor
heater = SimpleHeater()              # Erstellt eine Heizung
cooler = SimpleCooler()              # Erstellt eine Kühlung

sensor.set_temperature(16)           # Setzt die Temperatur
heater.check_and_heat(sensor)        # Heizung fragt aktiv nach der Temperatur
cooler.check_and_cool(sensor)        # Kühlung fragt aktiv nach der Temperatur

sensor.set_temperature(28)           # Setzt eine neue Temperatur
heater.check_and_heat(sensor)        # Heizung fragt erneut nach der Temperatur
cooler.check_and_cool(sensor)        # Kühlung fragt erneut nach der Temperatur

print("\n=== Mit Observer ===")

# Beispiel MIT Observer Pattern
class Observer:
    # Basisklasse für alle Beobachter
    def update(self, temperature):
        # Wird vom Subject aufgerufen, wenn sich die Temperatur ändert
        pass

class TemperatureSensor:
    def __init__(self):
        # Initialisiert die Temperatur und die Liste der Beobachter
        self.temperature = 20
        self.observers = []

    def add_observer(self, observer):
        # Fügt einen neuen Beobachter hinzu
        self.observers.append(observer)

    def set_temperature(self, value):
        # Setzt die Temperatur und benachrichtigt alle Beobachter
        self.temperature = value
        self.notify_observers()

    def notify_observers(self):
        # Benachrichtigt alle registrierten Beobachter über die neue Temperatur
        for observer in self.observers:
            observer.update(self.temperature)

class Heater(Observer):
    def update(self, temperature):
        # Reagiert auf Temperaturänderungen
        if temperature < 18:
            print("Heater: Heizung eingeschaltet.")
        else:
            print("Heater: Heizung ausgeschaltet.")

class Cooler(Observer):
    def update(self, temperature):
        # Reagiert auf Temperaturänderungen
        if temperature > 25:
            print("Cooler: Kühlung eingeschaltet.")
        else:
            print("Cooler: Kühlung ausgeschaltet.")

# Beispiel-Nutzung mit Observer
sensor2 = TemperatureSensor()    # Erstellt einen Temperatursensor
heater2 = Heater()               # Erstellt eine Heizung als Observer
cooler2 = Cooler()               # Erstellt eine Kühlung als Observer

sensor2.add_observer(heater2)    # Registriert die Heizung beim Sensor
sensor2.add_observer(cooler2)    # Registriert die Kühlung beim Sensor

sensor2.set_temperature(16)      # Setzt die Temperatur, alle Observer werden automatisch benachrichtigt
sensor2.set_temperature(28)      # Setzt eine neue Temperatur, alle Observer werden automatisch benachrichtigt