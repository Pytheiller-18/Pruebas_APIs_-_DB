import requests

# Configura la URL base de tu API local
BASE_URL = "http://localhost/API/productos/productos.php"

def mostrar_respuesta(respuesta):
    """Muestra el código de estado y el JSON de forma limpia."""
    print("\n" + "="*40)
    print(f"Código de Estado HTTP: {respuesta.status_code}")
    try:
        import json
        print(json.dumps(respuesta.json(), indent=4, ensure_ascii=False))
    except ValueError:
        print("Respuesta Texto:", respuesta.text)
    print("="*40 + "\n")

def menu():
    while True:
        print("--- MENÚ CRUD API ---")
        print("1. Ver todos los productos (GET)")
        print("2. Ver un producto por ID (GET)")
        print("3. Crear un nuevo producto (POST)")
        print("4. Actualizar un producto (PUT)")
        print("5. Eliminar un producto (DELETE)")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        # Estructura estructural match-case (Python 3.10+)
        match opcion:
            case "1":
                print("\n📋 Obteniendo todos los productos...")
                response = requests.get(BASE_URL)
                mostrar_respuesta(response)
                
            case "2":
                id_prod = input("Introduce el ID del producto que buscas: ")
                print(f"\n🔍 Buscando producto con ID {id_prod}...")
                response = requests.get(BASE_URL, params={"id": id_prod})
                mostrar_respuesta(response)
                
            case "3":
                print("\n➕ Agregar Nuevo Producto")
                nombre = input("Nombre del producto: ")
                precio = input("Precio del producto: ")
                
                nuevo_producto = {"nombre": nombre, "precio": float(precio)}
                response = requests.post(BASE_URL, json=nuevo_producto)
                mostrar_respuesta(response)
                
            case "4":
                id_prod = input("Introduce el ID del producto a actualizar: ")
                print("\n🔄 Introduce los nuevos datos:")
                nombre = input("Nuevo nombre: ")
                precio = input("Nuevo precio: ")
                
                producto_actualizado = {"id": int(id_prod), "nombre": nombre, "precio": float(precio)}
                response = requests.put(BASE_URL, json=producto_actualizado)
                mostrar_respuesta(response)
                
            case "5":
                id_prod = input("Introduce el ID del producto a eliminar: ")
                confirmar = input(f"¿Estás seguro de eliminar el ID {id_prod}? (s/n): ").lower()
                
                if confirmar == 's':
                    print(f"\n❌ Eliminando producto con ID {id_prod}...")
                    response = requests.delete(BASE_URL, params={"id": id_prod})
                    mostrar_respuesta(response)
                else:
                    print("\nOperación cancelada.\n")
                    
            case "6":
                print("\n¡Hasta luego!")
                break
                
            case _:
                print("\n⚠️ Opción inválida. Elige un número del 1 al 6.\n")

if __name__ == "__main__":
    menu()
