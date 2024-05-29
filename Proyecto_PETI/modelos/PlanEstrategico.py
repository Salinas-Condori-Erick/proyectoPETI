import mysql.connector
from mysql.connector import Error
from db import Conexion

class PlanEstrategico:
    def __init__(self):
        self.db = Conexion()

    def agregar_plan(self, nombre, empresa, mision, vision, fkidusuario):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "INSERT INTO plan_estrategico (Nombre, Empresa, Mision, Vision, FKIdUsuario) VALUES (%s, %s, %s, %s, %s)"
            val = (nombre, empresa, mision, vision, fkidusuario)
            cursor.execute(sql, val)
            conn.commit()
            return True
        except Error as e:
            print(f"Error al agregar plan estratégico: {e}")
            return False

    def obtener_plan_por_id(self, id_plan):
        try:
            #Error por recibir de valor una tupla
            #print("ID Plan antes de convertir:", id_plan, type(id_plan))
            if isinstance(id_plan, tuple):
                id_plan = int(id_plan[0])
            else:
                id_plan = int(id_plan)

            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM plan_estrategico WHERE IdPlanEstrategico = %s"
            cursor.execute(sql, (id_plan,))
            resultado = cursor.fetchone()
            return resultado if resultado else None
        except Error as e:
            print(f"Error al obtener misión: {e}")
            return None

    def actualizar_plan(self, id_plan, nombre, empresa, mision, vision):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = """
            UPDATE plan_estrategico SET Nombre = %s, Empresa = %s, Mision = %s, Vision = %s WHERE IdPlanEstrategico = %s
            """
            cursor.execute(sql, (nombre, empresa, mision, vision, id_plan))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al actualizar el plan: {e}")
            return False


    def listar_planes_por_id_usuario(self, user_id):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "SELECT * FROM plan_estrategico WHERE FKIdUsuario = %s"
            cursor.execute(sql, (user_id,))
            resultado = cursor.fetchall()
            return resultado
        except Error as e:
            print(f"Error al listar planes: {e}")
            return []


    def eliminar_plan(self, id_plan):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "DELETE FROM plan_estrategico WHERE IdPlanEstrategico = %s"
            cursor.execute(sql, (id_plan,))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al eliminar plan: {e}")
            return False


# Mision y Vision
    def actualizar_mision(self, id_plan, nueva_mision):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "UPDATE plan_estrategico SET Mision = %s WHERE IdPlanEstrategico = %s"
            cursor.execute(sql, (nueva_mision, id_plan))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al actualizar misión: {e}")
            return False

    def actualizar_vision(self, id_plan, nueva_vision):
        try:
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "UPDATE plan_estrategico SET Vision = %s WHERE IdPlanEstrategico = %s"
            cursor.execute(sql, (nueva_vision, id_plan))
            conn.commit()
            return True
        except Error as e:
            print(f"Error al actualizar visión: {e}")
            return False


# Valores

    def obtener_valores_por_plan_id(self, plan_id):
            try:

                if isinstance(plan_id, tuple):
                    plan_id = int(plan_id[0])
                else:
                    plan_id = int(plan_id)

                conn = self.db.get_connection()
                cursor = conn.cursor(dictionary=True)
                sql = "SELECT * FROM valor WHERE FKIdPlanEstrategico = %s"
                cursor.execute(sql, (plan_id,))
                valores = cursor.fetchall()
                cursor.close()
                conn.close()
                return valores
            except Exception as e:
                print(f"Error al obtener los valores del plan: {e}")
                return []


    # ...
    # +CRUD