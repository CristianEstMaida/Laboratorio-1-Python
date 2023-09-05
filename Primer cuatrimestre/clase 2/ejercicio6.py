lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

mayor = None

for numero in lista_numeros:
    if mayor == None or numero > mayor:
        mayor = numero

print("El número mayor en la lista es:", mayor)

