"""
Problemstellung:
Bei unterschiedlichen Sammlungen von Objekten, mit unterschiedlichen internen Aufbau und mit unterschiedlichen
Elementzugriff, ein Client nacheinander auf alle Elemente zugreifen kann, ohne die interne Struktur der
Sammlung zu kennen.

Beispiele:
Als Beispiel kann das Java Collections Frammework dienen, das verschiedene Sammlungen (Listen, Mengen, Karten)
mit unterschiedlichen internen Strukturen (Array, verkettete Liste, Baum) bereitstellt.
Aber auch Dateien in einem Verzeichnis kämen in Frage. Alternativ auch Objektmengen miit unbekannter
größe und Struktur, die z.B. aus einer Datenbank gelesen werden.

Kurze Erklärung:
Ein Iterator stellt eine einheitliche Schnittstelle zum sequentiellen Zugriff auf die Elemente
einer Sammlung bereit. Der Client kann so die Elemente einer Sammlung durchlaufen, ohne die
interne Struktur der Sammlung zu kennen. Der Iterator hält den aktuellen Zustand des Durchlaufs
und bietet Methoden zum Vorwärtsbewegen und zum Abrufen des aktuellen Elements.

Nachteile:
Der Iterator kann zusätzlichen Speicherbedarf verursachen, insbesondere bei großen Sammlungen.

"""

# Einfache Collection auf Basis einer Liste
class ListCollection:
    def __init__(self, items):
        # Initialisiert die Collection mit einer Liste von Elementen
        self.items = items

    def create_iterator(self):
        # Gibt einen Iterator für diese Collection zurück
        return ListIterator(self)

class ListIterator:
    def __init__(self, collection):
        # Speichert die Collection und den aktuellen Index
        self.collection = collection
        self.index = 0

    def has_next(self):
        # Prüft, ob noch weitere Elemente vorhanden sind
        return self.index < len(self.collection.items)

    def next(self):
        # Gibt das aktuelle Element zurück und geht zum nächsten weiter
        if self.has_next():
            item = self.collection.items[self.index]
            self.index += 1
            return item
        else:
            return None

# Collection auf Basis einer Menge (set)
class SetCollection:
    def __init__(self, items):
        # Initialisiert die Collection mit einer Menge von Elementen
        self.items = set(items)
        self.items_list = list(self.items)  # Für den Iterator als Liste speichern

    def create_iterator(self):
        # Gibt einen Iterator für diese Collection zurück
        return SetIterator(self)

class SetIterator:
    def __init__(self, collection):
        # Speichert die Collection und den aktuellen Index
        self.collection = collection
        self.index = 0

    def has_next(self):
        # Prüft, ob noch weitere Elemente vorhanden sind
        return self.index < len(self.collection.items_list)

    def next(self):
        # Gibt das aktuelle Element zurück und geht zum nächsten weiter
        if self.has_next():
            item = self.collection.items_list[self.index]
            self.index += 1
            return item
        else:
            return None

# Collection auf Basis eines Dictionaries
class DictCollection:
    def __init__(self, items):
        # Initialisiert die Collection mit einem Dictionary
        self.items = dict(items)
        self.keys = list(self.items.keys())  # Für den Iterator die Schlüssel speichern

    def create_iterator(self):
        # Gibt einen Iterator für diese Collection zurück
        return DictIterator(self)

class DictIterator:
    def __init__(self, collection):
        # Speichert die Collection und den aktuellen Index
        self.collection = collection
        self.index = 0

    def has_next(self):
        # Prüft, ob noch weitere Elemente vorhanden sind
        return self.index < len(self.collection.keys)

    def next(self):
        # Gibt das aktuelle Element (Schlüssel-Wert-Paar) zurück und geht zum nächsten weiter
        if self.has_next():
            key = self.collection.keys[self.index]
            value = self.collection.items[key]
            self.index += 1
            return (key, value)
        else:
            return None

# Beispiel-Nutzung
if __name__ == "__main__":
    print("ListCollection:")
    list_collection = ListCollection([1, 2, 3])
    list_iterator = list_collection.create_iterator()
    while list_iterator.has_next():
        print(list_iterator.next())

    print("\nSetCollection:")
    set_collection = SetCollection([4, 5, 6])
    set_iterator = set_collection.create_iterator()
    while set_iterator.has_next():
        print(set_iterator.next())

    print("\nDictCollection:")
    dict_collection = DictCollection({'a': 7, 'b': 8, 'c': 9})
    dict_iterator = dict_collection.create_iterator()
    while dict_iterator.has_next():
        print(dict_iterator.next())