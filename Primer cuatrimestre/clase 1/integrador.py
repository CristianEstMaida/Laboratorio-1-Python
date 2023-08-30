barbijo_mas_caro_precio = 0
barbijo_mas_caro_cantidad = 0
barbijo_mas_caro_fabricante = ""

max_unidades = 0
max_unidades_fabricante = ""
total_jabones = 0

for _ in range(5):
    tipo = input("Ingrese el tipo de producto (barbijo, jabón o alcohol): ").lower()
    while tipo not in ["barbijo", "jabón", "alcohol"]:
        tipo = input("Tipo inválido. Ingrese nuevamente (barbijo, jabón o alcohol): ").lower()
    
    precio = float(input("Ingrese el precio del producto (entre 100 y 300): "))
    while precio < 100 or precio > 300:
        precio = float(input("Precio inválido. Ingrese nuevamente (entre 100 y 300): "))
    
    cantidad = int(input("Ingrese la cantidad de unidades (mayor que 0 y hasta 1000): "))
    while cantidad <= 0 or cantidad > 1000:
        cantidad = int(input("Cantidad inválida. Ingrese nuevamente (mayor que 0 y hasta 1000): "))
    
    marca = input("Ingrese la marca del producto: ")
    fabricante = input("Ingrese el fabricante del producto: ")
        
    if tipo == "barbijo":
        if precio > barbijo_mas_caro_precio:
            barbijo_mas_caro_precio = precio
            barbijo_mas_caro_cantidad = cantidad
            barbijo_mas_caro_fabricante = fabricante
    
    if cantidad > max_unidades:
        max_unidades = cantidad
        max_unidades_fabricante = fabricante
    
    if tipo == "jabón":
        total_jabones += cantidad
    
print(f"El más caro de los barbijos tiene una cantidad de {barbijo_mas_caro_cantidad} unidades y es fabricado por: {barbijo_mas_caro_fabricante}")
print(f"El ítem con más unidades es: {max_unidades_fabricante} y tiene: {max_unidades} unidades")
print(f"La cantidad total de jabones es {total_jabones}")
print("Gracias por utilizar el programa")