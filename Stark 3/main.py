import re
from data_stark import lista_personajes

def stark_normalizar_datos(lista_heroes:list):
  """
  Normaliza los datos de la lista de héroes.

  Parámetros:
    lista_heroes: Lista de héroes.

  Devuelve:
    True si se normalizaron datos, False en caso contrario.
  """
  bandera_normalizados = False
  if(len(lista_heroes) > 0):
    bandera_normalizados = True
    for heroes in lista_heroes:
        for clave, valor in heroes.items():
            if clave == "fuerza":
                heroes[clave] = int(valor)
                
            elif clave == "altura" or clave == "peso":
                heroes[clave] = float(valor)
                
            elif clave == "color_ojos" or clave == "color_pelo" or clave == "inteligencia":
                heroes[clave] = str(valor).capitalize()
    print("Datos normalizados.")
  else:
      print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente")


  return bandera_normalizados


def obtener_dato(heroe:dict, clave:str):
  """
  Obtiene el valor de una key de un héroe.

  Parámetros:
    heroe: Héroe.
    key: Key del héroe.

  Devuelve:
    El valor de la key.
  """

  if heroe and clave in heroe:
    return heroe[clave]
  else:
    return False


def obtener_nombre(heroe:dict):
  """
  Obtiene el nombre de un héroe.

  Parámetros:
    heroe: Héroe.

  Devuelve:
    El nombre del héroe.
  """

  return f"Nombre: {obtener_dato(heroe, 'nombre')}"

def obtener_maximo(lista_heroes:list, clave:str)->str:
  """
  Obtiene el valor máximo de una key de una lista de héroes.

  Parámetros:
    lista_heroes: Lista de héroes.
    key: Key de los héroes.

  Devuelve:
    El valor máximo de la key.
  """
  if isinstance(lista_heroes, list):
    if len(lista_heroes) == 0:
      imprimir_dato("La lista está vacía")
    else:
      bandera = True
      valor_maximo = 0
      heroe_maximo = 0
    
      for heroe in lista_heroes:
          for clave_valor in heroe:
              if bandera == True and clave_valor == clave:
                  valor_maximo = heroe.get(clave)
                  heroe_maximo = heroe.get('nombre')
                  bandera = False
              elif clave_valor == clave and valor_maximo <= heroe.get(clave):
                  valor_maximo = heroe.get(clave)
                  heroe_maximo = heroe.get('nombre')
      
  else:
    imprimir_dato("No es una lista")
    heroe_maximo = ""

  return heroe_maximo

def obtener_minimo(lista_heroes:list, clave:str):
  """
  Obtiene el valor mínimo de una key de una lista de héroes.

  Parámetros:
    lista_heroes: Lista de héroes.
    key: Key de los héroes.

  Devuelve:
    El valor mínimo de la key.
  """
  
  if isinstance(lista_heroes, list):
    if len(lista_heroes) == 0:
      imprimir_dato("La lista está vacía")
      heroe_minimo = ""
    else:
      bandera = True
      valor_minimo = 0
      heroe_minimo = 0
      for heroe in lista_heroes:
          for clave_valor in heroe:
              if bandera == True and clave_valor == clave:
                  valor_minimo = heroe.get(clave)
                  heroe_minimo = heroe.get('nombre')
                  bandera = False
              elif clave_valor == clave and valor_minimo >= heroe.get(clave):
                  valor_minimo = heroe.get(clave)
                  heroe_minimo = heroe.get('nombre')

  else:
    imprimir_dato("No es una lista")
    heroe_minimo = ""

  return heroe_minimo

