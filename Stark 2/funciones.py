from data_stark import lista_personajes
# Funciones

def mostrar_lista(lista:list):
    for valor in lista:
        print(valor)

def mostrar_valor(mensaje:str, valor:int=""):
    print(f"{mensaje} {valor} ")

def superheroes(genero:str)->dict:
  """Recorre la lista imprimiendo por consola el nombre de cada superhéroe de género NB."""
  bandera = False
  lista_superheroe_nb = {}
  for superheroe in lista_personajes:
    if superheroe["genero"] == genero:
      lista_superheroe_nb.append(superheroe["nombre"])
      bandera = True
  if bandera is False:
    print(f"No hay superheroes de genero {genero} en la lista")
  return lista_superheroe_nb


def superheroe_mas_alto(genero:str)->str:
  """Determina cuál es el superhéroe más alto según su género."""
  superheroe_mas_alto = None
  lista_superheroe_alto = None
  bandera = False
  for superheroe in lista_personajes:
    if superheroe["genero"] == genero:
      if superheroe_mas_alto is None or float(superheroe["altura"]) > float(superheroe_mas_alto):
        bandera = True
        superheroe_mas_alto = float(superheroe["altura"])
        lista_superheroe_alto = superheroe["nombre"]
  if bandera is False:
    print(f"No hay superheroes de genero {genero} en la lista")
  return lista_superheroe_alto

def superheroe_mas_debil(genero:str)->str:
  """Determina cuál es el superhéroe más débil según su género."""
  superheroe_mas_debil = None
  lista_superheroe_debil = None
  bandera = False
  for superheroe in lista_personajes:
    if superheroe["genero"] == genero:
      if superheroe_mas_debil is None or int(superheroe["fuerza"]) < int(superheroe_mas_debil):
        bandera = True
        superheroe_mas_debil = int(superheroe["fuerza"])
        lista_superheroe_debil = superheroe["nombre"]
  if bandera is False:
    print(f"No hay superheroes de genero {genero} en la lista")
  return lista_superheroe_debil

def fuerza_promedio_nb()->float:
  """Determina la fuerza promedio de los superhéroes de género NB."""
  fuerza_total = 0
  superheroes_nb_count = 0
  for superheroe in lista_personajes:
    if superheroe["genero"] == "NB":
      fuerza_total += int(superheroe["fuerza"])
      superheroes_nb_count += 1
  if superheroes_nb_count != 0:  
    print(f"La fuerza promedio es {fuerza_total / superheroes_nb_count}")
    fuerza_promedio_nb = fuerza_total / superheroes_nb_count
  else:
    print("No hay superheroes no binarios en la lista")
    fuerza_promedio_nb = 0
  return fuerza_promedio_nb

def cantidad_superheroes_por_clave(clave:str)->int:
  """Determina cuántos superhéroes tienen cada tipo de color de ojos."""
  cantidad = 0
  cantidad_por_color = {}

  for superheroe in lista_personajes:
    color_clave = superheroe[clave]
    if color_clave not in cantidad_por_color:
      cantidad_por_color[color_clave] = 0
    cantidad_por_color[color_clave] += 1
    color_clave = ""
    
  for color_clave, cantidad in cantidad_por_color.items():
    if color_clave != "":
      if cantidad > 1:
        if clave == "color_ojos":
          print(f"Hay {cantidad} superhéroes con color de ojos: {color_clave}")
        elif clave == "color_pelo":
          print(f"Hay {cantidad} superhéroes con color de pelo: {color_clave}")
        else:  
          print(f"Hay {cantidad} superhéroes con clave {clave}: {color_clave}")
      else:
        if clave == "color_ojos":
          print(f"Hay {cantidad} superhéroe con color de ojos: {color_clave}")
        elif clave == "color_pelo":
          print(f"Hay {cantidad} superhéroe con color de pelo: {color_clave}")
        else:
          print(f"Hay {cantidad} superhéroe con clave {clave}: {color_clave}")
  return cantidad

def superheroes_agrupados_por_genero(genero:str)->dict:
  """Lista todos los superhéroes agrupados por genero."""
  superheroes_por_tipo = {}
  for superheroe in lista_personajes:
    if superheroe[genero] != "":
      if superheroe[genero] not in superheroes_por_tipo:
        superheroes_por_tipo[superheroe[genero]] = []
      
      superheroes_por_tipo[superheroe[genero]].append(
        superheroe)
  return superheroes_por_tipo

