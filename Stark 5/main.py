import json
import os
import re

def imprimir_menu_desafio_5():
  """
  Imprime el menú de opciones por pantalla.

  Parámetros:
    None

  Retorna:
    None
  """

  imprimir_dato("Menú de opciones")
  imprimir_dato("A. Listar superhéroes de género M")
  imprimir_dato("B. Listar superhéroes de género F")
  imprimir_dato("C. Mostrar superhéroe más alto de género M")
  imprimir_dato("D. Mostrar superhéroe más alto de género F")
  imprimir_dato("E. Mostrar superhéroe más bajo de género M")
  imprimir_dato("F. Mostrar superhéroe más bajo de género F")
  imprimir_dato("G. Mostrar altura promedio de superhéroes de género M")
  imprimir_dato("H. Mostrar altura promedio de superhéroes de género F")
  imprimir_dato("I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
  imprimir_dato("J. Mostrar cantidad de superhéroes por color de ojos")
  imprimir_dato("K. Mostrar cantidad de superhéroes por color de pelo")
  imprimir_dato("L. Mostrar cantidad de superhéroes por tipo de inteligencia")
  imprimir_dato("M. Listar superhéroes agrupados por color de ojos")
  imprimir_dato("N. Listar superhéroes agrupados por color de pelo")
  imprimir_dato("O. Listar superhéroes agrupados por tipo de inteligencia")
  imprimir_dato("Z. Salir")

def stark_menu_principal_desafio_5():
  """
  Imprime el menú de opciones y le pide al usuario que ingrese la letra de una de las opciones elegidas.

  Parámetros:
    None

  Retorna:
    letra: Letra de la opción elegida.
  """

  imprimir_menu_desafio_5()
  letra = input("Ingrese la letra de la opción elegida: ")

  while not re.match("[A-Z]", letra):
    print("Opción inválida. Ingrese una letra entre A y Z: ")
    letra = input()

  return letra

def stark_marvel_app_5(data):
  """
  Ejecuta el programa principal.

  Parámetros:
    data: Lista de superhéroes.

  Retorna:
    None
  """
  
  letra = stark_menu_principal_desafio_5()

  while letra != "Z":
    if letra == "A":
      imprimir_superheroes_genero(data, "M")
      stark_guardar_heroe_genero(data, "M")
    elif letra == "B":
      imprimir_superheroes_genero(data, "F")
      stark_guardar_heroe_genero(data, "F")
    elif letra == "C":
      #print("*** opcion C ***")
      #if not stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, 'altura', 'maximo','M'):
          #print("error en opcion C")
      stark_calcular_imprimir_guardar_heroe_genero(data, "M","altura","maximo")
    elif letra == "D":
      stark_calcular_imprimir_guardar_heroe_genero(data, "F","altura","maximo")
    elif letra == "E":
      
      stark_calcular_imprimir_guardar_heroe_genero(data, "M","altura","minimo")
      stark_guardar_heroe_genero(data, "M")
    elif letra == "F":
      
      stark_calcular_imprimir_guardar_heroe_genero(data, "F","altura","minimo")
      stark_guardar_heroe_genero(data, "F")
    elif letra == "G":
      promedio_altura_M = stark_calcular_imprimir_guardar_promedio_altura_genero(data, "M")
      nombre_archivo = f"promedio_altura_genero_M.csv"
      guardar_archivo(nombre_archivo, promedio_altura_M)
      print(f"El promedio de altura de los superhéroes de género M es: {float(promedio_altura_M)/100:.2} m")
    elif letra == "H":
      promedio_altura_F = stark_calcular_imprimir_guardar_promedio_altura_genero(data, "F")
      nombre_archivo = f"promedio_altura_genero_F.csv"
      guardar_archivo(nombre_archivo, promedio_altura_F)
      print(f"El promedio de altura de los superhéroes de género M es: {float(promedio_altura_F)/100:.2} m")
    elif letra == "I":
      stark_mostrar_data_archivo_heroes_calculo_numero_genero()
    elif letra == "J":
      stark_calcular_cantidad_por_tipo(data,"color_ojos")      
    elif letra == "K":
      stark_calcular_cantidad_por_tipo(data,"color_pelo")
    elif letra == "L":
      stark_calcular_cantidad_por_tipo(data,"inteligencia")
    elif letra == "M":
      stark_listar_heroes_por_dato(data,"color_ojos")
    elif letra == "N":
      stark_listar_heroes_por_dato(data,"color_pelo")
    elif letra == "O":
      stark_listar_heroes_por_dato(data,"inteligencia")
    elif letra == "Z":
      print("Hasta luego!")
    else:
      print("Opción inválida.")
    letra = stark_menu_principal_desafio_5()

  print("Hasta luego!")

def stark_mostrar_data_archivo_heroes_calculo_numero_genero() -> bool:
    '''
    Informa cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    Retorna: False en caso de haber error en alguno de los archivos. True en caso contrario
    '''
    retorno = True

    # C: heroes_maximo_altura_M.csv
    if not imprimir_data_archivo_heroes_calculo_numero_genero("heroes_maximo_M_altura.csv"):
        retorno = False

    # D: heroes_maximo_altura_F.csv
    if not imprimir_data_archivo_heroes_calculo_numero_genero("heroes_maximo_F_altura.csv"):
        retorno = False

    # E: heroes_minimo_altura_M.csv
    if not imprimir_data_archivo_heroes_calculo_numero_genero("heroes_minimo_M_altura.csv"):
        retorno = False

    # E: heroes_minimo_altura_F.csv
    if not imprimir_data_archivo_heroes_calculo_numero_genero("heroes_minimo_F_altura.csv"):
        retorno = False

    return retorno

def imprimir_data_archivo_heroes_calculo_numero_genero(nombre_archivo) -> bool:
    '''
    imprime el contenido del archivo o un mensaje de error
    Recibe: el nombre del archivo con sus datos
    Retorna: True o False    
    '''
    datos = leer_archivo_heroes_calculo_numero_genero(nombre_archivo) # extraigo contenido del archivo
    if error_data_archivo_heroes_calculo_genero(datos): # si hay un error se imprime, y se retorna False
        imprimir_dato(datos) 
        return False
    else: # si no hay error se informa lo correspondiente, y se retorna True
        datos_salida = f"En {nombre_archivo} se encontro la siguiente info: {interpretar_data_archivo_heroes_calculo_numero_genero(datos)}"
        imprimir_dato(datos_salida)
        return True



def error_data_archivo_heroes_calculo_genero(cadena_error):
    '''
    Verifica si cadena_error cumple con el patron r"Error: Aun no se ha creado (.+)"
    Retorna: True o False
    '''
    
    patron_formato_error = r"Error: Aun no se ha creado (.+)"
    if re.match(patron_formato_error, cadena_error):
        return True
    return False

def interpretar_data_archivo_heroes_calculo_numero_genero(cadena_data:str) -> str:
    '''
    Evalua el contenido de cadena_data para verificar si se recibio contenido o un mensaje de error
    Recibe: una cadena con formato especifico
    Retorna: la informacion extraida del formato o un mensaje de error
    '''

    # patrones de regex
    patron_formato_datos = r"[A-Za-z ]+: Nombre: ([A-Za-z -]+) \| [A-Za-z_]+: [0-9\.]+"
    

    if re.match(patron_formato_datos, cadena_data): # en caso que se haya abierto el archivo y recibido sus datos
        matches = re.match(patron_formato_datos, cadena_data)
        nombre_data = matches.group(1)
        return f"Nombre: {nombre_data}"    
    else: # en caso que no
        return cadena_data

def leer_archivo_heroes_calculo_numero_genero(nombre_archivo:str) -> str:
    '''
    Recibe: el nombre/la direccion de un archivo de tipo heroes_calculo_numero_genero junto a su extension
    Abre el archivo en modo lectura. Recupera la data del archivo la cual inicialmente sera un string del siguiente formato: "Mayor altura: Nombre: Gamora | Altura: 183.65"
    Retorna: la cadena formateada

    '''
    # directorio_archivo = armar_directorio_stark_5(nombre_archivo)
    if os.path.exists(nombre_archivo):
    # if os.path.exists(directorio_archivo): # verifica que el archivo exista antes de intentar leerlo
        with open(nombre_archivo, "r") as archivo:
        # with open(directorio_archivo, 'r') as archivo:
            data = archivo.read()
            return data # si existe retorna su contenido
    return f"Error: Aun no se ha creado {nombre_archivo}" # si no existe retorna mensaje de error

def leer_archivo(nombre_archivo):
  """
  Lee un archivo JSON y lo devuelve como una lista de diccionarios.

  Args:
    nombre_archivo: Nombre del archivo JSON.

  Returns:
    Lista de diccionarios.
  """

  with open(nombre_archivo, "r") as f:
    datos = json.load(f)

  return datos

def guardar_archivo(nombre_archivo, contenido):
  """
  Guarda un archivo con el nombre y contenido especificados.

  Args:
    nombre_archivo: El nombre del archivo a guardar.
    contenido: El contenido del archivo a guardar.

  Returns:
    True si se guardó el archivo correctamente, False en caso contrario.
  """

  # if os.path.exists(nombre_archivo):
  #   print(f'Error al crear el archivo: {nombre_archivo}')
  #   return False

  with open(nombre_archivo, 'w+') as archivo:
    archivo.write(contenido)
  return True

def capitalizar_palabras(cadena):
  """
  Capitaliza todas las palabras de una cadena.

  Args:
    cadena: La cadena a capitalizar.

  Returns:
    La cadena capitalizada.
  """
  return cadena.capitalize()
  # palabras = cadena.split()
  # for palabra in palabras:
  #   palabra = palabra[0].upper() + palabra[1:]
  # return ' '.join(palabras)

def obtener_nombre_capitalizado(heroe):
  """
  Obtiene el nombre capitalizado de un héroe.

  Args:
    héroe: El diccionario que representa al héroe.

  Returns:
    El nombre capitalizado del héroe.
  """

  return f'Nombre: {capitalizar_palabras(heroe["nombre"])}'

def obtener_nombre_y_dato(heroe, clave):
  """
  Obtiene el nombre y dato de un héroe.

  Args:
    héroe: El diccionario que representa al héroe.
    key: La key del héroe a imprimir.

  Returns:
    El nombre y dato del héroe.
  """
  
  return f'Nombre: {heroe["nombre"]} | Clave: {clave}'

def es_genero(heroe, genero):
  """
  Determina si un héroe tiene el género especificado.

  Args:
    héroe: El diccionario que representa al héroe.
    genero: El género a evaluar.

  Returns:
    True si el héroe tiene el género especificado, False en caso contrario.
  """

  return heroe["genero"].upper() == genero.upper()

def stark_guardar_heroe_genero(lista_heroes, genero):
  """
  Guarda los héroes de un género específico en un archivo CSV.

  Args:
    lista_heroes: La lista de héroes.
    genero: El género a evaluar.

  Returns:
    True si pudo guardar el archivo, False caso contrario.
  """

  heroes_genero = [heroe for heroe in lista_heroes if es_genero(heroe, genero)]

  for heroe in heroes_genero:
    imprimir_dato(obtener_nombre_capitalizado(heroe))

  nombre_archivo = f"heroes_{genero}.csv"
  contenido = ",".join([heroe["nombre"] for heroe in heroes_genero])
  return guardar_archivo(nombre_archivo, contenido)

def calcular_min_genero(lista_heroes, dato, genero):
  """
  Calcula el héroe o heroína con el mínimo valor de un dato específico,
  filtrando por género.

  Args:
    lista_heroes: La lista de héroes.
    dato: El dato a evaluar.
    genero: El género a filtrar.

  Returns:
    El héroe o heroína con el mínimo valor del dato especificado.
  """

  if lista_heroes == []:
        return False

  bandera_primera = True
  diccionario_retorno = {}
  for diccionario in lista_heroes:

      #se verifica que diccionario['genero'] == genero_buscado y que diccionario[clave_numerica] represente a un numero real o entero
      if diccionario['genero'] == dato:            
          numero_actual = float(diccionario[genero]) # en caso de ser el nuevo menor, se castea solo una vez
          if (bandera_primera): #primera comparacion de valores numericos con una bandera
              bandera_primera = False
              numero_menor = numero_actual 
              diccionario_retorno = diccionario

          elif (numero_menor > numero_actual):
              numero_menor = numero_actual
              diccionario_retorno = diccionario
  return diccionario_retorno
  # encontrado = False

  # heroe_min = ""
 
  # for heroe in lista_heroes[dato]:
  #     encontrado = True
  #     if heroe < heroe_min or heroe_min is None:
  #       heroe_min = heroe

  # if not encontrado:
  #   return None

  # return heroe_min

def calcular_max_genero(lista_heroes, dato, genero):
  """
  Calcula el héroe o heroína con el máximo valor de un dato específico,
  filtrando por género.

  Args:
    lista_heroes: La lista de héroes.
    dato: El dato a evaluar.
    genero: El género a filtrar.

  Returns:
    El héroe o heroína con el máximo valor del dato especificado.
  """

  if lista_heroes == []:
        return False

  bandera_primera = True
  diccionario_retorno = {}
  for diccionario in lista_heroes:

      #se verifica que diccionario['genero'] == genero_buscado y que diccionario[clave_numerica] represente a un numero real o entero
      # print(diccionario['genero'])
      # print(diccionario['genero'])
      # print(diccionario[genero])
      # print(genero)
      if diccionario['genero'] == dato:            
        numero_actual = float(diccionario[genero]) # en caso de ser el nuevo mayor, se castea solo una vez
        if (bandera_primera): #primera comparacion de valores numericos con una bandera
            bandera_primera = False
            numero_mayor = numero_actual 
            diccionario_retorno = diccionario

        elif (numero_mayor < numero_actual):
            numero_mayor = numero_actual
            diccionario_retorno = diccionario

  return diccionario_retorno

  # encontrado = False
  # heroe_max = None
  # heroe_max = ""

  # for heroe in lista_heroes[dato]:
  #     encontrado = True
  #     if heroe > heroe_max or heroe_max is None:
  #       heroe_max = heroe
        
  # if not encontrado:
  #   return None

  # return heroe_max

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

def calcular_max_min_dato_genero(lista_heroes, clave, genero, tipo):
  """
  Calcula el héroe o heroína con el valor máximo o mínimo de un dato específico,
  filtrando por género.

  Args:
    lista_heroes: La lista de héroes.
    dato: Clave del dato a evaluar.
    genero: El género a filtrar.
    tipo: El tipo de valor a buscar: 'max' o 'min'.

  Returns:
    El héroe o heroína con el valor máximo o mínimo del dato especificado.
  """

  if len(lista_heroes) == 0:
    return None

  if tipo not in ("maximo", "minimo"):
    print("El tipo de cálculo debe ser 'maximo' o 'minimo'")
    return None

  if clave not in ("M", "F"):
    print("El género debe ser 'M' o 'F'")
    return None

  # lista_heroes_genero = obtener_heroes_por_tipo(lista_heroes,clave,genero)

  if tipo == "maximo":
    return calcular_max_genero(lista_heroes, clave, genero)
    # return calcular_max_genero(lista_heroes_genero, clave, genero)
  if tipo == "minimo":
    return calcular_min_genero(lista_heroes, clave, genero)
    # return calcular_min_genero(lista_heroes_genero, clave, genero)

def stark_calcular_imprimir_guardar_heroe_genero(lista_heroes, dato, genero, tipo):
  """
  Calcula el héroe o heroína con el valor máximo o mínimo de un dato específico,
  filtrando por género, e imprime y guarda el resultado en un archivo CSV.

  Args:
    lista_heroes: La lista de héroes.
    dato: El dato a evaluar.
    genero: El género a filtrar.
    tipo: El tipo de valor a buscar: 'max' o 'min'.

  Returns:
    True si pudo guardar el archivo, False caso contrario.

  """

 

  heroe = calcular_max_min_dato_genero(lista_heroes, dato, genero, tipo)

  # mensaje = f"{tipo.capitalize()}: {obtener_nombre_y_dato(heroe, dato)}"
  mensaje = f"{obtener_nombre_y_dato(heroe, dato)}"
  imprimir_dato(mensaje)

  nombre_archivo = f"heroes_{tipo}_{dato}_{genero}.csv"
  contenido = obtener_nombre_y_dato(heroe, dato)
  return guardar_archivo(nombre_archivo, contenido)

def sumar_dato_heroe_genero(lista_heroes, dato, genero):
  """
  Suma el valor de un dato específico de los héroes o heroínas de un género específico.

  Args:
    lista_heroes: La lista de héroes.
    dato: El dato a evaluar.
    genero: El género a filtrar.

  Returns:
    La suma del valor del dato especificado.
  """

  sumadora = 0

  for heroe in lista_heroes:
    if dato not in lista_heroes[0]:
      return -1

    if not isinstance(heroe, dict):
      return -1

    if heroe == {}:
      continue

    if heroe["genero"] != genero:
      continue

    sumadora += float(heroe[dato])

  return sumadora

def cantidad_heroes_genero(lista_heroes, genero):
  """
  Cuenta la cantidad de héroes o heroínas de un género específico.

  Args:
    lista_heroes: La lista de héroes.
    genero: El género a filtrar.

  Returns:
    La cantidad de héroes o heroínas del género especificado.
  """

  cantidad = 0

  for heroe in lista_heroes:
    if heroe["genero"] == genero:
      cantidad += 1

  return cantidad

def dividir(suma, cantidad):
  """
  Divide dos números.

  Args:
    suma: El primer número.
    cantidad: El segundo número.

  Returns:
    El resultado de la división.
  """
  if cantidad == 0:
    division = None
  else:
    division = suma / cantidad

  return division

def calcular_promedio_genero(lista_heroes, dato, genero):
  """
  Calcula el promedio del valor de un dato específico de los héroes o heroínas de un género específico.

  Args:
    lista_heroes: La lista de héroes.
    dato: El dato a evaluar.
    genero: El género a filtrar.

  Returns:
    El promedio del valor del dato especificado.
  """

  suma = sumar_dato_heroe_genero(lista_heroes, dato, genero)
  cantidad = cantidad_heroes_genero(lista_heroes, genero)
  if cantidad == 0:
    return None

  return dividir(suma, cantidad)

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista_heroes, genero):
  """
  Calcula el promedio de altura de los héroes o heroínas de un género específico, lo imprime y lo guarda en un archivo CSV.

  Args:
    lista_heroes: La lista de héroes.
    genero: El género a filtrar.

  Returns:
    True si pudo la lista tiene algún elemento y pudo guardar el archivo, False en caso de que esté vacía o no haya podido guardar el archivo.
  """

  if not lista_heroes:
    imprimir_dato("Error: Lista de héroes vacía.")
    return False

  promedio_altura = calcular_promedio_genero(lista_heroes, "altura", genero)


  mensaje = f"Altura promedio género {genero}: {promedio_altura:.2f}"
  imprimir_dato(mensaje)

  nombre_archivo = f"heroes_promedio_altura_{genero}.csv"
  contenido = f"{promedio_altura:.2f}"
  guardar_archivo(nombre_archivo, contenido)
  return contenido