def obtener_dato_cantidad(lista_heroes:list, valor, clave:str):
  """
  Obtiene una lista de héroes con un valor específico de una key.

  Parámetros:
    lista_heroes: Lista de héroes.
    valor: Valor de la key.
    key: Key de los héroes.

  Devuelve:
    La lista de héroes con el valor especificado.
  """

  if len(lista_heroes) != 0:
    lista_heroes_con_valor = []
    for heroe in lista_heroes:
      if clave in heroe and obtener_dato(heroe, clave) == valor:
        lista_heroes_con_valor.append(heroe)
  else:
     lista_heroes_con_valor = False
     imprimir_dato("Lista vacía")
     
  if len(lista_heroes_con_valor) == 0:
     lista_heroes_con_valor = False
     print(f"No hay superheroes de {clave} {valor} en la lista")

  return lista_heroes_con_valor     

def obtener_nombre_y_dato(heroe:dict, clave:str):
  """
  Obtiene el nombre y un dato de un héroe.

  Parámetros:
    heroe: Héroe.
    key: Key del héroe.

  Devuelve:
    Un string con el nombre y el dato del héroe.
  """

  if heroe and clave in heroe:
    return f"Nombre: {obtener_dato(heroe, 'nombre')} | {clave}: {obtener_dato(heroe, clave)}"
  else:
    return False



def mostrar_superheroes_agrupados_por_genero(superheroes_por_genero:dict):
  print("+--------------------+-------------------------------+---------------+--------+--------+--------+-------------------------+---------------------+--------+--------------+")
  print(f"| Nombre\t     | Identidad\t\t     | Empresa\t     | Altura | Peso   | Género | Ojos\t\t\t  | Pelo\t\t| Fuerza | Inteligencia |")
  print("+--------------------+-------------------------------+---------------+--------+--------+--------+-------------------------+---------------------+--------+--------------+")
  for genero in superheroes_por_genero:
    for superheroe in superheroes_por_genero[genero]:
      print(f"| {superheroe['nombre']:18} | {superheroe['identidad']:29} | {superheroe['empresa']:10} | \
{float(superheroe['altura']):6.2f} | {float(superheroe['peso']):6.2f} | {superheroe['genero']:6} | \
{superheroe['color_ojos']:23} | {superheroe['color_pelo']:19} | {superheroe['fuerza']:6} | \
{superheroe['inteligencia']:12} |")

def stark_imprimir_heroes(lista_heroes:list):
  """
  Imprime la información de una lista de héroes.

  Parámetros:
    lista_heroes: Lista de héroes.

  """
  # if(len(lista_heroes) <= 0 ): 
  if(lista_heroes is None):
    imprimir_dato("Lista vacía")
  else:
    if lista_heroes == 0:
      pass
    else:   
      if opcion == 10 or opcion == 11:
        mostrar_superheroes_agrupados_por_genero(lista_heroes)
      else:
        for superheroe in lista_heroes:
          if opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6:
            imprimir_dato(superheroe)

def sumar_dato_heroe(lista_heroes:list, clave:str):
  """
  Suma los valores de una key de todos los héroes.

  Parámetros:
    lista_heroes: Lista de héroes.
    key: Key de los héroes.

  Devuelve:
    La suma de los valores de la key.
  """

  suma = 0
  for heroe in lista_heroes:
    if clave in heroe:
      suma += int(heroe[clave])
  return suma


def dividir(dividendo:int, divisor:int):
  """
  Divide dos números.

  Parámetros:
    dividendo: Dividendo.
    divisor: Divisor.

  Devuelve:
    El resultado de la división.
  """

  if divisor == 0:
    return False
  else:
    return dividendo / divisor


def calcular_promedio(lista_heroes:list, clave:str):
  """
  Calcula el promedio de los valores de una key de todos los héroes.

  Parámetros:
    lista_heroes: Lista de héroes.
    key: Key de los héroes.

  Devuelve:
    El promedio de los valores de la key.
  """
  if isinstance(lista_heroes, list):
    if len(lista_heroes) == 0:
      imprimir_dato("Lista vacía")

    suma = sumar_dato_heroe(lista_heroes, clave)
    promedio = 0
    if suma == 0:
      promedio = 0
    else:
      promedio = suma / len(lista_heroes)
  else:
    promedio = ""
  return promedio


