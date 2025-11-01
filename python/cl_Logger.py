from datetime import datetime


class Logger:
    """
    Context Manager für das Schreiben von Log-Einträgen in eine Datei.

    Diese Klasse ermöglicht das strukturierte Protokollieren von Nachrichten,
    Warnungen und Fehlern. Jeder Eintrag wird mit einem Zeitstempel versehen
    und kann mit einer individuellen Überschrift kategorisiert werden.

    Verwendung als Context Manager:
        with Logger() as log:
            log.write_to_log_file("Nachricht", "Überschrift")

    Attributes:
        _log_file_name (str): Pfad zur Log-Datei (default: "error.log")
    """

    def __init__(self, log_file_name: str = "error.log"):
        """
        Initialisiert den Logger mit einem Dateinamen.

        Args:
            log_file_name (str): Name/Pfad der Log-Datei.
                                 Default ist "error.log" im aktuellen Verzeichnis.

        Note:
            Das Präfix '_' markiert _log_file_name als protected (Konvention).
        """
        self._log_file_name = log_file_name

    def __enter__(self):
        """
        Wird beim Betreten des Context Managers aufgerufen.

        Ermöglicht die Verwendung der 'with'-Anweisung.

        Returns:
            Logger: Die Logger-Instanz selbst für die Verwendung im with-Block.

        Example:
            with Logger() as log:  # <- __enter__() wird hier aufgerufen
                log.write_to_log_file("Test")
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Wird beim Verlassen des Context Managers aufgerufen.

        Gibt Exception-Details in der Konsole aus, falls eine Exception
        im with-Block aufgetreten ist. Die Exception wird anschließend
        weitergegeben (nicht unterdrückt).

        Args:
            exc_type: Exception-Typ (z.B. ValueError, None wenn keine Exception)
            exc_val: Exception-Wert/Nachricht (z.B. "ungültiger Wert")
            exc_tb: Traceback-Objekt (Stacktrace der Exception)

        Returns:
            False: Exception wird weitergegeben (nicht unterdrückt).
                   True würde die Exception unterdrücken (nicht empfohlen!).

        Note:
            Kein Cleanup nötig, da die Log-Datei in write_to_log_file()
            bereits mit 'with open()' automatisch geschlossen wird.
        """
        # Prüfen, ob eine Exception aufgetreten ist
        if exc_type is not None:
            # Exception-Details rot formatiert in der Konsole ausgeben
            print(f"\033[31mException im Logger-Context: {exc_type.__name__}: {exc_val}\033[0m")

        # False = Exception wird weitergegeben (nicht unterdrücken)
        return False

    def write_to_log_file(self, message: str, headline: str = "Error"):
        """
        Schreibt einen formatierten Eintrag in die Log-Datei.

        Der Eintrag wird im Append-Modus ('a') ans Ende der Datei angefügt,
        sodass vorherige Einträge erhalten bleiben. Jeder Eintrag enthält:
        - Eine Überschrift (z.B. "Error", "Warning", "Info")
        - Einen Zeitstempel (Format: YYYY-MM-DD HH:MM:SS)
        - Die eigentliche Nachricht
        - Zwei Leerzeilen als Trenner zum nächsten Eintrag

        Args:
            message (str): Die zu protokollierende Nachricht.
            headline (str): Kategorisierung des Eintrags (default: "Error").
                           Beispiele: "Error", "Warning", "Info", "Debug"

        Example:
            log.write_to_log_file("Datei nicht gefunden", "Warning")

            # Erzeugt in error.log:
            # ===== Warning =====
            # 2025-01-19 14:30:15 - Datei nicht gefunden
            #

        Note:
            - Der Modus 'a' (append) stellt sicher, dass die Datei nicht
              überschrieben wird und jeder Aufruf einen neuen Eintrag anfügt.
            - UTF-8 Encoding gewährleistet korrekte Darstellung von Umlauten.
            - Die Datei wird automatisch durch 'with' geschlossen.
        """
        # Aktuellen Zeitstempel generieren
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Formatierte Log-Nachricht mit Überschrift, Zeitstempel und Nachricht erstellen
        log_entry = f"===== {headline} ===== \n{timestamp} - {message}\n\n"

        # Datei im Append-Modus öffnen und Eintrag hinzufügen
        # 'a' = append (anhängen, nicht überschreiben)
        # encoding='utf-8' = Umlaute und Sonderzeichen korrekt speichern
        # 'with' = Datei wird automatisch geschlossen, auch bei Fehlern
        with open(self._log_file_name, 'a', encoding='utf-8') as f:
            f.write(log_entry)


# Testen
if __name__ == "__main__":
    # Gibt autom. Ressourcen frei - ähnlich zu using in C#
    with Logger() as log:
        log.write_to_log_file("Nachricht", "Überschrift")
