from config.db import obtener_conexion


def listar_usuarios():
    """Consulta y retorna los usuarios registrados como diccionarios."""
    conn = obtener_conexion()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        "SELECT id, identificacion, nombre, apellido, correo, telefono, usuario, rol FROM usuarios"
    )
    filas = cur.fetchall()

    cur.close()
    conn.close()
    return filas


def crear_usuario(datos, password_hash):
    """Inserta un nuevo usuario en la base de datos."""
    conn = obtener_conexion()
    cur = conn.cursor()

    # Consulta parametrizada para prevenir inyecciones SQL
    consulta = """
        INSERT INTO usuarios
        (identificacion, nombre, apellido, correo, telefono, usuario, password, rol)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (
        datos["identificacion"],
        datos["nombre"],
        datos["apellido"],
        datos["correo"],
        datos["telefono"],
        datos["usuario"],
        password_hash,
        datos.get("rol", "usuario"),
    )

    cur.execute(consulta, valores)
    conn.commit()

    cur.close()
    conn.close()
