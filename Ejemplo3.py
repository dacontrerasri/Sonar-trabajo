import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/usuario")
def buscar_usuario():
    username = request.args.get("username")  # fuente no confiable

    conexion = sqlite3.connect("app.db")
    cursor = conexion.cursor()

    # El dato llega sin sanitizar a la consulta (regla S3649)
    query = "SELECT * FROM usuarios WHERE username = '" + username + "'"
    cursor.execute(query)

    return str(cursor.fetchall())