lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]
numeros_vistos = set()  # Conjunto para rastrear los números que ya hemos visto

print("Números repetidos en la lista:")

for numero in lista_numeros:
    if numero in numeros_vistos:
        print(numero)
    else:
        numeros_vistos.add(numero)  # Agregamos el número al conjunto para rastrearlo
