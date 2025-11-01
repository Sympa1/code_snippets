import os

class EnvLoader:
    """
    Lädt und verwaltet Umgebungsvariablen aus einer .env-Datei.

    Diese Klasse ermöglicht das strukturierte Lesen von Konfigurationswerten
    aus einer .env-Datei. Die Variablen werden in einem internen Dictionary
    gespeichert und können über get_var() abgerufen werden.

    Unterstützte .env-Formate:
        KEY=value\n
        KEY="value"\n
        KEY='value'\n
        # Kommentarzeilen werden ignoriert

    Example:
        env = EnvLoader()
        if env.load_env_file('.env'):
            repo_path = env.get_var('REPO_PFAD_LIN')

    Attributes:
        _env_vars (dict): Dictionary zum Speichern der geladenen Variablen.
                         Key = Variablenname, Value = Variablenwert
    """

    def __init__(self):
        """
        Initialisiert den EnvLoader mit einem leeren Dictionary.

        Das Dictionary _env_vars wird verwendet, um alle geladenen
        Umgebungsvariablen aus der .env-Datei zu speichern.

        Note:
            Das Präfix '_' markiert _env_vars als protected (Konvention).
        """
        self._env_vars = {}

    def load_env_file(self, env_path: str) -> bool:
        """
        Die Methode liest die angegebene .env-Datei zeilenweise, parst
        Key-Value-Paare und speichert sie im internen Dictionary.
        Fehler werden in der Konsole ausgegeben und geloggt.

        Parsing-Regeln:
        - Leerzeilen werden ignoriert
        - Zeilen mit '#' am Anfang werden als Kommentare ignoriert
        - Format: KEY=VALUE (Leerzeichen um '=' werden entfernt)
        - Anführungszeichen (', ") um Values werden entfernt

        Args:
            env_path (str): Pfad zur .env-Datei (relativ oder absolut).
                           Beispiel: '.env', '/path/to/config.env'

        Returns:
            bool: True bei erfolgreichem Laden, False bei Fehler.

        Example:
            # .env-Datei:
            # REPO_PFAD_LIN=/home/user/repo
            # DEBUG="true"

            if env.load_env_file('.env'):
                print("Erfolgreich geladen!")

        Note:
            - Fehler werden rot in der Konsole ausgegeben
            - Warnings werden gelb ausgegeben
            - Erfolg wird grün ausgegeben
            - Alle Fehler werden zusätzlich in die Log-Datei geschrieben
        """
        if not os.path.exists(env_path):
            # Warnung in Gelb ausgeben
            print(f"\033[33mWARNUNG: .env-Datei nicht gefunden unter: {env_path}\033[0m")

            return False

        try:
            # .env-Datei mit UTF-8 Encoding öffnen
            # 'r' = read-only Modus
            # encoding='utf-8' = Umlaute und Sonderzeichen korrekt lesen
            with open(env_path, 'r', encoding='utf-8') as file:
                # Jede Zeile der Datei durchgehen
                for line in file:
                    # Leerzeichen/Tabs am Anfang und Ende entfernen
                    line = line.strip()

                    # Prüfen, ob Zeile gültig ist:
                    # - Nicht leer
                    # - Kein Kommentar (startet nicht mit '#')
                    # - Enthält '=' (Key-Value-Trenner)
                    if line and not line.startswith('#') and '=' in line:
                        # Zeile bei erstem '=' in Key und Value aufteilen
                        # maxsplit=1 verhindert, dass '=' im Value selbst als Trenner gilt
                        key, value = line.split('=', 1)

                        # Leerzeichen um Key und Value entfernen
                        key = key.strip()

                        # Leerzeichen entfernen und Anführungszeichen (', ") am Anfang/Ende entfernen
                        # strip('"').strip("'") entfernt beide Arten von Anführungszeichen
                        value = value.strip().strip('"').strip("'")

                        # Key-Value-Paar im Dictionary speichern
                        self._env_vars[key] = value
            return True

        except Exception as e:
            # Fehler beim Lesen der Datei (z.B. Encoding-Problem, Zugriffsverweigerung)
            # Fehlermeldung rot in der Konsole ausgeben
            print(f"\033[31mFEHLER beim Lesen der .env-Datei: {e}\033[0m")

            return False

    def get_var(self, key: str, default: str = None) -> str | None:
        """
        Gibt den Wert einer geladenen Umgebungsvariable zurück.

        Diese Methode ermöglicht den sicheren Zugriff auf Variablen,
        die mit load_env_file() geladen wurden. Wenn die Variable nicht
        existiert, wird ein optionaler Standardwert zurückgegeben.

        Args:
            key (str): Name der Umgebungsvariable (z.B. 'REPO_PFAD_LIN').
            default (str, optional): Standardwert, falls Variable nicht existiert.
                                    Default ist None.

        Returns:
            str | None: Wert der Variable oder default-Wert.

        Example:
            # Mit Standardwert:
            repo_path = env.get_var('REPO_PFAD_LIN', '/default/path')

            # Ohne Standardwert:
            debug_mode = env.get_var('DEBUG')
            if debug_mode is None:
                print("DEBUG nicht gesetzt")

        Note:
            - Gibt None zurück, wenn die Variable nicht existiert und kein
              default-Wert angegeben wurde.
            - Es wird nicht geprüft, ob load_env_file() erfolgreich war.
              Bei leerem Dictionary wird immer default zurückgegeben.
        """
        # Dictionary.get() gibt entweder den Wert für den key zurück oder default, falls der key nicht existiert
        return self._env_vars.get(key, default)