def mostrar_promedio_dato(lista_heroes:list, clave:str):
  """
  Imprime el promedio de los valores de una key de todos los héroes.

  Parámetros:
    lista_heroes: Lista de héroes.
    key: Key de los héroes.
  """

  promedio = calcular_promedio(lista_heroes, clave)
  if promedio:
    print(f"El promedio de {clave} es: {promedio}")
  else:
    print(f"No hay datos de {clave} para calcular el promedio.")

def imprimir_dato(texto:str):
  """
  Imprime el menú de opciones.
  """

  print(texto, end="")

def imprimir_menu(texto:str):
  """
  Imprime el menú de opciones.
  """

  print(texto)

def validar_entero(numero):
  """
  Valida que un string sea un número entero.

  Parámetros:
    numero: String a validar.

  Devuelve:
    True si el string es un número entero, False en caso contrario.
  """

  expresion_regular = r"^[0-9]+$"
  match = re.match(expresion_regular, numero)
  return match is not None


def stark_menu_principal(lista_heroes:list):
  """
  Encargado de la ejecución principal del programa.

  Parámetros:
    lista_heroes: Lista de héroes.

  Devuelve:
    El valor de la opción seleccionada por el usuario.
  """

  opcion = None
  menu ='''
Menú de opciones:\n1. Normalizar datos\n2. Listar héroes de género NB\n3. Obtener el superhéroe más alto de género F\n\
4. Obtener el superhéroe más alto de género M\n5. Obtener el superhéroe más débil de género M\n6. Obtener el superhéroe más débil de género NB\n\
7. Obtener la fuerza promedio de los superhéroes de género NB\n8. Contar el número de superhéroes por color de ojos\n\
9. Contar el número de superhéroes por color de pelo\n10. Listar superhéroes agrupados por color de ojos\n11. Listar superhéroes agrupados por tipo de inteligencia\n12. Salir
        '''
  while opcion is None:
  
    imprimir_menu(menu)
    opcion_str = input("Ingrese una opción: ")
    if validar_entero(opcion_str):
      opcion = int(opcion_str.lower().strip())
    else:
      print("Opción inválida.")
  return opcion

def cantidad_superheroes_por_tipo(lista_personajes:list,tipo:str)->int:
  """Determina cuántos superhéroes tienen cada tipo."""
  cantidad = 0
  cantidad_por_color = {}

  for superheroe in lista_personajes:
    color_tipo = superheroe[tipo]

    if color_tipo not in cantidad_por_color:
      cantidad_por_color[color_tipo] = 0
    cantidad_por_color[color_tipo] += 1
  for color_tipo, cantidad in cantidad_por_color.items():
    if color_tipo != "":
      if cantidad > 1:
        print(f"Hay {cantidad} superhéroes con género {tipo}: {color_tipo}")
      else:
        print(f"Hay {cantidad} superhéroe con género {tipo}: {color_tipo}")
  return cantidad

def superheroes_agrupados_por_tipo(lista_personajes:list,tipo:str)->dict:
  """Lista todos los superhéroes agrupados por tipo."""
  superheroes_por_tipo = {}
  for superheroe in lista_personajes:
    if superheroe[tipo] != "":
      if superheroe[tipo] not in superheroes_por_tipo:
        superheroes_por_tipo[superheroe[tipo]] = []
      superheroes_por_tipo[superheroe[tipo]].append(
          superheroe)

  return superheroes_por_tipo

