using DotNetEnv; // --> NuGet Paket installieren

namespace chsarp.services
{
    /// <summary>
    /// Service zum Laden von Umgebungsvariablen aus einer .env-Datei.
    /// Liest die Konfigurationsdatei ".env" aus dem Anwendungsverzeichnis und lädt die Variablen in den Prozess.
    /// </summary>
    public class EnvLoadService
    {
        /// <summary>
        /// Lädt die Umgebungsvariablen aus der .env-Datei.
        /// Sucht die Datei im aktuellen Arbeitsverzeichnis (Chronolyze_Api/).
        /// Falls die Datei nicht gefunden wird, wird eine entsprechende Meldung ausgegeben und geloggt.
        /// </summary>
        /// <remarks>
        /// Diese Methode ist statisch und wird typischerweise beim Anwendungsstart aufgerufen.
        /// Wenn die .env-Datei existiert, werden alle Variablen mit Env.Load() geladen.
        /// Falls nicht, wird eine Warnung in der Konsole und im Error-Log ausgegeben.
        /// </remarks>
        public static void LoadDotEnv()
        {
            // Aktuelles Arbeitsverzeichnis (Chronolyze_Api/)
            string currentDir = Environment.CurrentDirectory;

            // .env liegt direkt im Chronolyze_Api/ Verzeichnis
            string envPath = Path.Combine(currentDir, ".env");

            Console.WriteLine($"Suche .env in: {envPath}");

            if (File.Exists(envPath))
            {
                Env.Load(envPath);
                Console.WriteLine(".env erfolgreich geladen!");
            }
            else
            {
                Console.WriteLine($".env-Datei nicht gefunden! Gesucht in: {envPath}");
                //FileLogService.WriteToLog($".env-Datei nicht gefunden! Gesucht in: {envPath}");
            }
        }
    }
}