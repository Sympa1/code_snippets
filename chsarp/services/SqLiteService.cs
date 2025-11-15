using Microsoft.Data.Sqlite; // --> NuGet Paket installieren
using DotNetEnv; // --> NuGet Paket installieren

// TODO: Muss noch überabreitet werden.
//  Ich möchte den Beispielaufruf hier auch integrieren.

namespace chsarp.services
{
    /// <summary>
    /// Service für die Verwaltung der SQLite-Datenbankverbindung.
    /// Verwaltet den Lebenszyklus der Verbindung und stellt Methoden zum Öffnen und Schließen bereit.
    /// Implementiert IDisposable für eine ordnungsgemäße Ressourcenfreigabe.
    /// </summary>
    public class SqLiteService : IDisposable
    {
        /// <summary>
        /// Die Verbindungszeichenfolge für die SQLite-Datenbank.
        /// Wird aus den Umgebungsvariablen oder mit einem Standard-Dateinamen erstellt.
        /// </summary>
        private readonly string _connectionString;

        /// <summary>
        /// Die aktuelle SQLite-Verbindung.
        /// Kann null sein, wenn noch keine Verbindung geöffnet wurde.
        /// </summary>
        private SqliteConnection? _connection;

        /// <summary>
        /// Initialisiert eine neue Instanz des SqLiteService.
        /// Versucht zunächst, den Datenbankpfad aus der Umgebungsvariable SQLITE_DATABASE zu lesen.
        /// Falls nicht vorhanden, wird "test.db" als Standardpfad verwendet.
        /// </summary>
        /// <remarks>
        /// Die Verbindung wird im Konstruktor noch nicht geöffnet. Dazu ist ein Aufruf von OpenConnection() erforderlich.
        /// </remarks>
        public SqLiteService()
        {
            var databasePath = Env.GetString("SQLITE_DATABASE");
            
            if (string.IsNullOrEmpty(databasePath))
            {
                databasePath = "test.db"; // Platziert das Datenbankfile im Stammverzeichnis des Projekts ../bin/Debug/netX.X/
            }

            _connectionString = $"Data Source={databasePath}";
        }

        /// <summary>
        /// Initialisiert eine neue Instanz des SqLiteService mit einem benutzerdefinierten Datenbankpfad.
        /// </summary>
        /// <param name="databasePath">Der Pfad zur SQLite-Datenbankdatei.</param>
        /// <remarks>
        /// Die Verbindung wird im Konstruktor noch nicht geöffnet. Dazu ist ein Aufruf von OpenConnection() erforderlich.
        /// </remarks>
        public SqLiteService(string databasePath)
        {
            if (string.IsNullOrEmpty(databasePath))
            {
                FileLogService.WriteToLog("SQLite-Datenbankpfad ist leer.");
                throw new ArgumentException("Datenbankpfad darf nicht leer sein.", nameof(databasePath));
            }

            _connectionString = $"Data Source={databasePath}";
        }

        /// <summary>
        /// Öffnet die SQLite-Datenbankverbindung.
        /// Erstellt eine neue Verbindung basierend auf der Verbindungszeichenfolge und öffnet sie.
        /// </summary>
        /// <returns>Die geöffnete SqliteConnection oder null, wenn ein Fehler auftritt.</returns>
        /// <remarks>
        /// Bei Fehlern wird die Exception protokolliert und null zurückgegeben.
        /// </remarks>
        public SqliteConnection? OpenConnection()
        {
            try
            {
                _connection = new SqliteConnection(_connectionString);
                _connection.Open();
                return _connection;
            }
            catch (Exception e)
            {
                FileLogService.WriteToLog($"SQLite-Verbindungsfehler: {e}");
                return null;
            }
        }

        /// <summary>
        /// Schließt die SQLite-Datenbankverbindung, falls sie geöffnet ist.
        /// Prüft zunächst, ob die Verbindung nicht null und offen ist, bevor sie geschlossen wird.
        /// </summary>
        /// <remarks>
        /// Diese Methode ist sicher und wirft keine Exception, wenn die Verbindung bereits geschlossen oder null ist.
        /// </remarks>
        public void CloseConnection()
        {
            if (_connection?.State == System.Data.ConnectionState.Open)
            {
                _connection.Close();
            }
        }

        /// <summary>
        /// Erstellt einen neuen SqliteCommand für die Ausführung von SQL-Befehlen.
        /// </summary>
        /// <returns>Ein neuer SqliteCommand, der mit dieser Verbindung verknüpft ist.</returns>
        /// <remarks>
        /// Die Verbindung muss vorher mit OpenConnection() geöffnet werden.
        /// </remarks>
        public SqliteCommand CreateCommand()
        {
            if (_connection == null)
            {
                throw new InvalidOperationException("Verbindung ist nicht geöffnet. Rufen Sie OpenConnection() auf.");
            }
            return _connection.CreateCommand();
        }

        /// <summary>
        /// Gibt die Ressourcen (SQLite-Verbindung) frei.
        /// Sollte aufgerufen werden, wenn der SqLiteService nicht mehr benötigt wird.
        /// </summary>
        /// <remarks>
        /// Diese Methode implementiert das IDisposable-Interface.
        /// Am besten wird der SqLiteService in einem 'using'-Statement verwendet, um automatische Ressourcenfreigabe zu gewährleisten.
        /// </remarks>
        public void Dispose()
        {
            _connection?.Dispose();
        }
    }
}