from config.db import obtener_conexion

def listar_usuarios():
    conn = obtener_conexion()
    # Retorna los registros en formato diccionario (clave-valor)
    cur = conn.cursor(dictionary=True) 
    cur.execute("SELECT id, identificacion, nombre, apellido, correo, telefono, usuario, rol FROM usuarios")
    filas = cur.fetchall()
    
    cur.close()
    conn.close()
    return filas

def crear_usuario(datos, password_hash):
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
        datos.get("rol", "cajero") # Rol asignado o valor por defecto 'cajero'
    )
    
    cur.execute(consulta, valores)
    conn.commit() # Confirmación de la transacción en la base de datos
    
    cur.close()
    conn.close()