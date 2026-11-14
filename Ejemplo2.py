import sqlite3

def buscar_usuario(db_path, username_input):
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()

    query = "SELECT * FROM usuarios WHERE username = '" + username_input + "'"

    cursor.execute(query)
    return cursor.fetchall()