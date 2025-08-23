# Beispiel-Connection-String für MySQL
# mysql://username:password@host:port/database

class ConnectionStringBuilderLight:
    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        
    def build_connection_string(self):
        # MySQL-typischer Connection-String (URI-Format)
        self.conn_string = f"mysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        return self.conn_string
    
class ConnectionStringBuilder:
    def __init__(self, host, port, database, username, password):
        self._host = host
        self._port = port
        self._database = database
        self._username = username
        self._password = password

    # Getter und Setter für Host
    def get_host(self):
        return self._host

    def set_host(self, host):
        self._host = host

    # Getter und Setter für Port
    def get_port(self):
        return self._port

    def set_port(self, port):
        self._port = port

    # Getter und Setter für Datenbank
    def get_database(self):
        return self._database

    def set_database(self, database):
        self._database = database

    # Getter und Setter für Benutzername
    def get_username(self):
        return self._username

    def set_username(self, username):
        self._username = username

    # Getter und Setter für Passwort
    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    # Getter und Setter für alle Felder auf einmal
    def get_all(self):
        self.all_params = {
            "host": self._host,
            "port": self._port,
            "database": self._database,
            "username": self._username,
            "password": self._password
        }
        return self.all_params

    def set_all(self, host, port, database, username, password):
        self._host = host
        self._port = port
        self._database = database
        self._username = username
        self._password = password

    def build_connection_string(self):
        # MySQL-typischer Connection-String (URI-Format)
        self.conn_string = f"mysql://{self._username}:{self._password}@{self._host}:{self._port}/{self._database}"
        return self.conn_string