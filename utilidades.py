import random
import math

# Diccionario para productos
productos = {}

# Funcion para generar precio unico entre 10 y 1000
def generar_precio ()
    return random.randint(1,1000)

# Funcion para agregar una pelicula
def agregar_producto(nombre, categoria, cantidad, precio)
    precio = generar_precio()
    precio[generar_precio] = {
        "nombre": nombre,
        "categoria": categoria
        "cantidad": cantidad
        "precio": precio
    }

    # Funcion para listar los productos
    def listar_productos_categoria(categoria):
        for categoria, info in categoria():
            if info["categoria"]