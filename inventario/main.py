from scripts.producto import Producto
from scripts.inventario import Inventario, pedir_numero_positivo

def mostrar_menu():
    print("\n" + "="*40)
    print("<-- SISTEMA DE GESTIÓN DE INVENTARIO -->")
    print("="*40)
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto(s) por ID, nombre o categoría")
    print("5. Calcular valor total del inventario")
    print("6. Consulta general de productos")
    print("7. Guardar inventario en archivo")
    print("8. Bajo stock de productos")
    print("9. Salir")
    print("="*40)

def main():
    mi_inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-9): ").strip()

        # 1. Agregar producto
        if opcion == "1":
            print("\n<--- AGREGAR NUEVO PRODUCTO --->")
            id = input("ID del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            categoria = input("Categoría: ").strip()
            
            # valores no negativos
            precio = pedir_numero_positivo("Precio ($): ", es_entero=False)
            peso = pedir_numero_positivo("Peso (kg): ", es_entero=False)
            cantidad = pedir_numero_positivo("Cantidad en stock: ", es_entero=True)

            try:
                nuevo_prod = Producto(id, nombre, categoria, precio, peso, int(cantidad))
                mi_inventario.agregar_producto(nuevo_prod)
            except ValueError as e:
                print(f" Error: {e}")

        # 2. Eliminar producto
        elif opcion == "2":
            print("\n<--- ELIMINAR PRODUCTO --->")
            id = input("Ingresa el ID del producto a eliminar: ").strip()
            mi_inventario.eliminar_producto(id)

        # 3. Actualizar producto
        elif opcion == "3":
            print("\n<--- ACTUALIZAR PRODUCTO --->")
            id = input("Ingresa el ID del producto a actualizar: ").strip()
            
            # Verificamos si existe antes de pedir datos
            coincidencias = mi_inventario.buscar_producto(id)
            if not coincidencias:
                print(f"No se encontró el producto con ID '{id}'.")
                continue

            print("Ingresa los nuevos valores:")

            # actualizar nombre
            inp_nombre = input("Nuevo nombre: ").strip()
            nuevo_nombre = str(inp_nombre) if inp_nombre else None

            # actualizar categoria
            inp_categoria = input("Nueva categoría: ").strip()
            nueva_categoria = str(inp_categoria) if inp_categoria else None

            # actualizar precio
            inp_precio = input("Nuevo precio ($): ").strip()
            nuevo_precio = float(inp_precio) if inp_precio else None

            # actualizar peso
            inp_peso = input("Nuevo peso (kg): ").strip()
            nuevo_peso = float(inp_peso) if inp_peso else None

            # actualizar cantidad
            inp_cantidad = input("Nueva cantidad en stock: ").strip()
            nueva_cantidad = int(inp_cantidad) if inp_cantidad else None

            mi_inventario.actualizar_producto(id, nuevo_nombre, nueva_categoria, nuevo_precio, nuevo_peso, nueva_cantidad)

        # 4. Consultar específica del producto
        elif opcion == "4":
            print("\n<--- CONSULTAR PRODUCTO --->")
            criterio = input("Ingresa ID, nombre o categoría a buscar: ").strip()
            resultados = mi_inventario.buscar_producto(criterio)
            
            if resultados:
                print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
                for p in resultados:
                    print(p.mostrar_info())
            else:
                print("No se encontraron productos que coincidan con la búsqueda.")

        # 5. Calcular valor total del inventario
        elif opcion == "5":
            total = mi_inventario.calcular_valor_total()
            print(f"\nEl valor total del inventario es: ${total:,.2f}")

        # 6. Consulta General de productos
        elif opcion == "6":
            mi_inventario.consultar_general()

        # 7. Guardar inventario en archivo txt
        elif opcion == "7":
            print("\n<--- GUARDAR INVENTARIO --->")
            mi_inventario.guardar_archivo("inventario/data/inventario.txt")

        # 8. Bajo Stock de productos (5 o menos)
        elif opcion == "8":
            print("\n<--- PRODUCTOS CON BAJO STOCK (5 o menos unidades) --->")
            bajos = mi_inventario.productos_bajo_stock(limite=5)
            
            if bajos:
                print(f"\nAlerta: Los siguientes productos tienen 5 o menos unidades:")
                for p in bajos:
                    print(p.mostrar_info())
            else:
                print("Todos los productos tienen suficiente stock.")

        # 9. Salir
        elif opcion == "9":
            print("\n¡Gracias por usar el sistema de inventario! Hasta luego :) .")
            break

        else:
            print("Opción no válida. Por favor, selecciona un número entre 1 y 9.")


if __name__ == "__main__":
    main()