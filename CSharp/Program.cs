using CSharp;
using DotNetEnv; // --> NuGet-Paket

# region notes
// Das @ vor dem String macht den C#-String zu einem "verbatim string", d.h. Backslashes müssen nicht escaped werden
// und der String kann über mehrere Zeilen gehen. So lassen sich lange SQL-Statements sauber und lesbar schreiben.

// In C#, ist ein Interface ein "Vertrag" oder eine Blaupause, die die Definitionen von Methoden, Eigenschaften und
// Ereignissen enthält, aber keine Implementierung
# endregion

// Test Log
void TestLog()
{
    FileLogger testLog = new FileLogger();
    testLog.WriteToLog("Test");
}

// SQLiteService Test
void SQLiteServiceTest()
{
    FileLogger dbErrorLog = new FileLogger();
    SQLiteService dbServiceSQLite = new SQLiteService();
    try
    {
        using (var dbConnection = dbServiceSQLite.OpenConnection())
        {
            // Create Table
            using (var dbCommand = dbConnection.CreateCommand())
            {
                dbCommand.CommandText = @"CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                                            name TEXT NOT NULL)";
                try
                {
                    dbCommand.ExecuteNonQuery();
                }
                catch (Exception e)
                {
                    dbErrorLog.WriteToLog($"{e}");
                    throw;
                }
            }

            // Insert
            using (var dbCommand = dbConnection.CreateCommand())
            {
                dbCommand.CommandText = @"INSERT INTO test (name) VALUES (@name)";
                dbCommand.Parameters.AddWithValue("@name", "Test");
                try
                {
                    dbCommand.ExecuteNonQuery();
                }
                catch (Exception e)
                {
                    dbErrorLog.WriteToLog($"{e}");
                    throw;
                }
            }

            // Select
            using (var command = dbConnection.CreateCommand())
            {
                command.CommandText = "SELECT * FROM test";
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        Console.WriteLine(reader.GetString(1));
                    }
                }
            }

            // Zählt
            using (var command = dbConnection.CreateCommand())
            {
                command.CommandText = "SELECT COUNT(*) FROM test";
                try
                {
                    var count = command.ExecuteScalar();
                    Console.WriteLine(count);
                }
                catch (Exception e)
                {
                    dbErrorLog.WriteToLog($"{e}");
                }
            }
        }
    }
    catch (Exception e)
    {
        dbErrorLog.WriteToLog($"{e}");
        throw; // Was macht diese Zeile?
    }
    finally
    {
        dbServiceSQLite.CloseConnection();
        dbServiceSQLite.Dispose(); // Ressourcen freigeben
    }
}


// MySQLService Test
void MySQLServiceTest()
{
    FileLogger dbErrorLog = new FileLogger();
    MySQLService dbServiceMySQL = new MySQLService();

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
                    dbErrorLog.WriteToLog($"{e}");
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
                    dbErrorLog.WriteToLog($"{e}");
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
                    dbErrorLog.WriteToLog($"{e}");
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
                    dbErrorLog.WriteToLog($"{e}");
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
                    dbErrorLog.WriteToLog($"{e}");
                    throw;
                }
            }
        }
    }
    catch (Exception e)
    {
        dbErrorLog.WriteToLog($"{e}");
        throw;
    }
    finally
    {
        dbServiceMySQL.CloseConnection();
        dbServiceMySQL.Dispose(); // Ressourcen freigeben?
    }
}

//TestLog();
//SQLiteServiceTest();
//EnvLoader.LoadDotEnv();
//MySQLServiceTest();