using DotNetEnv; // --> NuGet Paket installieren
using Npgsql; // --> NuGet Paket installieren
using System;
using System.Data;

namespace chsarp.services
{
    /// <summary>
    /// Service für die Verwaltung der PostgreSQL-Datenbankverbindung.
    /// Analoge API wie MySqlService.
    /// </summary>
    public class PostgresService : IDisposable
    {
        private readonly string _connectionString;
        private NpgsqlConnection _connection;

        public PostgresService()
        {
            var host = Env.GetString("PG_HOST");
            var port = Env.GetInt("PG_PORT");
            var database = Env.GetString("PG_DATABASE");
            var user = Env.GetString("PG_USER");
            var password = Env.GetString("PG_PASSWORD");

            if (string.IsNullOrEmpty(host) || string.IsNullOrEmpty(database) || string.IsNullOrEmpty(user) ||
                string.IsNullOrEmpty(password))
            {
                FileLogService.WriteToLog("PostgreSQL-Verbindungsdaten fehlen.");
                throw new Exception("PostgreSQL-Verbindungsdaten fehlen.");
            }

            var builder = new NpgsqlConnectionStringBuilder
            {
                Host = host,
                Port = port == 0 ? 5432U : Convert.ToUInt32(port),
                Database = database,
                Username = user,
                Password = password,
                SslMode = SslMode.Require, // Default: Require (wie bei MySQL-Beispiel)
                TrustServerCertificate = true // Falls Selbstsignierte Zertifikate verwendet werden
            };

            _connectionString = builder.ConnectionString;
        }

        public NpgsqlCommand CreateCommand() => _connection.CreateCommand();

        /// <summary>
        /// Öffnet die PostgreSQL-Verbindung.
        /// </summary>
        /// <returns>Die geöffnete NpgsqlConnection oder null bei Fehler.</returns>
        public NpgsqlConnection OpenConnection()
        {
            try
            {
                _connection = new NpgsqlConnection(_connectionString);
                _connection.Open();
                return _connection;
            }
            catch (Exception e)
            {
                FileLogService.WriteToLog($"{e}");
                return null;
            }
        }

        public void CloseConnection()
        {
            if (_connection?.State == ConnectionState.Open)
                _connection.Close();
        }

        public void Dispose()
        {
            _connection?.Dispose();
        }
    }

    public class PostgresTest
    {
        // PostgreSQL Service Test
        void PostgresServiceTest()
        {
            PostgresService dbService = new PostgresService();

            try
            {
                using (var connection = dbService.OpenConnection())
                {
                    // Beispiel: Tabelle erstellen
                    using (var dbCommand = connection.CreateCommand())
                    {
                        dbCommand.CommandText = @"
                                CREATE TABLE IF NOT EXISTS Test (
                                    Id SERIAL PRIMARY KEY,
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
                                    int id = reader.GetInt32(0);
                                    string name = reader.GetString(1);
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
                }
            }
            catch (Exception e)
            {
                FileLogService.WriteToLog($"{e}");
                throw;
            }
            finally
            {
                dbService.CloseConnection();
                dbService.Dispose();
            }
        }
    }
}

