namespace CSharp;

public class DbLogger
{
    public DbLogger(string logTableName = "error")
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
            }
        }
        catch (Exception e)
        {
            
            dbErrorLog.WriteToLog($"{e}");
        }
    }
    
    
    
}