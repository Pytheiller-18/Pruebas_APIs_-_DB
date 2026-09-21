# Sistema POS - Módulo de Gestión de Usuarios

Sistema para la administración y registro de usuarios en un entorno de Punto de Venta (POS). Desarrollado bajo una arquitectura desacoplada con un backend en Python (Flask) conectado a MySQL y un frontend ligero en HTML5, CSS3 y JavaScript moderno.

---

## Características

- **Gestión de Usuarios**: Consulta y renderizado en tiempo real de los usuarios registrados en el sistema.
- **Registro Seguro**:
  - Validación de campos obligatorios en cliente y servidor.
  - Validación de formato de correo electrónico mediante expresiones regulares.
  - Encriptación de contraseñas utilizando hashing seguro (`werkzeug.security`).
  - Control de duplicados en base de datos para `identificacion`, `correo` y `usuario` mediante restricciones de unicidad.
- **Mapeo de Roles**: Asignación de roles de usuario (`cajero`, `administrador`).
- **Arquitectura Limpia**: Separación de responsabilidades mediante rutas modulares (`Blueprints`), capa de modelo (`models`) y capa de configuración (`config`).

---

## Estructura del Proyecto

```text
PROYECTO-POS/
├── backend/
│   ├── app.py                     # Punto de entrada de la aplicación Flask
│   ├── requirements.txt           # Dependencias del backend
│   ├── .env.example               # Plantilla de variables de entorno
│   ├── config/
│   │   ├── __init__.py
│   │   └── db.py                  # Conexión a la base de datos MySQL
│   ├── models/
│   │   ├── __init__.py
│   │   └── usuario_model.py       # Consultas y transacciones de usuarios
│   └── routes/
│       ├── __init__.py
│       └── usuarios_routes.py     # Endpoints y validaciones de la API
├── database/
│   └── usuarios.sql               # Script de creación de base de datos y tablas
├── frontend/
│   ├── index.html                 # Redirección de entrada
│   ├── usuarios.html              # Interfaz de gestión de usuarios
│   ├── css/
│   │   └── estilos.css            # Hoja de estilos de la interfaz
│   └── js/
│       └── usuarios.js            # Lógica de consumo de API y control del DOM
├── .gitignore                     # Exclusión de archivos para Git
└── README.md                      # Documentación del proyecto
```

---

## Requisitos Previos

- **Python**: Versión 3.10 o superior.
- **MySQL Server**: Versión 8.0 o compatible (MySQL Workbench o phpMyAdmin).
- **Navegador Web**: Cualquier navegador moderno con soporte para ES6+.

---

## Instalación y Configuración

### 1. Base de Datos

1. Abra su cliente de MySQL (MySQL Workbench, terminal o phpMyAdmin).
2. Ejecute el script ubicado en:
   ```text
   database/usuarios.sql
   ```
3. Esto creará la base de datos `bd_pos` y la tabla `usuarios` con los índices únicos correspondientes.

### 2. Configuración del Backend

1. Abra una terminal en la raíz del proyecto o en la carpeta `backend`.
2. (Opcional pero recomendado) Cree y active un entorno virtual:
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   ```
3. Instale las dependencias necesarias:
   ```bash
   pip install -r backend/requirements.txt
   ```
4. Si su usuario o contraseña de MySQL difiere de los valores por defecto (`root` / `123456`), configure las variables de entorno basándose en `backend/.env.example` o ajústelas en `backend/config/db.py`.

### 3. Ejecución del Servidor Backend

Inicie el servidor de Flask:

```bash
cd backend
python app.py
```

El servidor quedará disponible en: `http://127.0.0.1:5000`

---

## Uso del Frontend

Puede abrir directamente el archivo `frontend/usuarios.html` o `frontend/index.html` en su navegador web preferido, o servir la carpeta `frontend` mediante una extensión como **Live Server** en VS Code.

---

## Endpoints de la API

| Método | Endpoint | Descripción | Códigos HTTP |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/usuarios` | Obtiene el listado completo de usuarios registrados. | `200`, `500` |
| `POST` | `/api/usuarios` | Registra un nuevo usuario en la base de datos. | `201`, `400`, `409`, `500` |

### Formato de Solicitud para Registro (`POST /api/usuarios`):

```json
{
  "identificacion": "1234567890",
  "nombre": "Juan",
  "apellido": "Pérez",
  "correo": "juan.perez@example.com",
  "telefono": "3001234567",
  "usuario": "jperez",
  "password": "PasswordSeguro123",
  "rol": "cajero"
}
```

---

## Autor

Desarrollado por [Pytheiller-18](https://github.com/Pytheiller-18).
