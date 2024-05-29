import mysql.connector
from mysql.connector import Error
from db import Conexion
#import db

class Usuario:
    def __init__(self):
        self.db = Conexion()

    def agregar_usuario(self, nombre_usuario, contrasena, email):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "INSERT INTO usuario (NombreUsuario, Contrasena, Email) VALUES (%s, %s, %s)"
            val = (nombre_usuario, contrasena, email)
            cursor.execute(sql,val)
            conn.commit()
            return True
        except Error as e:
            print(f"Error al agregar usuario: {e}")
            return False


    def login(self, nombre_usuario, contrasena):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "SELECT IdUsuario FROM usuario WHERE NombreUsuario = %s AND Contrasena = %s"
            val = (nombre_usuario, contrasena)
            cursor.execute(sql, val)
            resultado = cursor.fetchone()
            if resultado:
                user_id = resultado[0]
                return True, user_id
            return False, None
        except Error as e:
            print(f"Error al verificar el usuario: {e}")
            return False, None


    def obtener_usuario_por_id(self, user_id):
        try:
            conn = self.db.get_connection()
            if conn is not None:
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT * FROM usuario WHERE IdUsuario = %s"
                cursor.execute(sql, (user_id,))
                resultado = cursor.fetchone()
                cursor.close()
                conn.close()
                return resultado if resultado else None
        except Error as e:
            print(f"Error al obtener usuario: {e}")
        return None


    def editar_usuario(self, id_usuario, nombre_usuario, contrasena, email):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "UPDATE usuario SET NombreUsuario = %s, Contrasena = %s, Email = %s WHERE IdUsuario = %s"
            val = (nombre_usuario, contrasena, email, id_usuario)
            cursor.execute(sql, val)
            conn.commit()
            return True
        except Error as e:
            print(f"Error al editar usuario: {e}")
            return False


    # ...
    # +CRUD