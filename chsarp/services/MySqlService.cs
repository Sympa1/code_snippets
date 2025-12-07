using DotNetEnv; // --> NuGet Paket installieren
using MySql.Data.MySqlClient; // --> NuGet Paket installieren

namespace chsarp.services
{
    /// <summary>
    /// Service für die Verwaltung der MySQL-Datenbankverbindung.
    /// Verwaltet den Lebenszyklus der Verbindung und stellt Methoden zum Öffnen und Schließen bereit.
    /// Implementiert IDisposable für eine ordnungsgemäße Ressourcenfreigabe.
    /// </summary>
    public class MySqlService : IDisposable
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
        public MySqlService()
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

    public class MySqlTest
    {
        // MySQLService Test
        void MySQLServiceTest()
        {
            MySqlService dbServiceMySQL = new MySqlService();

            try
            {
                using (var connection = dbServiceMySQL.OpenConnection())
                {
                    // Beispiel: Tabelle erstellen
                    using (var dbCommand = connection.CreateCommand())
                    {
                        dbCommand.CommandText = @"
                                CREATE TABLE IF NOT EXISTS Test (
                                    Id INT AUTO_INCREMENT PRIMARY KEY,
                                    Name VARCHAR(100) NOT NULL
                                )";
                        try
                        {
                            dbCommand.ExecuteNonQuery();
                        }
                        catch (Exception e)
                        {
                            FileLogService.WriteToLog($"{e}");
                            throw;
                        }
                    }

                    // Beispiel: Datensatz einfügen
                    using (var dbCommand = connection.CreateCommand())
                    {
                        dbCommand.CommandText = @"INSERT INTO Test (Name) VALUES (@name)";
                        dbCommand.Parameters.AddWithValue("@name", "John Doe");
                        try
                        {
                            dbCommand.ExecuteNonQuery();
                        }
                        catch (Exception e)
                        {
                            FileLogService.WriteToLog($"{e}");
                            throw;
                        }
                    }

                    // Beispiel: Anzahl Datensätze zählen
                    using (var dbCommand = connection.CreateCommand())
                    {
                        dbCommand.CommandText = @"SELECT COUNT(*) FROM Test";
                        try
                        {
                            object result = dbCommand.ExecuteScalar();
                            long count = Convert.ToInt64(result);
                            Console.WriteLine($"Es gibt {count} Benutzer.");
                        }
                        catch (Exception e)
                        {
                            FileLogService.WriteToLog($"{e}");
                            throw;
                        }
                    }

                    // Beispiel: Alle Datensätze auslesen
                    using (var dbCommand = connection.CreateCommand())
                    {
                        dbCommand.CommandText = @"SELECT Id, Name FROM Test";
                        try
                        {
                            using (var reader = dbCommand.ExecuteReader())
                            {
                                while (reader.Read())
                                {
                                    int id = reader.GetInt32(0); // Spalte 0 = Id
                                    string name = reader.GetString(1); // Spalte 1 = Name
                                    Console.WriteLine($"Id={id}, Name={name}");
                                }
                            }
                        }
                        catch (Exception e)
                        {
                            FileLogService.WriteToLog($"{e}");
                            throw;
                        }
                    }

                    // Beispiel: Einen bestimmten Datensatz auslesen
                    int searchId = 1;

                    using (var dbCommand = connection.CreateCommand())
                    {
                        dbCommand.CommandText = @"SELECT Id, Name FROM Test WHERE Id = @id";
                        dbCommand.Parameters.AddWithValue("@id", searchId);
                        try
                        {
                            using (var reader = dbCommand.ExecuteReader())
                            {
                                if (reader.Read())
                                {
                                    int id = reader.GetInt32(0);
                                    string name = reader.GetString(1);
                                    Console.WriteLine($"Gefundener Datensatz -> Id={id}, Name={name}");
                                }
                                else
                                {
                                    Console.WriteLine($"Kein Datensatz mit Id={searchId} gefunden.");
                                }
                            }
                        }
                        catch (Exception e)
                        {
                            FileLogService.WriteToLog($"{e}");
                            throw;
                        }
                    }
                }
            }
            catch (Exception e)
            {
                FileLogService.WriteToLog($"{e}");
                throw;
            }
            finally
            {
                dbServiceMySQL.CloseConnection();
                dbServiceMySQL.Dispose(); // Ressourcen freigeben?
            }
        }
    }
}