def calcular_cantidad_tipo(lista_heroes, tipo_dato):
  """
  Calcula la cantidad de cada valor del tipo de dato especificado en la lista de héroes.

  Args:
    lista_heroes: La lista de héroes.
    tipo_dato: El tipo de dato a buscar.

  Returns:
    Un diccionario con los distintos valores del tipo de dato y la cantidad de cada uno.
  """

  if not lista_heroes:
    return {"Error": "La lista se encuentra vacía"}

  cantidad_por_tipo = {}

  for heroe in lista_heroes:
    valor = heroe[tipo_dato]
    valor = capitalizar_palabras(valor)
    if valor in cantidad_por_tipo:
      cantidad_por_tipo[valor] += 1
    else:
      cantidad_por_tipo[valor] = 1
  # print(cantidad_por_tipo)
    # valor = heroe[tipo_dato]

    # valor = capitalizar_palabras(valor)

    # if valor not in cantidad_por_tipo:
    #   cantidad_por_tipo[valor] = 1
    # else:
    #   cantidad_por_tipo[valor] += 1

  return cantidad_por_tipo

def guardar_cantidad_heroes_tipo(cantidad_por_tipo, dato):
  """
  Guarda en un archivo CSV la cantidad de héroes de cada variedad del tipo de dato especificado.

  Args:
    cantidad_por_tipo: Un diccionario con las distintas variedades del tipo de dato y la cantidad de cada una.
    dato: El tipo de dato a buscar.

  Returns:
    True si salió todo bien, False caso contrario.
  """

  if not cantidad_por_tipo:
    return False

  nombre_archivo = f"heroes_cantidad_{dato}.csv"
  # print(cantidad_por_tipo)

  for clave, valor in cantidad_por_tipo.items():

    if clave != '':
      mensaje = f"Caracteristica: {clave} - Cantidad de heroes: {valor}"

      print(mensaje)

  # resultado = guardar_archivo(nombre_archivo, mensaje)

  # if not resultado:
  #   return False

  return True

