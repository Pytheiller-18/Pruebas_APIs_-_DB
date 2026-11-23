<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: GET, POST, PUT, DELETE");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");

include_once 'conexion.php';

$metodo = $_SERVER['REQUEST_METHOD'];

switch ($metodo) {
    // ----------------------------------------------------
    // LEER (GET) - Obtener uno o todos los productos
    // ----------------------------------------------------
    case 'GET':
        if (isset($_GET['id'])) {
            $query = "SELECT * FROM productos WHERE id = :id LIMIT 1";
            $stmt = $conexion->prepare($query);
            $stmt->bindParam(':id', $_GET['id']);
        } else {
            $query = "SELECT * FROM productos";
            $stmt = $conexion->prepare($query);
        }
        
        $stmt->execute();
        $resultado = $stmt->fetchAll(PDO::FETCH_ASSOC);
        echo json_encode($resultado);
        break;

    // ----------------------------------------------------
    // CREAR (POST) - Insertar un nuevo producto
    // ----------------------------------------------------
    case 'POST':
        $data = json_decode(file_get_contents("php://input"), true);
        
        if (!empty($data['nombre']) && !empty($data['precio'])) {
            $query = "INSERT INTO productos (nombre, precio) VALUES (:nombre, :precio)";
            $stmt = $conexion->prepare($query);
            
            $stmt->bindParam(':nombre', $data['nombre']);
            $stmt->bindParam(':precio', $data['precio']);
            
            if ($stmt->execute()) {
                http_response_code(201);
                echo json_encode(["mensaje" => "Producto creado con éxito."]);
            } else {
                http_response_code(500);
                echo json_encode(["mensaje" => "No se pudo crear el producto."]);
            }
        } else {
            http_response_code(400);
            echo json_encode(["mensaje" => "Datos incompletos."]);
        }
        break;

    // ----------------------------------------------------
    // ACTUALIZAR (PUT) - Modificar un producto existente
    // ----------------------------------------------------
    case 'PUT':
        $data = json_decode(file_get_contents("php://input"), true);
        
        if (!empty($data['id']) && !empty($data['nombre']) && !empty($data['precio'])) {
            $query = "UPDATE productos SET nombre = :nombre, precio = :precio WHERE id = :id";
            $stmt = $conexion->prepare($query);
            
            $stmt->bindParam(':id', $data['id']);
            $stmt->bindParam(':nombre', $data['nombre']);
            $stmt->bindParam(':precio', $data['precio']);
            
            if ($stmt->execute()) {
                echo json_encode(["mensaje" => "Producto actualizado con éxito."]);
            } else {
                http_response_code(500);
                echo json_encode(["mensaje" => "No se pudo actualizar el producto."]);
            }
        } else {
            http_response_code(400);
            echo json_encode(["mensaje" => "Datos incompletos para actualizar."]);
        }
        break;

    // ----------------------------------------------------
    // ELIMINAR (DELETE) - Borrar un producto
    // ----------------------------------------------------
    case 'DELETE':
        if (isset($_GET['id'])) {
            $query = "DELETE FROM productos WHERE id = :id";
            $stmt = $conexion->prepare($query);
            $stmt->bindParam(':id', $_GET['id']);
            
            if ($stmt->execute()) {
                echo json_encode(["mensaje" => "Producto eliminado con éxito."]);
            } else {
                http_response_code(500);
                echo json_encode(["mensaje" => "No se pudo eliminar el producto."]);
            }
        } else {
            http_response_code(400);
            echo json_encode(["mensaje" => "ID no proporcionado."]);
        }
        break;

    default:
        http_response_code(405);
        echo json_encode(["mensaje" => "Método no permitido."]);
        break;
}
?>
