"""
Problemstellung:
Von einer Klasse soll nur genau eine Instanz existieren.
Allen interessierten Clients soll Zugang zu dieser einen Instanz ermöglicht werden.
Zugriff sollte für die Clients möglichst einfach sein.

Beispiele:
Ein zentraler Cache.
Eine zentrale Verwaltung externer Ressourcen (z.B. Logdateien oder programmweite Konfigurationsdateien).
Effizientes Zurverfügungstellen von Nur-Lese-Daten.

Kurze Erklärung:
Ein Singleton stellt sicher, dass von einer Klasse nur eine einzige Instanz existiert und alle Clients auf diese Instanz zugreifen können.
Die einfache Variante ist nicht thread-sicher und eignet sich für Single-Thread-Anwendungen.
Die thread-sichere Variante verwendet einen Lock, damit auch bei parallelem Zugriff aus mehreren Threads garantiert nur eine Instanz erzeugt wird.
Beide Varianten bieten eine Dummy-Methode, um die Nutzung zu demonstrieren.
"""

# Einfacher Singleton (nicht thread-sicher)
class SimpleSingleton:
    _instance = None  # Klassenvariable, speichert die einzige Instanz der Klasse

    def __new__(cls):
        # __new__ ist die Methode, die eine neue Instanz erzeugt, bevor __init__ ausgeführt wird.
        # 'cls' ist ein Verweis auf die Klasse selbst, nicht auf eine Instanz.
        # Hier wird geprüft, ob bereits eine Instanz existiert.
        if cls._instance is None:
            # Falls noch keine Instanz existiert, wird sie mit super().__new__ erzeugt.
            cls._instance = super().__new__(cls)
        # Gibt die (neue oder bestehende) Instanz zurück.
        return cls._instance

    def do_something(self):
        # Dummy-Methode, die eine Aktion simuliert.
        print("SimpleSingleton tut etwas.")

# Beispiel-Nutzung des einfachen Singletons
singleton1 = SimpleSingleton()  # Erstellt die Instanz (oder gibt die bestehende zurück)
singleton2 = SimpleSingleton()  # Gibt dieselbe Instanz zurück wie singleton1
print(singleton1 is singleton2)  # True, beide Variablen zeigen auf dieselbe Instanz
singleton1.do_something()        # Führt die Dummy-Methode aus


# Thread-sicherer Singleton
import threading  # Importiert das threading-Modul für Thread-Sicherheit

class ThreadSafeSingleton:
    _instance = None  # Klassenvariable, speichert die einzige Instanz der Klasse
    # Lock-Objekt, um parallelen Zugriff zu synchronisieren.
    # Ein Lock sorgt dafür, dass immer nur ein Thread den kritischen Bereich betreten kann.
    # So wird verhindert, dass zwei Threads gleichzeitig die Instanz erzeugen und es am Ende zwei Instanzen gibt.
    _lock = threading.Lock()  

    def __new__(cls):
        # Mit dem Lock wird verhindert, dass mehrere Threads gleichzeitig eine Instanz erzeugen.
        # Der 'with'-Block sorgt dafür, dass das Lock vor Eintritt in den kritischen Bereich erworben wird
        # und nach Verlassen automatisch wieder freigegeben wird.
        with cls._lock:
            # Innerhalb des Locks wird geprüft, ob die Instanz bereits existiert.
            # Nur der Thread, der das Lock hält, kann diese Prüfung und ggf. die Instanzerzeugung durchführen.
            if cls._instance is None:
                # Falls noch keine Instanz existiert, wird sie erzeugt.
                cls._instance = super().__new__(cls)
        # Gibt die (neue oder bestehende) Instanz zurück.
        return cls._instance

    def do_something(self):
        # Dummy-Methode, die eine Aktion simuliert.
        print("ThreadSafeSingleton tut etwas.")

# Beispiel-Nutzung des thread-sicheren Singletons
ts_singleton1 = ThreadSafeSingleton()  # Erstellt die Instanz (oder gibt die bestehende zurück)
ts_singleton2 = ThreadSafeSingleton()  # Gibt dieselbe Instanz zurück wie ts_singleton1
print(ts_singleton1 is ts_singleton2)  # True, beide Variablen zeigen auf dieselbe Instanz
ts_singleton1.do_something()           # Führt die Dummy-Methode aus