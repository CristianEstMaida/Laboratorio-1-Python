# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

# Inicializar contadores y variables
cantidad_pares = 0
cantidad_impares = 0

menor_numero = None
mayor_par = None
suma_positivos = 0
producto_negativos = 1
bandera_par = False
bandera_negativos = False

lista_numeros = []
contador  = 0
while contador < 5:
    numero = int(input(f"Ingrese el número {contador + 1} entero: "))
    # Verificar que el número no sea cero
    while numero == 0:
        numero = int(input("El número debe ser distinto de cero. Intente de nuevo: "))

    lista_numeros.append(numero)
    contador += 1
# Pedir 5 números enteros distintos de cero
for i in range(5):
   
    #a
    # Contar pares e impares
    if numero % 2 == 0:
        cantidad_pares += 1
        #c
        # if mayor_par is None or numero > mayor_par:
        #     mayor_par = numero
    else:
        cantidad_impares += 1
    #b
    # Encontrar el menor número
    if menor_numero is None or numero < menor_numero:
        menor_numero = numero

    #c
    if numero % 2 == 0:
        if mayor_par is None or numero > mayor_par:
            mayor_par = numero
            bandera_par = True
    #d
    # Calcular suma de positivos y producto de negativos
    if numero > 0:
        suma_positivos += numero
    #e
    else:
        producto_negativos *= numero
        bandera_negativos = True

# Informar los resultados

if cantidad_pares == 0:
    print("No se ingresaron números pares.")
else:
    print(f"Cantidad de pares: {cantidad_pares}")

if cantidad_impares == 0:
    print("No se ingresaron números impares.")
else:
    print(f"Cantidad de impares: {cantidad_impares}")

print(f"Menor número ingresado: {menor_numero}")

if bandera_par == True:
    print(f"Mayor número par ingresado: {mayor_par}")
else:
    print("No se ingresaron números pares.")

if suma_positivos > 0:
    print(f"Suma de los positivos: {suma_positivos}")
else:
    print("No se ingresaron números positivos.")

if bandera_negativos == True:
    print(f"Producto de los negativos: {producto_negativos}")
else:
    print("No se ingresaron números negativos.")
