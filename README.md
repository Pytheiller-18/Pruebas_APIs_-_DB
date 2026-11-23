# Repositorio de Pruebas de APIs y Bases de Datos

Colección de módulos independientes para prácticas y pruebas de APIs REST y bases de datos MySQL / MariaDB.

## Estructura del Repositorio

```text
API/
├── productos/               # API REST CRUD en PHP + cliente Python + Postman
│   ├── api_crud.sql         # BD: api_crud (tabla productos)
│   ├── conexion.php         # Conexión PDO a MySQL
│   ├── productos.php        # Endpoints GET, POST, PUT, DELETE
│   ├── main.py              # Cliente de consola en Python
│   └── postman.docx         # Guía de pruebas en Postman
├── gestion_motocicletas/    # Base de datos para gestión de motocicletas
│   └── motocicletas.sql     # BD: gestion_motocicletas (tabla motocicletas)
└── usuarios/                # API REST en Flask + frontend HTML/CSS/JS
    ├── backend/
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── .env.example
    │   ├── config/db.py
    │   ├── models/usuario_model.py
    │   └── routes/usuarios_routes.py
    ├── database/
    │   └── usuarios.sql     # BD: gestion_usuarios (tabla usuarios)
    └── frontend/
        ├── index.html
        ├── usuarios.html
        ├── css/estilos.css
        └── js/usuarios.js
```

## Módulos

### 1. `productos/` (PHP + MySQL + Python)
1. Importa `productos/api_crud.sql` en MySQL / phpMyAdmin (crea la tabla `productos` dentro de `api_crud`).
2. Sirve la carpeta en Apache/XAMPP (`http://localhost/API/productos/productos.php`).
3. Ejecuta el cliente de prueba:
   ```bash
   python productos/main.py
   ```

### 2. `gestion_motocicletas/` (SQL)
1. Importa `gestion_motocicletas/motocicletas.sql` en MySQL / phpMyAdmin.
2. El script crea automáticamente la base de datos `gestion_motocicletas`, la tabla `motocicletas` y sus datos iniciales.

### 3. `usuarios/` (Flask + MySQL + Frontend)
1. Ejecuta `usuarios/database/usuarios.sql` en MySQL / phpMyAdmin para crear la base de datos `gestion_usuarios` y la tabla `usuarios`.
2. Instala las dependencias del backend:
   ```bash
   pip install -r usuarios/backend/requirements.txt
   ```
3. Configura variables de entorno si tus credenciales difieren de `root` / `123456` (usa `usuarios/backend/.env.example` como guía).
4. Inicia el servidor Flask:
   ```bash
   cd usuarios/backend
   python app.py
   ```
5. Abre `usuarios/frontend/usuarios.html` o `usuarios/frontend/index.html` en tu navegador.

#### Endpoints disponibles (`usuarios`)
| Método | Endpoint | Descripción | Códigos HTTP |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/usuarios` | Lista todos los usuarios registrados | `200`, `500` |
| `POST` | `/api/usuarios` | Registra un nuevo usuario (`usuario` o `administrador`) | `201`, `400`, `409`, `500` |
