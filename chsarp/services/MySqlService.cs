using DotNetEnv; // --> NuGet Paket installieren
using MySql.Data.MySqlClient; // --> NuGet Paket installieren

namespace chsarp.services
{
    /// <summary>
    /// Service für die Verwaltung der MySQL-Datenbankverbindung.
    /// Verwaltet den Lebenszyklus der Verbindung und stellt Methoden zum Öffnen und Schließen bereit.
    /// Implementiert IDisposable für eine ordnungsgemäße Ressourcenfreigabe.
    /// </summary>
    public class DatabaseService : IDisposable
    {
        /// <summary>
        /// Die Verbindungszeichenfolge für die MySQL-Datenbank.
        /// Wird aus den Umgebungsvariablen in der .env-Datei geladen.
        /// </summary>
        private readonly string _connectionString;
        
        /// <summary>
        /// Die aktuelle MySQL-Verbindung.
        /// Kann null sein, wenn noch keine Verbindung geöffnet wurde.
        /// </summary>
        private MySqlConnection _connection;
        
        /// <summary>
        /// Initialisiert eine neue Instanz des DatabaseService.
        /// Liest die MySQL-Verbindungsdaten aus den Umgebungsvariablen (MYSQL_SERVER, MYSQL_PORT, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD).
        /// Erstellt die Verbindungszeichenfolge mit TLS 1.3-Verschlüsselung.
        /// </summary>
        /// <exception cref="Exception">Wird geworfen, wenn erforderliche Umgebungsvariablen fehlen.</exception>
        /// <remarks>
        /// Die Verbindung wird im Konstruktor noch nicht geöffnet. Dazu ist ein Aufruf von OpenConnection() erforderlich.
        /// Bei fehlenden Verbindungsdaten wird eine Exception protokolliert und eine Exception geworfen.
        /// </remarks>
        public DatabaseService()
        {
            var server = Env.GetString("MYSQL_SERVER");
            var port = Env.GetInt("MYSQL_PORT");
            var database = Env.GetString("MYSQL_DATABASE");
            var user = Env.GetString("MYSQL_USER");
            var password = Env.GetString("MYSQL_PASSWORD");

            if (string.IsNullOrEmpty(server) || string.IsNullOrEmpty(database) || string.IsNullOrEmpty(user) ||
                string.IsNullOrEmpty(password))
            {
                FileLogService.WriteToLog("MySQL-Verbindungsdaten fehlen.");
                throw new Exception("MySQL-Verbindungsdaten fehlen."); // Erzeuge eine Exception.
            }

            //_connectionString = $"Server={server};Port={port};Database={database};Uid={user};Pwd={password};SslMode=none;";

            var _connectionStringBuilder = new MySqlConnectionStringBuilder
            {
                Server = server,
                Port = Convert.ToUInt32(port),
                Database = database,
                UserID = user,
                Password = password,
                SslMode = MySqlSslMode.Required, // Alternativ None oder Preferred oder Required

                // Explizit die zu verwendende TLS-Version angeben.
                // Wir versuchen es zuerst mit der sichersten Variante, die MySQL 5.7 evtl. kann.
                TlsVersion = "Tls13"
            };
            _connectionString = _connectionStringBuilder.ConnectionString;
        }

        //public MySqlConnection Connection => _connection;
        public MySqlCommand CreateCommand() => _connection.CreateCommand();
        
        /// <summary>
        /// Öffnet die MySQL-Datenbankverbindung.
        /// Erstellt eine neue Verbindung basierend auf der Verbindungszeichenfolge und öffnet sie.
        /// </summary>
        /// <returns>Die geöffnete MySqlConnection oder null, wenn ein Fehler auftritt.</returns>
        /// <remarks>
        /// Bei Fehlern wird die Exception protokolliert und null zurückgegeben.
        /// </remarks>
        public MySqlConnection OpenConnection()
        {
            try
            {
                _connection = new MySqlConnection(_connectionString);
                _connection.Open();
                return _connection;
            }
            catch (Exception e)
            {
                FileLogService.WriteToLog($"{e}");
                return null;
            }
        }
        
        /// <summary>
        /// Schließt die MySQL-Datenbankverbindung, falls sie geöffnet ist.
        /// Prüft zunächst, ob die Verbindung nicht null und offen ist, bevor sie geschlossen wird.
        /// </summary>
        /// <remarks>
        /// Diese Methode ist sicher und wirft keine Exception, wenn die Verbindung bereits geschlossen oder null ist.
        /// </remarks>
        public void CloseConnection()
        {
            if (_connection?.State == System.Data.ConnectionState.Open)
                _connection.Close();
        }

        /// <summary>
        /// Gibt die Ressourcen (MySQL-Verbindung) frei.
        /// Sollte aufgerufen werden, wenn der DatabaseService nicht mehr benötigt wird.
        /// </summary>
        /// <remarks>
        /// Diese Methode implementiert das IDisposable-Interface.
        /// Am besten wird der DatabaseService in einem 'using'-Statement verwendet, um automatische Ressourcenfreigabe zu gewährleisten.
        /// </remarks>
        public void Dispose()
        {
            _connection.Dispose();
        }
    }
}