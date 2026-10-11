from scripts.producto import Producto
import os

class Inventario:
    def __init__(self):
        # lista para los objetos Producto
        self.productos = []

    def agregar_producto(self, producto: Producto) -> bool:
        # agrega un producto y valida que no pueda haber duplicados
        for p in self.productos:
            if p.id == producto.id:
                print(f"Error: Ya existe un producto con el código '{producto.id}'.")
                return False
        
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado con éxito.")
        return True

    def eliminar_producto(self, id: str) -> bool:
        # elimina un producto buscando por código
        for p in self.productos:
            if p.id == id:
                self.productos.remove(p)
                print(f"Producto con código '{id}' eliminado correctamente.")
                return True
        
        print(f"No se encontró ningún producto con el código '{id}'.")
        return False

    def buscar_producto(self, criterio: str) -> list:
        # busca productos por código, nombre o categoría, devuelve una lista
        coincidencias = []
        criterio_lower = criterio.lower()
        
        for p in self.productos:
            if (criterio_lower in p.id.lower() or 
                criterio_lower in p.nombre.lower() or 
                criterio_lower in p.categoria.lower()):
                coincidencias.append(p)
        
        return coincidencias

    def actualizar_producto(self, id: str, nuevo_nombre=None, nueva_categoria=None, nuevo_precio=None, nuevo_peso=None, nueva_cantidad=None) -> bool:
        # actualizar precio, peso o cantidad
        for p in self.productos:
            if p.id == id:
                if nuevo_nombre is not None:
                    p.nombre = nuevo_nombre
                if nueva_categoria is not None:
                    p.categoria = nueva_categoria
                if nuevo_precio is not None:
                    p.precio = nuevo_precio
                if nuevo_peso is not None:
                    p.peso = nuevo_peso
                if nueva_cantidad is not None:
                    p.cantidad = nueva_cantidad
                print(f"Producto '{id}' actualizado con éxito.")
                return True
        
        print(f"No se encontró el producto con ID '{id}'.")
        return False

    def consultar_general(self):
        # mostrar todos los productos
        if not self.productos:
            print("El inventario está vacío.")
            return
        
        print("\n" + "="*60)
        print("<-- Lista de PRODUCTOS en inventario -->")
        print("="*60)
        for p in self.productos:
            print(p.mostrar_info())
        print("="*60)

    def calcular_valor_total(self) -> float:
        # calcula el valor total del inventario (precio * cantidad de cada producto)
        total = sum(p.precio * p.cantidad for p in self.productos)
        return total

    def productos_bajo_stock(self, limite: int = 5) -> list:
        # devuelve productos cuya cantidad sea menor o igual a 5
        return [p for p in self.productos if p.cantidad <= limite]

    # guardar la lista de productos actual en un txt
    def guardar_archivo(self, ruta_archivo: str = "inventario/data/inventario.txt") -> bool:
        if not self.productos:
            print("El inventario está vacío. No hay datos para guardar.")
            return False

        try:
            # Obtiene el directorio de la ruta (ej. 'data')
            directorio = os.path.dirname(ruta_archivo)
            
            # Si se especificó una carpeta y no existe, la crea
            if directorio and not os.path.exists(directorio):
                os.makedirs(directorio)

            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("=== INVENTARIO DE PRODUCTOS ===\n\n")
                for p in self.productos:
                    archivo.write(p.mostrar_info() + "\n")
            
            print(f"\nInventario guardado exitosamente en '{ruta_archivo}'.")
            return True
            
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")
            return False

# Validacionessss
#Pide un número al usuario por consola y repite la pregunta 
#hasta que ingrese un valor válido y no negativo (>= 0).
def pedir_numero_positivo(mensaje: str, es_entero: bool = False):
    while True:
        try:
            entrada = input(mensaje)
            valor = int(entrada) if es_entero else float(entrada)
            
            if valor < 0:
                print("Error: El número no puede ser negativo. Intenta de nuevo.")
            else:
                return valor
        except ValueError:
            print("Error: Debes ingresar un número válido.")