def stark_calcular_cantidad_por_tipo(lista_heroes, tipo_dato):
  """
  Calcula la cantidad de cada valor del tipo de dato especificado en la lista de héroes y guarda el resultado en un archivo CSV.

  Args:
    lista_heroes: La lista de héroes.
    tipo_dato: El tipo de dato a buscar.

  Returns:
    True si pudo guardar el archivo, False caso contrario.
  """

  cantidad_por_tipo = calcular_cantidad_tipo(lista_heroes, tipo_dato)

  resultado = guardar_cantidad_heroes_tipo(cantidad_por_tipo, tipo_dato)

  return resultado

def obtener_lista_de_tipos(lista_heroes, tipo_dato):
  """
  Obtiene una lista con las distintas variedades del tipo de dato especificado en la lista de héroes.

  Args:
    lista_heroes: La lista de héroes.
    tipo_dato: El tipo de dato a buscar.

  Returns:
    Un set con las distintas variedades del tipo de dato especificado.
  """

  lista_valores = []

  for heroe in lista_heroes:

    valor = heroe[tipo_dato]

    if valor is None or valor == "":
      valor = "N/A"

    valor = capitalizar_palabras(valor)
    lista_valores.append(valor)

  lista_valores = set(lista_valores)
  # print(lista_valores)
  return lista_valores

