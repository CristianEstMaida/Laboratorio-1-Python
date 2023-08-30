# Inicializar contadores y variables
cantidad_pares = 0
cantidad_impares = 0
menor_numero = None
mayor_par = None
suma_positivos = 0
producto_negativos = 1

# Pedir 5 números enteros distintos de cero
for i in range(5):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    
    # Verificar que el número no sea cero
    while numero == 0:
        numero = int(input("El número debe ser distinto de cero. Intente de nuevo: "))
    
    # Contar pares e impares
    if numero % 2 == 0:
        cantidad_pares += 1
        if mayor_par is None or numero > mayor_par:
            mayor_par = numero
    else:
        cantidad_impares += 1
    
    # Encontrar el menor número
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero
    
    # Calcular suma de positivos y producto de negativos
    if numero > 0:
        suma_positivos += numero
    else:
        producto_negativos *= numero

# Informar los resultados
print(f"Cantidad de pares: {cantidad_pares}")
print(f"Cantidad de impares: {cantidad_impares}")
print(f"Menor número ingresado: {menor_numero}")
print(f"Mayor número par ingresado: {mayor_par}")
print(f"Suma de los positivos: {suma_positivos}")
print(f"Producto de los negativos: {producto_negativos}")