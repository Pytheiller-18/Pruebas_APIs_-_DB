import os
from flask import Flask
from flask_cors import CORS
from routes.usuarios_routes import usuarios_bp

app = Flask(__name__)

# Configuración de CORS para habilitar solicitudes HTTP desde el frontend
CORS(app)

# Registro de rutas modulares de la aplicación
app.register_blueprint(usuarios_bp)

if __name__ == "__main__":
    puerto = int(os.getenv("PORT", 5000))
    print("Iniciando el servidor de API de Usuarios...")
    # Modo debug habilitado para recarga automática durante desarrollo
    app.run(port=puerto, debug=True)
