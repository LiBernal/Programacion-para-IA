class Producto:
    def __init__(self, id: str, nombre: str, categoria: str, precio: float, peso: float, cantidad: int):
        # validaciones de valores no negativos
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if peso < 0:
            raise ValueError("El peso no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        # 6 atributos del producto
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.peso = float(peso)
        self.cantidad = int(cantidad)

    def mostrar_info(self):
        #cadena con los datos del producto
        return (f"Id: {self.id} | Nombre: {self.nombre} | "
                f"Categoría: {self.categoria} | Precio: ${self.precio:.2f} | "
                f"Peso: {self.peso} kg | Stock: {self.cantidad}")
