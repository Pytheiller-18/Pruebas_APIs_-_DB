-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-11-2026 a las 22:29:47
-- Versión del servidor: 10.11.16-MariaDB
-- Versión de PHP: 8.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gestion_motocicletas`
--
CREATE DATABASE IF NOT EXISTS `gestion_motocicletas`
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE `gestion_motocicletas`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `motocicletas`
--

CREATE TABLE `motocicletas` (
  `id_motocicleta` int(11) NOT NULL,
  `marca` varchar(60) NOT NULL,
  `modelo` varchar(80) NOT NULL,
  `anio` year(4) NOT NULL,
  `cilindraje` int(11) NOT NULL,
  `precio` decimal(12,2) NOT NULL,
  `stock` int(11) NOT NULL DEFAULT 0,
  `estado` enum('Disponible','Agotada','Inactiva') NOT NULL DEFAULT 'Disponible',
  `fecha_registro` timestamp NULL DEFAULT current_timestamp()
) ;

--
-- Volcado de datos para la tabla `motocicletas`
--

INSERT INTO `motocicletas` (`id_motocicleta`, `marca`, `modelo`, `anio`, `cilindraje`, `precio`, `stock`, `estado`, `fecha_registro`) VALUES
(1, 'Yamaha', 'FZ 2.0', '2024', 150, 10500000.00, 5, 'Disponible', '2026-10-26 16:50:48'),
(2, 'Bajaj', 'Pulsar NS200', '2025', 200, 12500000.00, 3, 'Disponible', '2026-10-26 16:50:48'),
(3, 'Honda', 'CB125F', '2023', 125, 8200000.00, 0, 'Agotada', '2026-10-26 16:50:48'),
(4, 'Suzuki', 'Gixxer 150', '2024', 150, 9900000.00, 2, 'Disponible', '2026-10-26 16:50:48'),
(5, 'AKT', 'NKD 125', '2022', 125, 5800000.00, 1, 'Inactiva', '2026-10-26 16:50:48'),
(7, 'KTM', 'MotoSOAPActualizada', '2025', 250, 9500000.00, 5, 'Disponible', '2026-10-26 19:07:44'),
(8, 'AKT', '2026', '2026', 5, 20000000.00, 4, 'Disponible', '2026-10-26 19:36:11'),
(9, 'SUZUKI', '2026', '2025', 6, 10000000.00, 5, 'Agotada', '2026-10-26 19:36:54'),
(10, 'Yamaha', 'h', '2025', 155, 900000000.00, 7, 'Disponible', '2026-10-26 19:43:54'),
(12, 'Kawasaki', 'Z400', '2025', 399, 28500000.00, 2, 'Disponible', '2026-11-09 15:46:42'),
(13, 'Kawasaki', 'Z400', '2025', 399, 28500000.00, 2, 'Disponible', '2026-11-09 15:55:24');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `motocicletas`
--
ALTER TABLE `motocicletas`
  ADD PRIMARY KEY (`id_motocicleta`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `motocicletas`
--
ALTER TABLE `motocicletas`
  MODIFY `id_motocicleta` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
