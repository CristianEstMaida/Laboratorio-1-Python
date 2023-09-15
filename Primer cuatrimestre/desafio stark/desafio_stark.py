from data_stark import lista_personajes

def opcion_a():
    '''Recorre la lista imprimiendo por consola todos los datos de cada superhéroe'''

    print("+--------------------+-------------------------------+---------------+--------+--------+--------+-------------------------+---------------------+--------+--------------+")
    print(f"| Nombre\t     | Identidad\t\t     | Empresa\t     | Altura | Peso   | Género | Ojos\t\t\t  | Pelo\t\t| Fuerza | Inteligencia |")
    print("+--------------------+-------------------------------+---------------+--------+--------+--------+-------------------------+---------------------+--------+--------------+")
    for superheroe in lista_personajes:
        print(f"| {superheroe['nombre']:18} | {superheroe['identidad']:29} | {superheroe['empresa']:10} | {float(superheroe['altura']):6.2f} | {float(superheroe['peso']):6.2f} | {superheroe['genero']:6} | {superheroe['color_ojos']:23} | {superheroe['color_pelo']:19} | {superheroe['fuerza']:6} | {superheroe['inteligencia']:12} |" )
        
    print("+--------------------+-------------------------------+---------------+--------+--------+--------+-------------------------+---------------------+--------+--------------+")
        

def opcion_b():
  '''Recorre la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)'''
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
    print("+--------------+--------+")
    print(f"| Identidad    | Peso   |")
    print("+--------------+--------+")
    for superheroe in super_fuertes:
      print(f"| {superheroe['identidad']} | {float(superheroe['peso']):.2f} |")
    print("+--------------+--------+")
  else:
    print("Superhéroe con mayor fuerza:")
    print("+--------------+--------+")
    print(f"| Identidad    | Peso   |")
    print("+--------------+--------+")
    print(f"| {super_fuertes[0]['identidad']} | {float(super_fuertes[0]['peso']):.2f} |")
    print("+--------------+--------+")

def opcion_c():
  '''Recorre la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)'''
  minimo_altura = None
  super_bajo = None
  for superheroe in lista_personajes:
    altura = float(superheroe["altura"])
    if minimo_altura == None or altura < minimo_altura:
      minimo_altura = altura
      super_bajo = superheroe
  print(f"Superhéroe más bajo: {super_bajo['nombre']}")
  print(f"Identidad: {super_bajo['identidad']}")

def opcion_d():
  '''Recorre la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)'''
  suma_pesos_masculinos = 0
  cantidad_superheroes_masculinos = 0
  for superheroe in lista_personajes:
    if superheroe["genero"] == "M":
      suma_pesos_masculinos += float(superheroe["peso"])
      cantidad_superheroes_masculinos += 1
  promedio_peso_masculino = suma_pesos_masculinos / cantidad_superheroes_masculinos
  print(f"Promedio de peso de los superhéroes masculinos: {promedio_peso_masculino:.2f}")

def opcion_e():
  '''Recorre la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superheroínas de género femenino'''
  fuerza_promedio_heroinas = 0
  cantidad_heroinas = 0
  for superheroe in lista_personajes:
    if superheroe["genero"] == "F":
      fuerza_promedio_heroinas += float(superheroe["fuerza"])
      cantidad_heroinas += 1
  fuerza_promedio_heroinas /= cantidad_heroinas
  print(f"Superhéroes con fuerza superior a la promedio de las superheroínas:")
  print("+--------------------+--------+")
  print(f"| Nombre\t     | Peso   |")
  print("+--------------------+--------+")
  for superheroe in lista_personajes:
    if float(superheroe["fuerza"]) > fuerza_promedio_heroinas:
      print(f"| {superheroe['nombre']:18} | {float(superheroe['peso']):6.2f} |")
  print("+--------------------+--------+")

def mostrar_menu():
  """Muestra el menú de opciones."""
  print("**Menú Desafío Stark #01**")
  print("(A) Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe")
  print("(B) Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)")
  print("(C) Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)")
  print("(D) Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)")
  print("(E) Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superheroínas de género femenino")
  print("(F) Salir")

def procesar_opcion(opcion:int, bandera:bool) -> bool:
    """Procesa la opción elegida por el usuario."""
    match opcion:
      case "A":
        opcion_a()      
      case "B":
        opcion_b()
      case "C":
        opcion_c()
      case "D":
        opcion_d()
      case "E":
        opcion_e()
      case "F":
        print("Saliendo del menú...")
        bandera = False    
      case _:
        print("Opción no válida")
    return bandera

bandera = True
while bandera == True:
  mostrar_menu()
  opcion = input("Ingrese una opción: ").upper()

  bandera = procesar_opcion(opcion, bandera)
  
