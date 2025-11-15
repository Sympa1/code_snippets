namespace chsarp.services
{
    /// <summary>
    /// Statischer Service für das Protokollieren von Fehlern in einer Logdatei.
    /// Schreibt Fehlermeldungen mit Zeitstempel in die Datei "error.log" im Anwendungsverzeichnis.
    /// </summary>
    public static class FileLogService
    {
        /// <summary>
        /// Pfad zur Logdatei. Wird im Anwendungsverzeichnis erstellt und gespeichert.
        /// Der Standardname ist "error.log".
        /// </summary>
        private static readonly string LogFilePath = Path.Combine(
            AppDomain.CurrentDomain.BaseDirectory,
            "error.log");

        /// <summary>
        /// Schreibt eine Fehlermeldung mit Zeitstempel in die Logdatei.
        /// Falls das Verzeichnis nicht existiert, wird es automatisch erstellt.
        /// Jeder Eintrag ist durch "===== ERROR =====" und "=================" begrenzt.
        /// </summary>
        /// <param name="message">Die Fehlermeldung, die geloggt werden soll. Kann null oder leer sein.</param>
        /// <remarks>
        /// Die Methode ist statisch und kann daher direkt über die Klasse aufgerufen werden.
        /// Fehlermeldungen werden an die vorhandene Datei angehängt (append: true).
        /// Der Zeitstempel folgt dem Format: yyyy-MM-dd HH:mm:ss
        /// </remarks>
        public static void WriteToLog(string message)
        {
            //check if dir exist - the ! silence the warning, because it might return null
            Directory.CreateDirectory(Path.GetDirectoryName(LogFilePath)!);

            using (StreamWriter streamwriter = new StreamWriter(LogFilePath, append: true))
            {
                streamwriter.WriteLine("===== ERROR =====");
                streamwriter.WriteLine($"Timestamp: {DateTime.Now:yyyy-MM-dd HH:mm:ss}");

                if (!string.IsNullOrWhiteSpace(message))
                    streamwriter.WriteLine($"Message: {message}");
                streamwriter.WriteLine("=================\n");
            }
        }
    }
}