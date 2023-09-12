from data_stark import lista_personajes

def opcion_a():
  # Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
#   contador = 0
#   print(f"Nombre, Identidad, Empresa, Altura, Peso, Genero, Color de ojos, Color de pelo, Fuerza e Inteligencia")
#   for superheroe in lista_personajes:
#     contador += 1
    # print(f"Superheroe {contador}")
    
    # for lista in superheroe:
    #     print(f"{superheroe[lista]} - ", end="")
        
    # print()
    print("+-----------------+-------------------------------+---------------+--------------------+----------------------+--------+-------+--------+--------+--------------+")
    print(f"| Nombre\t  | Identidad\t\t\t  | Empresa\t  | Altura\t       | Peso\t\t      | Género | Ojos  | Pelo   | Fuerza | Inteligencia |")
    print("+-----------------+-------------------------------+---------------+--------------------+----------------------+--------+-------+--------+--------+--------------+")
    for superheroe in lista_personajes:
        print(f"| {superheroe['nombre']:15} | {superheroe['identidad']:29} | {superheroe['empresa']:10} | {superheroe['altura']:18} | {superheroe['peso']:20} | {superheroe['genero']:6} | {superheroe['color_ojos']:5} | {superheroe['color_pelo']:6} | {superheroe['fuerza']:6} | {superheroe['inteligencia']:12} |" )
        # print(f"| {superheroe['nombre']:10} | {superheroe['identidad']:15} | {superheroe['empresa']:10} | {superheroe['altura']:10.2f} | {superheroe['peso']:10.2f} | {superheroe['genero']:8} | {superheroe['color_ojos']:10} | {superheroe['color_pelo']:10} | {superheroe['fuerza']:10.2f} | {superheroe['inteligencia']:10.2f} |")

    print("+-----------------+-------------------------------+---------------+--------------------+----------------------+--------+-------+--------+--------+--------------+")
        

def opcion_b():
  # Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
  maximo_fuerza = 0
  super_fuerte = None
  for superheroe in lista_personajes:
    if superheroe["fuerza"] > maximo_fuerza:
      maximo_fuerza = superheroe["fuerza"]
      super_fuerte = superheroe
  print(f"Superhéroe con mayor fuerza: {super_fuerte['identidad']} (peso: {super_fuerte['peso']})")

def opcion_c():
  # Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
  minimo_altura = float("inf")
  super_bajo = None
  for superheroe in lista_personajes:
    if superheroe["altura"] < minimo_altura:
      minimo_altura = superheroe["altura"]
      super_bajo = superheroe
  print(f"Superhéroe más bajo: {super_bajo['nombre']} (identidad: {super_bajo['identidad']})")

def opcion_d():
  # Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
  suma_pesos_masculinos = 0
  cantidad_superheroes_masculinos = 0
  for superheroe in lista_personajes:
    if superheroe["genero"] == "M":
      suma_pesos_masculinos += superheroe["peso"]
      cantidad_superheroes_masculinos += 1
  promedio_peso_masculino = suma_pesos_masculinos / cantidad_superheroes_masculinos
  print(f"Promedio de peso de los superhéroes masculinos: {promedio_peso_masculino}")

def opcion_e():
  # Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superheroínas de género femenino
  fuerza_promedio_heroinas = 0
  cantidad_heroinas = 0
  for superheroe in lista_personajes:
    if superheroe["genero"] == "F":
      fuerza_promedio_heroinas += superheroe["fuerza"]
      cantidad_heroinas += 1
  fuerza_promedio_heroinas /= cantidad_heroinas
  for superheroe in lista_personajes:
    if superheroe["fuerza"] > fuerza_promedio_heroinas:
      print(f"Superhéroe con fuerza superior a la promedio de las superheroínas: {superheroe['nombre']} (identidad: {superheroe['identidad']})")

print("**Menú Desafío Stark #01**")
print("(A) Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe")
print("(B) Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)")
print("(C) Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)")
print("(D) Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)")
print("(E) Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superheroínas de género femenino")

opcion = input("Ingrese una opción: ")

if opcion == "A":
  opcion_a()
elif opcion == "B":
  opcion_b()
elif opcion == "C":
  opcion_c()
elif opcion == "D":
  opcion_d()
elif opcion == "E":
  opcion_e()
else:
  print("Opción no válida")