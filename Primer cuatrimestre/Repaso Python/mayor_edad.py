#Declara variable, se le tiene que asignar un valor
'''
nombre = "marina"

print("Hola mundo")

numero = input("Ingrese su nombre")

print("El nombres es {0}".format(nombre))
print(f"El nombre es {nombre}")



    Operadores logicos
    and (&&)
    or (||)
    not (!)

es_impar = numero % 2

if numero == 2:
    print("Estoy dentro del if")

    print("es el numero dos")
elif numero < 2 and es_impar != 0:
    print("Es menor a dos")
else:
    print("No es el numero dos")
print("fuera del if")


match mes:
    case 'abril':
        print("Es mi cumple")
    case 'mayo':
        print("cumple mi mama")
    case _:
        print("No recuerdo si hay cumples")

while continuar == 's':
    print("Iteramos")
    continuar = input('Si desea continuar ingrese s')

#[0,1,2,3,4,5,6,7,8,9]

    for elementos in lista
    range(10) ----> [0,1,2,3,4,5,6,7,8,9] genera una lista secuencial de numeros

    [0,1,2,3,4,5,6,7,8,9]
     0,1,2,3,4,5,6,7,8,9  ---> indices


    [2,3,"marina",[0,1]]
     0,1,      2, 3  ----> indices


     int numerosArray[10]
'''
numeros = []

numeros_lista = list()

#print(numero[2])

numeros.append("juan")

'''
    Alumnos
    nombre
    edad
    altura

'''
nombre = "Marina"
edad = 23
altura = 1.70

print(type(nombre))
print(type(edad))
print(type(altura))

nombres_alumnos = ["juan","mariana","pepe"]
edades_alumnos = [20,25,30]
altura_alumnos = [1.80,1.50,1.70]

'''
#Carga de datos
while continuar == 'si':

    nombre = input("Ingrese un nombre")

    edad = input("Ingrese una edad")
    while edad.isdigit() == False or int(edad) < 1:
        edad = input("Error! Ingrese una edad")
    
    edad = int(edad)

    altura = input("Ingrese la altura")
    altura = float(altura)
    while altura < 0:
        altura = input("Error! Ingrese la altura")
        altura = float(altura)

    nombres_alumnos.append(nombre)
    edades_alumnos.append(edad)
    altura_alumnos.append(altura)
    continuar = input("Desea continuar ? si ")
'''

#manejar los datos ingresados

tam_lista = len(nombres_alumnos) #me retora la cantidad de elementos que tiene
print("El tamaño de la lista esss")
print(tam_lista)

mayor_edad = None
for indice in range(tam_lista):
    print("Indice: {3} El alumno es Nombre: {0} edad: {1} altura: {2}".format(nombres_alumnos[indice],edades_alumnos[indice],altura_alumnos[indice],indice))
    
    edad = edades_alumnos[indice]
    if indice == 0:
        mayor_edad = edad
    elif edad > mayor_edad:
        mayor_edad = edad


   

contador = 0
for elemento in nombres_alumnos:

    print(elemento)
    contador = contador +1 