import mysql.connector
from mysql.connector import Error

class Conexion:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Conexion, cls).__new__(cls)
        if not hasattr(cls._instance, 'connection') or not cls._instance.connection.is_connected():
            cls._setup_connection()
        return cls._instance

    @staticmethod
    def _setup_connection():
        host = 'localhost'
        user = 'root'
        password = ''
        database = 'dbplanestrategico'
        try:
            Conexion._instance.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Conexion a la base de datos establecida")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            raise ConnectionError("Failed to connect to the database.")

    def get_connection(self):
        if self.connection.is_connected():
            return self.connection
        else:
            self._setup_connection()
            return self.connection

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexion a la base de datos cerrada")
