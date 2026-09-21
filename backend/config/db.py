import os
import mysql.connector

def obtener_conexion():
    # Establece y retorna la conexión a la base de datos MySQL
    # Permite configuración mediante variables de entorno o valores predeterminados
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "123456"), 
        database=os.getenv("DB_NAME", "bd_pos"),
    )