def stark_marvel_app(lista_heroes:list):
  """
  Encargado de resolver los puntos del desafío.

  Parámetros:
    lista_heroes: Lista de héroes.
  """

  global opcion
  bandera_normalizacion = False
  while True:
    opcion = stark_menu_principal(lista_heroes)

    if opcion == 1:
      bandera_normalizacion = stark_normalizar_datos(lista_heroes)
        
    elif opcion == 2:
      if bandera_normalizacion:
        lista_heroes_nb = obtener_dato_cantidad(lista_heroes, "NB", "género")
        if lista_heroes_nb:
          stark_imprimir_heroes(lista_heroes_nb)   
      else:
        print("Por favor primero normalice los datos") 

    elif opcion == 3:
      if bandera_normalizacion:
        superheroe_mas_alto_f = obtener_dato_cantidad(lista_heroes, "F","genero")
        if superheroe_mas_alto_f:
          mas_alto_f = "El superhéroe más alto de género F es: " + obtener_maximo(superheroe_mas_alto_f, "altura")
          stark_imprimir_heroes(mas_alto_f)
        
      else:
        print("Por favor primero normalice los datos")

    elif opcion == 4:
      if bandera_normalizacion:
        superheroe_mas_alto_m = obtener_dato_cantidad(lista_heroes, "M", "genero")
        if superheroe_mas_alto_m:
          mas_alto_m = "El superhéroe más alto de género M es: " + obtener_maximo(superheroe_mas_alto_m,"altura")
          stark_imprimir_heroes(mas_alto_m)
      
      else:
        print("Por favor primero normalice los datos")

    elif opcion == 5:
      if bandera_normalizacion:
        superheroe_mas_debil_m = obtener_dato_cantidad(lista_heroes, "M", "genero")
        mas_debil_m = "El superhéroe más débil de género M es: " + obtener_minimo(superheroe_mas_debil_m, "fuerza")
        stark_imprimir_heroes(mas_debil_m)
      else:
        print("Por favor primero normalice los datos")

    elif opcion == 6:
      if bandera_normalizacion:
        superheroe_mas_debil_nb = obtener_dato_cantidad(lista_heroes, "NB", "genero")
        if superheroe_mas_debil_nb:
          mas_debil_m = "El superhéroe más débil de género NB es: " + obtener_minimo(superheroe_mas_debil_nb, "fuerza")
          stark_imprimir_heroes(mas_debil_m)
      else:
        print("Por favor primero normalice los datos")

    elif opcion == 7:
      if bandera_normalizacion:
        lista_fuerza_promedio_nb = obtener_dato_cantidad(lista_heroes, "NB", "genero")
        if lista_fuerza_promedio_nb:
          fuerza_promedio_nb = "La fuerza promedio de los superhéroes de género NB es: " + calcular_promedio(lista_fuerza_promedio_nb, "fuerza")
          stark_imprimir_heroes(fuerza_promedio_nb)
      else:
        print("Por favor primero normalice los datos")



    elif opcion == 8:
      if bandera_normalizacion:
        cantidad_superheroes_por_tipo(lista_heroes,"color_ojos")
      else:
        print("Por favor primero normalice los datos")
      
    elif opcion == 9:
      if bandera_normalizacion:
        cantidad_superheroes_por_tipo(lista_heroes,"color_pelo")
      else:
        print("Por favor primero normalice los datos")

    elif opcion == 10:
      if bandera_normalizacion:
        superheroes_agrupados_por_color_ojos = superheroes_agrupados_por_tipo(lista_heroes,"color_ojos")

   
        stark_imprimir_heroes(superheroes_agrupados_por_color_ojos)
      else:
        print("Por favor primero normalice los datos")
    
    elif opcion == 11:
        if bandera_normalizacion:  
        
          superheroes_agrupados_por_inteligencia = superheroes_agrupados_por_tipo(lista_heroes,"inteligencia")
          
          stark_imprimir_heroes(superheroes_agrupados_por_inteligencia)
        else:
          print("Por favor primero normalice los datos")
    elif opcion == 12:
       
        print("Saliendo de la aplicación.")
        break
    else:
      print("Opción incorrecta")

def main():
  """
  Programa principal.
  """

stark_marvel_app(lista_personajes)

