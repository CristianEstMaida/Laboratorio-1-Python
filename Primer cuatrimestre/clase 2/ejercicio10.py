nombres = []
sexo = []
nota = []

for i in range(1, 6):
    nombre = input(f"Ingrese el nombre del alumno {i}: ")
    sexo_alumno = input(f"Ingrese el sexo del alumno {i} (f/m): ").lower()
    
    while sexo_alumno not in ["f", "m"]:
        sexo_alumno = input(f"Sexo inválido. Ingrese nuevamente (f/m) para el alumno {i}: ").lower()
    
    nota_alumno = float(input(f"Ingrese la nota del alumno {i} (0-10): "))
    
    while nota_alumno < 0 or nota_alumno > 10:
        nota_alumno = float(input(f"Nota inválida. Ingrese nuevamente (0-10) para el alumno {i}: "))
    
    nombres.append(nombre)
    sexo.append(sexo_alumno)
    nota.append(nota_alumno)

indice_hombre_nota_baja = None
nota_mas_baja_hombres = float('inf')

for i in range(len(nombres)):
    if sexo[i] == 'm' and nota[i] < nota_mas_baja_hombres:
        nota_mas_baja_hombres = nota[i]
        indice_hombre_nota_baja = i

if indice_hombre_nota_baja is not None:
    print("El hombre con la nota más baja es:", nombres[indice_hombre_nota_baja])
else:
    print("No se ingresaron hombres.")

suma_notas_mujeres = 0
cantidad_mujeres = 0

for i in range(len(nombres)):
    if sexo[i] == 'f':
        suma_notas_mujeres += nota[i]
        cantidad_mujeres += 1

if cantidad_mujeres > 0:
    promedio_notas_mujeres = suma_notas_mujeres / cantidad_mujeres
    print("El promedio de notas de las mujeres es:", promedio_notas_mujeres)
else:
    print("No se ingresaron mujeres.")