def normalizar_dato(dato, valor_default):
  """
  Normaliza un dato de héroe, reemplazando los valores vacíos por el valor por defecto especificado.

  Args:
    dato: El dato de héroe a normalizar.
    valor_default: El valor por defecto a utilizar en caso de que el dato esté vacío.

  Returns:
    El dato normalizado.
  """

  if dato is None or dato == "":
    dato = valor_default

  return dato

def normalizar_heroe(heroe, key):
  """
  Normaliza un héroe, capitalizando las palabras de su nombre y del valor de la key especificada, luego normaliza el valor de la key, reemplazando los valores vacíos por el valor por defecto especificado.

  Args:
    héroe: El héroe a normalizar.
    key: El nombre de la key a normalizar.

  Returns:
    El héroe normalizado.
  """


  heroe["nombre"] = capitalizar_palabras(heroe["nombre"])

  valor = heroe[key]
  valor = capitalizar_palabras(valor)

  valor = normalizar_dato(valor, "N/A")

  heroe[key] = valor

  return heroe

def obtener_heroes_por_tipo(lista_heroes, set_tipos, tipo_dato):
  """
  Obtiene un diccionario con los héroes de cada variedad del tipo de dato especificado.

  Args:
    lista_heroes: La lista de héroes.
    set_tipos: Un set con las distintas variedades del tipo de dato.
    tipo_dato: El tipo de dato a evaluar.

  Returns:
    Un diccionario con los héroes de cada variedad.
  """

  diccionario = {}

  for tipo in set_tipos:
    if tipo not in diccionario:
      diccionario[tipo] = []

    for heroe in lista_heroes:
      valor_normalizado = normalizar_dato(heroe[tipo_dato], "N/A")

      if valor_normalizado.capitalize() == tipo.capitalize():
        diccionario[tipo].append(heroe["nombre"])
  # print(diccionario)
  return diccionario

