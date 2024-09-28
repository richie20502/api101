from db  import get_db_connection

def obtener_usuario():
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql ="SELECT id, nombre, email FROM usuarios"
        cursor.execute(sql)
        usuarios = cursor.fetchall()
    connection.close()
    return usuarios