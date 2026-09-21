import re
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from mysql.connector import IntegrityError
from models import usuario_model

# Definición del Blueprint para modularizar las rutas de usuarios
usuarios_bp = Blueprint("usuarios", __name__)

# Definición de campos obligatorios para el registro
CAMPOS = ["identificacion", "nombre", "apellido", "correo", "telefono", "usuario", "password"]

# Endpoint para listar todos los usuarios registrados
@usuarios_bp.route("/api/usuarios", methods=["GET"])
def get_usuarios():
    try:
        usuarios = usuario_model.listar_usuarios()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error al consultar usuarios: {str(e)}"}), 500

# Endpoint para registrar un nuevo usuario
@usuarios_bp.route("/api/usuarios", methods=["POST"])
def post_usuario():
    datos = request.get_json(silent=True) or {}
    
    # Validación de campos requeridos y no vacíos
    faltan = [c for c in CAMPOS if not str(datos.get(c, "")).strip()]
    if faltan:
        return jsonify({"success": False, "message": f"Campos obligatorios faltantes: {', '.join(faltan)}"}), 400
    
    # Validación de formato de correo electrónico mediante expresión regular
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", datos["correo"]):
        return jsonify({"success": False, "message": "El correo ingresado es inválido."}), 400
        
    try:
        # Generación de hash seguro para la contraseña
        password_hash = generate_password_hash(datos["password"])
        
        # Inserción del nuevo usuario mediante la capa del modelo
        usuario_model.crear_usuario(datos, password_hash)
        
        return jsonify({"success": True, "message": "Usuario registrado correctamente"}), 201
        
    except IntegrityError as e:
        # Manejo de conflictos de unicidad en la base de datos (identificación, correo o usuario duplicados)
        error_msg = str(e).lower()
        campo = "identificación" if "identificacion" in error_msg else "correo" if "correo" in error_msg else "usuario"
        return jsonify({"success": False, "message": f"Ya existe un registro con este {campo}."}), 409
        
    except Exception as e:
        return jsonify({"success": False, "message": f"Error interno del servidor: {str(e)}"}), 500

    