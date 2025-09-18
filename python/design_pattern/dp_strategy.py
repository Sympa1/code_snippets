"""
Problemstellung:
Das Verhalten eines Objekts soll zur Laufzeit festgelegt und auch geändert werden können.
Dabei soll aus einer Gruppe vopn Algorithmen der passende ausgewählt werden.
Das Verhalten soll also unabhängig vom Objekt variiert werden können.

Beispiele:
Eine Auswahl aus verschiedenen Sortieralgorithmen (z.B. BubbleSort, QuickSort, MergeSort).
Speichern einer Datei in verschiedenen Formaten (z.B. JSON, XML, CSV).
Ein Computerspiel mit verschiedenen Autos, die unterschiedlich gut beschleunigen oder bremsen.

Kurze Erklärung:
Das Strategy-Pattern definiert eine Familie von Algorithmen, kapselt jeden Algorithmus und macht sie
austauschbar. Das Strategy-Pattern ermöglicht es, das Verhalten eines Objekts zur Laufzeit zu ändern.

Nachteile:
- Erhöhter Aufwand für die Implementierung, da das Subject die Beobachter verwalten muss.
- Es werden alle Änderungen an den Beobachter weitergegeben, auch wennn diese nicht relevant sind.
- Beim löschen eines Beobachters muss darauf geachtet werden, dass diese auch beim Subject entfernt werden.
"""

# In C# wäre Engine ein Interface, das die Methode accelerate() vorschreibt.
# In Python gibt es keine echten Interfaces, daher wird hier eine Basisklasse verwendet, deren Methode von
# den Unterklassen überschrieben wird.
class Engine:
    def drive(self):
        # Methode, die von konkreten Motoren überschrieben wird
        pass

class SportEngine(Engine):
    def drive(self):
        print("SportEngine: Das Auto beschleunigt sehr schnell!")

class EcoEngine(Engine):
    def drive(self):
        print("EcoEngine: Das Auto beschleunigt langsam und sparsam.")

class Brake:
    def brake(self):
        # Methode, die von konkreten Bremsen überschrieben wird
        pass

class DiscBrake(Brake):
    def brake(self):
        print("DiscBrake: Das Auto bremst kräftig.")

class DrumBrake(Brake):
    def brake(self):
        print("DrumBrake: Das Auto bremst sanft.")

class AudioSystem:
    def play_music(self):
        # Methode, die von konkreten Audiosystemen überschrieben wird
        pass

class PremiumAudio(AudioSystem):
    def play_music(self):
        print("PremiumAudio: Musik klingt fantastisch!")

class StandardAudio(AudioSystem):
    def play_music(self):
        print("StandardAudio: Musik klingt okay.")

class Car:
    def __init__(self, engine, brake, audio):
        # Initialisiert das Auto mit Engine-, Brake- und AudioSystem-Strategie
        self.engine = engine
        self.brake = brake
        self.audio = audio

    def drive(self):
        # Führt die aktuelle Engine-Strategie aus
        self.engine.drive()

    def brake_car(self):
        # Führt die aktuelle Brake-Strategie aus
        self.brake.brake()

    def play_music(self):
        # Führt die aktuelle AudioSystem-Strategie aus
        self.audio.play_music()

# Beispiel-Nutzung
engine = SportEngine()           # Erstellt einen Sportmotor
brake = DiscBrake()              # Erstellt eine Scheibenbremse
audio = PremiumAudio()           # Erstellt ein Premium-Audiosystem

car = Car(engine, brake, audio)  # Erstellt ein Auto mit den gewählten Strategien

car.drive()                      # Ausgabe: SportEngine: Das Auto beschleunigt sehr schnell!
car.brake_car()                  # Ausgabe: DiscBrake: Das Auto bremst kräftig.
car.play_music()                 # Ausgabe: PremiumAudio: Musik klingt fantastisch!

# Strategien zur Laufzeit ändern
car.engine = EcoEngine()         # Wechselt auf Sparmotor
car.brake = DrumBrake()          # Wechselt auf Trommelbremse
car.audio = StandardAudio()      # Wechselt auf Standard-Audiosystem

car.drive()                      # Ausgabe: EcoEngine: Das Auto beschleunigt langsam und sparsam.
car.brake_car()                  # Ausgabe: DrumBrake: Das Auto bremst sanft.
car.play_music()                 # Ausgabe: StandardAudio: Musik klingt okay.