def mostrar_superheroes_agrupados_por_genero(superheroes_por_genero:dict):
  
  print("+--------------------+-------------------------------+---------------+--------+--------+--------+-------------------------+---------------------+--------+--------------+")
  print(f"| Nombre\t     | Identidad\t\t     | Empresa\t     | Altura | Peso   | Género | Ojos\t\t\t  | Pelo\t\t| Fuerza | Inteligencia |")
  print("+--------------------+-------------------------------+---------------+--------+--------+--------+-------------------------+---------------------+--------+--------------+")
  for genero in superheroes_por_genero:
    for superheroe in superheroes_por_genero[genero]:
      if superheroes_por_genero[genero] != "":
        print(f"| {superheroe['nombre']:18} | {superheroe['identidad']:29} | {superheroe['empresa']:10} | \
{float(superheroe['altura']):6.2f} | {float(superheroe['peso']):6.2f} | {superheroe['genero']:6} | \
{superheroe['color_ojos']:23} | {superheroe['color_pelo']:19} | {superheroe['fuerza']:6} | \
{superheroe['inteligencia']:12} |")

def stark_normalizar_datos():
  """
  Normaliza los datos de la lista de héroes.

  Parámetros:
    lista_heroes: Lista de héroes.
  """

  if(len(lista_personajes) > 0):
    for heroes in lista_personajes:
        for clave, valor in heroes.items():
            if clave == "fuerza":
                heroes[clave] = int(valor)
                
            elif clave == "altura" or clave == "peso":
                heroes[clave] = float(valor)
                
            elif clave == "color_ojos" or clave == "color_pelo" or clave == "inteligencia":
                heroes[clave] = str(valor).capitalize()
  else:
      print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")


def procesar_opcion(opcion:int, bandera:bool)->bool:
#   """Procesa la opción elegida por el usuario."""
    stark_normalizar_datos()
    match opcion:  
      case "1":
        superheroes_nb = superheroes("NB")
        if superheroes_nb is not None:
          mostrar_lista(superheroes_nb)
      case "2":
        superheroe_mas_alto_f = superheroe_mas_alto("F")
        mostrar_valor("El superhéroe más alto de género F es: ", superheroe_mas_alto_f)
      case "3":
        superheroe_mas_alto_m = superheroe_mas_alto("M")
        mostrar_valor("El superhéroe más alto de género M es: ", superheroe_mas_alto_m)
      case "4":
        superheroe_mas_debil_m = superheroe_mas_debil("M")
        mostrar_valor("El superhéroe más débil de género M es: ", superheroe_mas_debil_m)
      case "5":
        superheroe_mas_debil_nb = superheroe_mas_debil("NB")
        if superheroe_mas_debil_nb is not None:
          mostrar_valor("El superhéroe más débil de género NB es: ", superheroe_mas_debil_nb)
      case "6":
        fuerza_promedio_nb()
      case "7":
        cantidad_superheroes_por_clave("color_ojos")
      case "8":
        cantidad_superheroes_por_clave("color_pelo")
      case "9":
        superheroes_agrupados_por_color_ojos = superheroes_agrupados_por_genero("color_ojos")
        mostrar_superheroes_agrupados_por_genero(superheroes_agrupados_por_color_ojos)
      case "10":
        superheroes_agrupados_por_tipo_inteligencia = superheroes_agrupados_por_genero("inteligencia")
        mostrar_superheroes_agrupados_por_genero(superheroes_agrupados_por_tipo_inteligencia)
      case "11":
        print("Saliendo del menú...")
        bandera = False    
      case _:
        print("Opción no válida")
    return bandera

def mostrar_menu():
  # Menú
  """Muestra el menú de opciones."""
  print("\n\n**Menú Desafío Stark #02**")
  print("Menú de informes")
  print("1. Superheroes NB")
  print("2. Superheroe más alto F")
  print("3. Superheroe más alto M")
  print("4. Superheroe más débil M")
  print("5. Superheroe más débil NB")
  print("6. Fuerza promedio NB")
  print("7. Cantidad superhéroes por color de ojos")
  print("8. Cantidad superhéroes por color de pelo")
  print("9. Superheroes agrupados por color de ojos")
  print("10. Superheroes agrupados por tipo de inteligencia")
  print("11. Salir")