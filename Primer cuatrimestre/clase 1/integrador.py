lista_producto = []
lista_precio = []
lista_unidades= []
lista_marca = []
lista_fabricante = []

contador = 0
maximo_barbijo =  None
maximo_unidades = None
unidades_de_jabon = 0

#Ingreso y validación de datos
while contador < 5:
    contador += 1
    producto = input("Ingrese el producto (jabon, barbijo o alcohol): ")
    while producto != "barbijo" and producto != "jabon" and producto != "alcohol":
        producto = input("Error, ingrese un producto válido: ")

    producto = float(input(f"Ingrese el precio del producto ({producto}) que sea entre $100 y $300): "))
    while precio < 100 or precio > 300:
        precio = input("Error, ingrese un producto válido: ")

    unidades = int(input(f"Ingrese la cantidad de unidades del producto ({producto}) que sea entre 1 y 1000 unidades: "))
    while unidades < 1 or unidades > 1000:
        unidades = int(f"Error, ingrese una cantidad válida para el producto ({producto}: )")
    marca = input(f"Ingrese la marca del producto ({producto} que sea M1, M2, M3)")
    while marca != "M1" and marca != "M2" and marca != "M3":
        marca = input(f"Error, ingrese una marca válida para el producto ({producto})")
    fabricante = input(f"Ingrese el fabricante del producto ({producto}) F1, F2 o F3")
    while fabricante != "F1" and fabricante != "F2" and fabricante != "F3":
        fabricante = input(f"Error, ingrese un fabricnte del producto ({producto}) M1, M2 o M3")

    lista_producto.append(producto)
    lista_precio.append(precio)
    lista_unidades.append(unidades)
    lista_marca.append(marca)
    lista_fabricante.append(fabricante)

    for indice in range(len(lista_producto)):
        #a
        if lista_producto[indice] == "barbijo":
            if maximo_barbijo == None or lista_precio[indice] > maximo_barbijo:
                maximo_barbijo = lista_precio[indice]
                cantidad_unidades_barbijo = lista_unidades[indice]
                fabricante_barbijo = lista_fabricante[indice]
        #c
        elif lista_producto[indice] == "jabon":
            unidades_de_jabon += lista_unidades[indice]
        #b
        if maximo_unidades == None or lista_unidades[indice] > maximo_unidades:
            maximo_unidades = lista_unidades[indice]
            fabricante_maximo_unidades = lista_unidades[indice]
            nombre_producto_maximo_unidades = lista_producto[indice]

print(f"El barbijo mas caro tiene un precio de ${maximo_barbijo} con {cantidad_unidades_barbijo} unidades de la marca {fabricante_barbijo}")
print(f"El producto con más unidades es el {nombre_producto_maximo_unidades} con {maximo_unidades} unidades de la marca {fabricante_maximo_unidades}")
print(f"Hay un total de {unidades_de_jabon} jabones")

'''
barbijo, 150, 500, M1, F1
jabon, 120, 250, M2, F2
alcohol, 290, 330, M3, F3
barbijo, 120, 350, M3, F1
jabon, 110, 450, M1, F3

A) 500 y F1
B) 500 Y f1
C) 700

'''
