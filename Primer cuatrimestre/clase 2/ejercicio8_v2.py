lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

print("Números repetidos en la lista:")

for i in range(len(lista_numeros)):
    repetido = False
    for j in range(i + 1, len(lista_numeros)):
        if lista_numeros[i] == lista_numeros[j]:
            repetido = True
            break
    if repetido:
        print(lista_numeros[i])