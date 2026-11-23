-- =======================================================
-- Script de Base de Datos - Módulo de Gestión de Usuarios
-- =======================================================

-- Creación de la base de datos si no existe
CREATE DATABASE IF NOT EXISTS gestion_usuarios
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE gestion_usuarios;

-- Creación de la tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    identificacion VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol ENUM('usuario', 'administrador') NOT NULL DEFAULT 'usuario',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
