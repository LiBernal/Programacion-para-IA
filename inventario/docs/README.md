## Sistema de inventario
Sistema de gestión de inventario desarrollado en Python utilizando prácticas de POO.

### Estructura del proyecto:

```text
inventario/
├── data/
│   └── inventario.txt
├── docs/
│   └── README.md
├── scripts/
│   ├── inventario.py
│   └── producto.py
└── main.py
```

### ¿Cómo probarlo?
Cuenta con un menú con las siguientes opciones:
1. Agregar producto: Registra un nuevo producto solicitando ID, nombre, categoría, precio, peso y cantidad.
2. Eliminar producto: Elimina un producto ingresando su ID.
3. Actualizar producto: Permite modificar los datos de un producto por su ID. (Si presionas Enter sin ingresar texto, el atributo actual se mantendrá sin cambios).
4. Buscar producto(s): Permite realizar búsquedas por coincidencia en ID, nombre o categoría.
5. Calcular valor total del inventario: Muestra la suma total del valor acumulado (precio * cantidad) de todos los productos.
6. Consulta general: Muestra la lista completa de productos registrados.
7. Guardar inventario: Exporta los productos actuales a un archivo de texto (data/inventario.txt).
8. Bajo stock: Lista los productos con 5 o menos unidades disponibles en inventario.
9. Salir: Finaliza la ejecución del programa.