def guardar_heroes_por_tipo(diccionario, tipo_dato):
  """Guarda los superhéroes por tipo en un archivo CSV.

  Args:
    diccionario: Diccionario que representa los distintos tipos como clave y una lista de nombres como valor.
    tipo_dato: Tipo de dato a evaluar.

  Returns:
    True si salió todo bien, False caso contrario.
  """
  # print(diccionario)
  if len(diccionario) == 0:
    return False

  nombre_archivo = f"heroes_segun_{tipo_dato}.csv"
  # print(diccionario)
  with open(nombre_archivo, "w") as archivo:

    for tipo, lista_nombres in diccionario.items():
      if(tipo!="N/a" and lista_nombres != []):
        print(tipo+": ",end="")
        archivo.write(f"{tipo},")
        # print(lista_nombres)
        for nombre in lista_nombres:
          
          print(nombre+" | ",end="")
          archivo.write(f"{nombre},")
        print("\n")
        archivo.write("\n")

  return True

def stark_listar_heroes_por_dato(lista_personajes, tipo_dato):
  """Lista los superhéroes por tipo en un archivo CSV.

  Args:
    lista_personajes: Lista de superhéroes.
    tipo_dato: Tipo de dato a evaluar.

  Returns:
    True si pudo guardar el archivo, False caso contrario.
  """

  lista_tipos = obtener_lista_de_tipos(lista_personajes, tipo_dato)

  diccionario_heroes_por_tipo = obtener_heroes_por_tipo(lista_personajes, lista_tipos, tipo_dato)

  return guardar_heroes_por_tipo(diccionario_heroes_por_tipo, tipo_dato)

def imprimir_superheroes_genero(data, genero):
  """
  Imprime por consola el nombre de cada superhéroe de un género específico.

  Parámetros:
    data: Lista de superhéroes.
    genero: Género de los superhéroes a imprimir.

  Retorna:
    None
  """


def imprimir_dato(dato:str):
  """
  Imprime un dato por pantalla.

  Parámetros:
    dato: Dato a imprimir.

  Retorna:
    None
  """

  print(f"{dato}")



def main():
  """
  Programa principal.

  Parámetros:
    None

  Retorna:
    None
  """

  datos = leer_archivo("data_stark.json")
  if datos is not None:
    print("Datos cargados correctamente")
  else:
    print("Archivo vacío")
  stark_marvel_app_5(datos["heroes"])

main()