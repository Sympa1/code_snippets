from datetime import datetime


class Logger:
    def __init__(self, log_file_name: str = "error.log"):
        """
        Diese Klasse stellt einen Logger bereit, der Nachrichten und Fehlermeldungen
        in eine Protokolldatei schreibt. Die Einträge werden mit einem Zeitstempel und einer Überschrift versehen.
        Die Konstruktor-Methode erwartet einen Dateinamen als Parameter.
        """
        self._log_file_name = log_file_name  # _ = protected

    def write_to_log_file(self, message: str, headline: str = "Error"):
        """
        Schreibt einen Eintrag in das Log-File.
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"===== {headline} ===== \n{timestamp} - {message}\n\n"

        with open(self._log_file_name, 'a', encoding='utf-8') as f:  # a = append - Eintrag der Datei hinzufügen
            f.write(log_entry)


# Testen
if __name__ == "__main__":
    logger = Logger()
    logger.write_to_log_file("Ich bin ein Test.", "ich bin eine Überschrift")