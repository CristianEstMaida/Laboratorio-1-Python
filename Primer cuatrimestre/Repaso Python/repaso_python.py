#Declarar una variable, se le tiene que asignar un valor

nombre = "Marina"

print("Hola mundo")

nombre = input("Ingrese su nombre")

numero = input("Ingrese un número")
int(numero)

print("El nombre es {0}".format(nombre))

print(f"El nombre es ${nombre}")

#operadores lógicos
#and
#or
#not

es_impar = numero % 2
if numero == 2:
    print("Estoy dentro del if")
    print("Es el numero dos")
elif numero < 2 and es_impar != 0:
    print("Es menor a dos")
else:
    print("No es el numero dos")
print("Fuera del if")

mes = input("Ingrese un mes de nacimiento")
int(mes)

match mes:
    case 'abril':
        print("Es mi mes de nacimiento")
    case 'mayo':
        print("Es el mes de nacimiento de mi mamá")
    case _:
        print("No recuerdo si es el mes de nacimiento de un conocido")

while continuar == 's':
    print("Iteramos")
    continuar = input('Si desea continuar ingrese s')

#[0,1,2,3,4,5,6,7,8,9]

#range(10) [0,1,2,3,4,5,6,7,8,9] - genera una lista secuencial de números
#0,1,2,3,4,5,6,7,8,9 - índices
# [2,3,"Marina",[0,1]] 
#las listas pueden guardar cualquier dato y están indexadas
#0,1,2,3 - índices
for numero in range(10):
    # print("El número es {0}".format(numero))
    print(f"El número es {numero}")

#declarar lista
numeros = []
numeros_lista = list()

#mostrar elemento lista
print(numero[2])

#agregar elemento a una lista
numeros.append("juan")

#alumnos
#nombre
#edad
#altura


nombre = 'Marina'
edad = 23
altura = 1.70

print(type(nombre))
print(type(edad))
print(type(altura))

nombres_alumnos = []
edades_alumnos = []
altura_alumnos = []
#harcodeo para prueba rápida
# nombres_alumnos = ["juan", "marina", "pepe"]
# edades_alumnos = [20, 35, 50]
# altura_alumnos = [1.80, 1.50, 1.70]

#carga de datos
while continuar == True:
    nombre = input("Ingrese un nombre")

    edad = input("Ingrese una edad")
    while edad.isdigit() == False or int(edad) < 1:
        edad = input("Error.Ingrese una edad")

    edad = int(edad)

    altura = input("Ingrese la altura")
    altura = float(altura)
    # while float(altura) < 0:
    while altura < 0:
        altura = input("Error.Ingrese la altura")

    altura = float(altura)

    nombres_alumnos.append(nombre)
    edades_alumnos.append(edad)
    altura_alumnos.append(altura)

    continuar  = input("Desea continuar? (si/no)")

    #manejar los datos ingresados

    tam_lista = len(nombres_alumnos) #me retorna la cantidad de elementos que tiene
    print("El tamaño de la lista es")
    print(tam_lista)

    mayor_edad = None
    contador_mayores_veinte = 0
    for indice in range(tam_lista):
        print("Indice: {4} El alumno es Nombre {0} edad: {1} altura: {2}".format(nombres_alumnos[indice], edades_alumnos[indice], altura_alumnos[indice], indice))
        if edades_alumnos[indice] > 20:
            contador_mayores_veinte = contador_mayores_veinte + 1

        edad = edades_alumnos[indice]
        if indice == 0:
            mayor_edad = edad
        elif edad > mayor_edad:
            mayor_edad = edad

    contador = 0
    for elemento in nombres_alumnos:
        print(elemento)
        contador = contador + 1
