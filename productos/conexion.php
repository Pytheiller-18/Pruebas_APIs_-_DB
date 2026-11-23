<?php
$host = "localhost";
$db_name = "api_crud";
$username = "root"; // Tu usuario de MySQL
$password = "";     // Tu contraseña de MySQL

try {
    $conexion = new PDO("mysql:host=" . $host . ";dbname=" . $db_name, $username, $password);
    $conexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $conexion->exec("set names utf8");
} catch(PDOException $exception) {
    echo json_encode(["error" => "Error de conexión: " . $exception->getMessage()]);
    exit;
}
?>
