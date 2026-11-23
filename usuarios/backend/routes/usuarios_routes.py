import re
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from mysql.connector import IntegrityError
from models import usuario_model

# Definición del Blueprint para modularizar las rutas de usuarios
usuarios_bp = Blueprint("usuarios", __name__)

# Definición de campos obligatorios y roles permitidos para el registro
CAMPOS = ["identificacion", "nombre", "apellido", "correo", "telefono", "usuario", "password"]
ROLES_PERMITIDOS = {"usuario", "administrador"}


@usuarios_bp.route("/api/usuarios", methods=["GET"])
def get_usuarios():
    """Endpoint para listar todos los usuarios registrados."""
    try:
        usuarios = usuario_model.listar_usuarios()
        return jsonify(usuarios), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error al consultar usuarios: {str(e)}"}), 500


@usuarios_bp.route("/api/usuarios", methods=["POST"])
def post_usuario():
    """Endpoint para registrar un nuevo usuario."""
    datos = request.get_json(silent=True) or {}

    # Validación de campos requeridos y no vacíos
    faltan = [c for c in CAMPOS if not str(datos.get(c, "")).strip()]
    if faltan:
        return jsonify({"success": False, "message": f"Campos obligatorios faltantes: {', '.join(faltan)}"}), 400

    correo = str(datos["correo"]).strip()
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", correo):
        return jsonify({"success": False, "message": "El correo ingresado es inválido."}), 400

    rol = str(datos.get("rol") or "usuario").strip().lower()
    if rol not in ROLES_PERMITIDOS:
        return jsonify({"success": False, "message": "Rol inválido. Valores permitidos: usuario, administrador."}), 400

    datos_limpios = {
        "identificacion": str(datos["identificacion"]).strip(),
        "nombre": str(datos["nombre"]).strip(),
        "apellido": str(datos["apellido"]).strip(),
        "correo": correo,
        "telefono": str(datos["telefono"]).strip(),
        "usuario": str(datos["usuario"]).strip(),
        "rol": rol,
    }

    try:
        password_hash = generate_password_hash(str(datos["password"]))
        usuario_model.crear_usuario(datos_limpios, password_hash)
        return jsonify({"success": True, "message": "Usuario registrado correctamente"}), 201

    except IntegrityError as e:
        error_msg = str(e).lower()
        campo = "identificación" if "identificacion" in error_msg else "correo" if "correo" in error_msg else "usuario"
        return jsonify({"success": False, "message": f"Ya existe un registro con este {campo}."}), 409

    except Exception as e:
        return jsonify({"success": False, "message": f"Error interno del servidor: {str(e)}"}), 500
