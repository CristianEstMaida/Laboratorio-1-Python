# Importar la lista de superhéroes
from data_stark import lista_personajes

# Variables
lista_superheroes = lista_personajes
bandera = True

# Bucle principal
while bandera:
  # Mostrar el menú de opciones
  print("**Menú Desafío Stark #01**")
  print("(A) Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe")
  print("(B) Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)")
  print("(C) Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)")
  print("(D) Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)")
  print("(E) Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superheroínas de género femenino")
  print("(F) Salir")

  # Leer la opción del usuario
  opcion = input("Ingrese una opción: ").upper()

  # Procesar la opción
  if opcion == "A":
    # Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
    print("+--------------------+-------------------------------+---------------+----------+-----------+--------+-------------------------+---------------------+--------+--------------+")
    print(f"| Nombre\t     | Identidad\t\t     | Empresa\t     | Altura   | Peso      | Género | Ojos\t\t       | Pelo\t\t     | Fuerza | Inteligencia |")
    print("+--------------------+-------------------------------+---------------+----------+-----------+--------+-------------------------+---------------------+--------+--------------+")
    for superheroe in lista_personajes:
        print(f"| {superheroe['nombre']:18} | {superheroe['identidad']:29} | {superheroe['empresa']:10} | \
{float(superheroe['altura'])/100:6.2f} m | {float(superheroe['peso']):6.2f} kg | {superheroe['genero']:6} | \
{superheroe['color_ojos']:23} | {superheroe['color_pelo']:19} | {float(superheroe['fuerza']):3.0f} N{'':1} | \
{superheroe['inteligencia']:12} |")
  elif opcion == "B":
    # Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
    maximo_fuerza = None
    super_fuertes = []
    for superheroe in lista_personajes:
      fuerza = int(superheroe["fuerza"])
      if fuerza == maximo_fuerza:
        super_fuertes.append(superheroe)
      elif maximo_fuerza == None or fuerza > maximo_fuerza:
        maximo_fuerza = fuerza
        super_fuertes = [superheroe]

    if len(super_fuertes) > 1:
      print(f"Hay {len(super_fuertes)} superhéroes con máxima fuerza:")
      print("+--------------+-----------+")
      print(f"| Identidad    | Peso      |")
      print("+--------------+-----------+")
      for superheroe in super_fuertes:
        print(f"| {superheroe['identidad']} | {float(superheroe['peso']):.2f} kg |")
      print("+--------------+-----------+")
    else:
      print("Superhéroe con mayor fuerza:")
      print("+--------------+-----------+")
      print(f"| Identidad    | Peso      |")
      print("+--------------+-----------+")
      print(f"| {super_fuertes[0]['identidad']} | {float(super_fuertes[0]['peso']):.2f} kg |")
      print("+--------------+-----------+")

  elif opcion == "C":
    # Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
    minimo_altura = None
    super_bajo = None
    for superheroe in lista_personajes:
      altura = float(superheroe["altura"])
      if minimo_altura == None or altura < minimo_altura:
        minimo_altura = altura
        super_bajo = superheroe
    print(f"El nombre del superhéroe más bajo es: {super_bajo['nombre']}")
    print(f"Su identidad es: {super_bajo['identidad']}")

  elif opcion == "D":
    # Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
    suma_pesos_masculinos = 0
    cantidad_superheroes_masculinos = 0
    for superheroe in lista_personajes:
      if superheroe["genero"] == "M":
        suma_pesos_masculinos += float(superheroe["peso"])
        cantidad_superheroes_masculinos += 1
    if cantidad_superheroes_masculinos > 0:
      promedio_peso_masculino = suma_pesos_masculinos / cantidad_superheroes_masculinos
      print(f"Promedio de peso de los superhéroes masculinos: {promedio_peso_masculino:.2f} kg")
    else:
      print("No hay superhéroes de género masculino en la lista")

  elif opcion == "E":
    # Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superheroínas de género femenino
    fuerza_promedio_heroinas = 0
    cantidad_heroinas = 0
    for superheroe in lista_superheroes:
      if superheroe["genero"] == "F":
        fuerza_promedio_heroinas += float(superheroe["fuerza"])
        cantidad_heroinas += 1
    if cantidad_heroinas > 0:
      fuerza_promedio_heroinas /= cantidad_heroinas
      print(f"Superhéroes con fuerza superior a la promedio de las superheroínas:")
      print("+--------------------+-----------+")
      print(f"| Nombre\t     | Peso      |")
      print("+--------------------+-----------+")
      for superheroe in lista_personajes:
        if float(superheroe["fuerza"]) > fuerza_promedio_heroinas:
          print(f"| {superheroe['nombre']:18} | {float(superheroe['peso']):6.2f} kg |")
      print("+--------------------+-----------+")
    else:
      print("No hay supeheroinas en la lista")
  elif opcion == "F":

    # Salir del menú
    bandera = False