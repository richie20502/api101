# controllers/usuarios_controller.py
from db import get_db_connection

def obtener_usuarios():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT id, nombre, email FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
    connection.close()
    return usuarios

def agregar_usuario(nombre, email):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
        cursor.execute(sql, (nombre, email))
        connection.commit()
    connection.close()
    return "Usuario agregado correctamente"
