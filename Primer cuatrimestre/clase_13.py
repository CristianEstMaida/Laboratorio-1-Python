'''
clase 13

'''

variable_1 = "hola"
variable_2 = variable_1

print (variable_1) #hola
print (variable_2) #hola

variable_1 = "chau"

print (variable_1) #chau
print (variable_2) #hola

print(lambda a, b : a + b(4,5)) #dirección de memoria

sumar = lambda a, b : a + b

print(sumar(4,5)) #9

a = 2
b = 13

print("Verdadero") if a < b else print("Falso")

mayor = lambda a, b : a if a > b else b #Devuelve el número que sea más grande de los dos
                                        #pasados por parámetro
lista_1 = [["Marty","McFly"], "Emmett", "Biff"]

#Sallow copy / Copia superficial

lista_2 = lista_1.copy()

lista_1[0][0] = "MARTY"
lista_1[2] = "Pedro"

print(lista_1)
print(lista_2)

#Deep copy / Copia profunda

from copy import deepcopy

lista_1 = [["Marty","McFly"], "Emmett", "Biff"]


lista_2 = deepcopy(lista_1)

lista_1[0][0] = "MARTY"
lista_1[2] = "Pedro"

print(lista_1)
print(lista_2)

lista = ["Marty", "Emmett", "Biff"]

lista.insert(1,"Jennifer")

lista.insert(5,"Jennifer")

print(lista)

lista = ["Marty", "Emmett", "Biff"]

lista.extend("Jennifer")

print(lista)

lista = ["Marty", "Emmett", "Biff"]

elemento_eliminado = lista_1.pop(1)

print(lista)

print(elemento_eliminado)

lista = ["Marty", "Emmett", "Biff"]

lista.remove("Marty")

print(lista)

lista = ["Marty", "Emmett", "Biff"]

print(lista.index("Emmett"))

lista_1 = ["Marty", "Emmett", "Biff"]

for indice,elemento in enumerate(lista_1):
    print(indice,elemento)
    

lista_1 = ["Marty", "Emmett", "Biff"]

lista_2 = ["McFly", "Brown", "Tannen"]

lista_3 = ["17", "71", "18"]

for elem_l1, elem_l2, elem_l3 in zip(lista_1, lista_2, lista_3):
    print(elem_l1, elem_l2, elem_l3)
    

lista = ["Marty", "Emmett", "Biff"]

lista_resultado = list(map(str.upper, lista))

print(resultado)

print(lista_resultado)

lista = [17, 71, 18]

lista_resultado= list(filter(lambda elem: elem >= 18, lista))

print(lista_resultado)

from functools import reduce

lista = [17, 71, 18]

suma = reduce(lambda x, y: x + y, lista)

print(suma)

from random import shuffle

lista = ["Marty", "Emmett", "Biff"]

shuffle(lista)
