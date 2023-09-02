# Copyright (C) 2023 <UTN FRA>
# ...

'''
UTN Inversiones, realiza un estudio de mercado para saber cual será la nueva franquicia que se insertará en el 
mercado argentino y en la cual invertir
Las posibles franquicias son las siguientes: 
# Apple,
# Dunkin Donuts, 
# Ikea o 
# Taco Bell.

Para ello, se realizará una encuesta mediante un sistema de voto electrónico, con el propósito de conocer cuáles
son los gustos de los encuestados:

El programa tendrá precargado un menú de opciones en el que debemos programar lo siguiente

1. Cargar voto, esta opción agregará a las listas un voto en específico pidiendo los siguientes datos
    nombre del encuestado.
    edad (no menor a 18)
    género (Masculino - Femenino - Otro)
    voto (APPLE, DUNKIN, IKEA, TACO)   
    
2. Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años.
3. Género que predomina en la empresa.
4. Porcentaje de empleados que no votaron por APPLE , siempre y cuando su género no sea Femenino y su edad se encuentre 
entre los 18 y 30.
5. Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados
6. Salir
'''

# Define the initial lists
lista_nombres = []
lista_edades = []
lista_generos = []
lista_votos = []

while True:
    print("\n1. Cargar Voto\n2. Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años\n3. Género que predomina en la empresa.\n4. Porcentaje de empleados que no votaron por APPLE, cumple condiciones.\n5. Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados.\n6. Salir")
    
    opcion = input("Ingrese una opción 1-6:")
    opcion = int(opcion)

    if opcion == 1:
        # Opción 1: Cargar Voto
        nombre = input("Nombre del encuestado: ")
        
        while True:
            edad = input("Edad (no menor a 18): ")
            if edad.isdigit():
                edad = int(edad)
                if edad >= 18:
                    break
                else:
                    print("La edad debe ser mayor o igual a 18.")
            else:
                print("Ingrese una edad válida (número entero).")
        
        genero = input("Género (Masculino/Femenino/Otro): ")
        
        while True:
            voto = input("Voto (APPLE/DUNKIN/IKEA/TACO): ").upper()
            if voto in ["APPLE", "DUNKIN", "IKEA", "TACO"]:
                break
            else:
                print("Voto no válido. Ingrese uno de los siguientes: APPLE, DUNKIN, IKEA, TACO.")

        lista_nombres.append(nombre)
        lista_edades.append(edad)
        lista_generos.append(genero)
        lista_votos.append(voto)

    elif opcion == 2:
        # Opción 2: Cantidad de encuestados que votaron por APPLE, cuya edad no supere los 35 años
        count_apple_voters = 0
        for i in range(len(lista_nombres)):
            if lista_votos[i] == "APPLE" and lista_edades[i] <= 35:
                count_apple_voters += 1

        print(f"Cantidad de encuestados que votaron por APPLE y tienen <= 35 años: {count_apple_voters}")

    elif opcion == 3:
        # Opción 3: Género que predomina en la empresa
        masculino_count = 0
        femenino_count = 0
        otro_count = 0

        for genero in lista_generos:
            if genero == "Masculino":
                masculino_count += 1
            elif genero == "Femenino":
                femenino_count += 1
            elif genero == "Otro":
                otro_count += 1

        if masculino_count >= femenino_count and masculino_count >= otro_count:
            predominant_gender = "Masculino"
        elif femenino_count >= masculino_count and femenino_count >= otro_count:
            predominant_gender = "Femenino"
        else:
            predominant_gender = "Otro"
        print(f"Género que predomina en la empresa: {predominant_gender}")

    elif opcion == 4:
        # Opción 4: Porcentaje de empleados que no votaron por APPLE, cumple condiciones
        total_employees = len(lista_nombres)
        apple_voters = 0
        filtered_employees = 0

        for i in range(total_employees):
            if lista_votos[i] == "APPLE":
                apple_voters += 1
            if lista_votos[i] != "APPLE" and (lista_generos[i] != "Femenino" or not (18 <= lista_edades[i] <= 30)):
                filtered_employees += 1
        
        percentage = (filtered_employees / total_employees) * 100
        print(f"Porcentaje de empleados que no votaron por APPLE, cumple condiciones: {percentage:.2f}%")

    elif opcion == 5:
        # Opción 5: Nombre y edad de empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados
        total_employees = len(lista_nombres)

        total_age = 0
        for i in range(total_employees):
            total_age += lista_edades[i]

        if total_employees > 0:
            average_age = total_age / total_employees
            qualified_employees = []

            for i in range(total_employees):
                if lista_votos[i] in ["IKEA", "TACO"] and lista_edades[i] > average_age:
                    name = lista_nombres[i]
                    age = lista_edades[i]
                    qualified_employees.append((name, age))

            if qualified_employees:
                print("Empleados que votaron IKEA o TACO y edad > promedio de empleados:")
                for name, age in qualified_employees:
                    print(f"Nombre: {name}, Edad: {age}")
            else:
                print("No hay empleados que cumplan con los criterios.")
        else:
            print("No hay empleados registrados.")

    elif opcion == 6:
        print("Adiós")
        break

    else:
        print("Opción incorrecta (1-6)")
