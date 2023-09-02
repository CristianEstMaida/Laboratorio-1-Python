# Copyright (C) 2023 <UTN FRA>
# ...

'''
UTN Inversiones, realiza un estudio de mercado para saber cuál será la nueva franquicia que se insertará en el 
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
4. Porcentaje de empleados que no votaron por APPLE, siempre y cuando su género no sea Femenino y su edad se encuentre 
entre los 18 y 30.
5. Nombre y edad de los empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados.
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
        cantidad_votantes_apple = 0
        for i in range(len(lista_nombres)):
            if lista_votos[i] == "APPLE" and lista_edades[i] <= 35:
                cantidad_votantes_apple += 1

        print(f"Cantidad de encuestados que votaron por APPLE y tienen <= 35 años: {cantidad_votantes_apple}")

    elif opcion == 3:
        # Opción 3: Género que predomina en la empresa
        cantidad_masculino = 0
        cantidad_femenino = 0
        cantidad_otro = 0

        for genero in lista_generos:
            match genero:
                case "Masculino":
                    cantidad_masculino += 1
                case "Femenino":
                    cantidad_femenino += 1    
                # case "Otro":
                case _:
                    cantidad_otro += 1    
            # if genero == "Masculino":
            #     cantidad_masculino += 1
            # elif genero == "Femenino":
            #     cantidad_femenino += 1
            # elif genero == "Otro":
            #     cantidad_otro += 1

        if cantidad_masculino >= cantidad_femenino and cantidad_masculino >= cantidad_otro:
            genero_predominante = "Masculino"
        elif cantidad_femenino >= cantidad_masculino and cantidad_femenino >= cantidad_otro:
            genero_predominante = "Femenino"
        else:
            genero_predominante = "Otro"
        print(f"Género que predomina en la empresa: {genero_predominante}")

    elif opcion == 4:
        # Opción 4: Porcentaje de empleados que no votaron por APPLE, cumple condiciones
        cantidad_empleados = len(lista_nombres)
        cantidad_no_apple_filtrados = 0
        # cantidad_votantes_apple = 0
        # cantidad_filtrados = 0

        for i in range(cantidad_empleados):
            if lista_votos[i] != "APPLE" and lista_generos[i] != "Femenino" and lista_edades[i] in range(18, 31):
            # if lista_votos[i] != "APPLE" and lista_generos[i] != "Femenino" and 18 <= lista_edades[i] <= 30:
                cantidad_no_apple_filtrados += 1
            # if lista_votos[i] == "APPLE":
            #     cantidad_votantes_apple += 1
            # if lista_votos[i] != "APPLE" and (lista_generos[i] != "Femenino" or lista_edades[i] in range(18, 31)):
            #     cantidad_filtrados += 1
            # if lista_votos[i] != "APPLE" and (lista_generos[i] != "Femenino" or not (18 <= lista_edades[i] <= 30)):
                # cantidad_filtrados += 1
        if cantidad_empleados > 0:
            porcentaje = (cantidad_no_apple_filtrados / cantidad_empleados) * 100
            print(f"Porcentaje de empleados que no votaron por APPLE y cumplen condiciones: {porcentaje:.2f}%")
        else:
            print("No hay empleados registrados.")
        # porcentaje = (cantidad_filtrados / cantidad_empleados) * 100
        # print(f"Porcentaje de empleados que no votaron por APPLE, cumple condiciones: {porcentaje:.2f}%")

    elif opcion == 5:
        # Opción 5: Nombre y edad de empleados que votaron IKEA o TACO, cuya edad supere la edad promedio de todos los empleados
        cantidad_empleados = len(lista_nombres)

        suma_edades = 0
        for i in range(cantidad_empleados):
            suma_edades += lista_edades[i]

        if cantidad_empleados > 0:
            edad_promedio = suma_edades / cantidad_empleados
            empleados_calificados = []

            for i in range(cantidad_empleados):
                if lista_votos[i] in ["IKEA", "TACO"] and lista_edades[i] > edad_promedio:
                    nombre = lista_nombres[i]
                    edad = lista_edades[i]
                    empleados_calificados.append((nombre, edad))

            if empleados_calificados:
                print("Empleados que votaron IKEA o TACO y edad > promedio de empleados:")
                for nombre, edad in empleados_calificados:
                    print(f"Nombre: {nombre}, Edad: {edad}")
            else:
                print("No hay empleados que cumplan con los criterios.")
        else:
            print("No hay empleados registrados.")

    elif opcion == 6:
        print("Adiós")
        break

    else:
        print("Opción incorrecta (1-6)")
