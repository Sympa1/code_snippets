using System;
using System.Collections.Generic;
using System.Data;
using Microsoft.Data.Sqlite;  // --> NuGet-Paket

namespace CSharp;

/// <summary>
/// Diese Klasse dient zum Verwalten einer SQLite-Datenbank.
/// </summary>
public class SQLiteService : IDisposable
{
    private readonly string _connectionString;
    private SqliteConnection? _connection;  // --> Das "?" macht die Variable "nullable", sie kann null sein
    
    /// <summary>
    /// Konsturktor-Methode, die den Pfad zum Datenbank-File als Parameter entgegennimmt.
    /// </summary>
    /// <param name="connectionString"></param>
    public SQLiteService(string connectionString = "test.db") // Platziert das Logfile im Stammverzeichnis des Projekts ../bin/Debug/netX.X/
    {
        this._connectionString = $"Data Source={connectionString}";
    }

    /// <summary>
    /// Öffnet die Datenbankverbindung.
    /// </summary>
    public SqliteConnection OpenConnection()
    {
        // Neue SQLite-Verbindung mit dem gespeicherten Connection String erstellen & anschließend öffnen
        _connection = new SqliteConnection(_connectionString);
        _connection.Open();
        return _connection;
    }
    
    /// <summary>
    /// Schließt die Datenbankverbindung.
    /// </summary>
    public void CloseConnection()
    {
        _connection.Close();
    }
    
    /// <summary>
    /// Gibt die Ressourcen (Connection) frei.
    /// </summary>
    public void Dispose()
    {
        _connection?.Dispose();
    }
}
