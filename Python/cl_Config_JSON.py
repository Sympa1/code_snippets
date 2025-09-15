import json

class Config:
    """
    Eine Klasse zur Verwaltung der Konfigurationseinstellungen in einer JSON-Datei.
    """
    def __init__(self, filename = "config.json"):
        self.filename = filename
        self.data = {}
        self.load_config() # lädt automatisch die Config beim erstellen des Objektes

    def load_config(self):
        """Liest die config.json ein. Wenn die Datei nicht existiert, wird eine neue erstellt mit Standardwerten."""
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError as e:
            # Default values wenn datei nicht existiert
            self.data = {
                "debug": False,
                "theme": "dark",
                "window_width": 800,
                "window_height": 600
            }
            self.save_config()

            # Fehlerprotokoll schreiben
            self.write_to_log("Config.json existiert nicht." + str(e))
            self.config_created = True

    def save_config(self):
        """Speichere config in Datei."""
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def get_config(self, key):
        """Gibt den Wert für den angegebenen Schlüssel zurück, oder None, wenn der Schlüssel nicht existiert."""
        return self.data.get(key)
    
    def set_config(self, key, value):
        """Setzt den Wert für den angegebenen Schlüssel und speichert die config.json."""
        self.data[key] = value
        self.save_config()