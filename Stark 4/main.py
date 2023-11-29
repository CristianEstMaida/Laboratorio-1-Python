import re
from data_stark import lista_personajes

def extraer_iniciales(nombre_heroe:str)->str:
  """
  Función que extrae las iniciales de un nombre de superhéroe.

  Args:
    nombre_heroe: String con el nombre del superhéroe.

  Returns:
    String con las iniciales del nombre del superhéroe seguidas por un punto.
  """

  if not nombre_heroe:
    return "N/A"

  nombre_heroe = re.sub("the", "", nombre_heroe)

  nombre_heroe = nombre_heroe.replace("-", " ")

  iniciales = ""
  
  for i,letra in enumerate(nombre_heroe):  
  
    if letra.isalpha() and letra != " ":
      if i == 0 or nombre_heroe[i - 1] == " ":
        iniciales += letra.upper() + "."
    elif not letra.isspace():
      break
  
  return iniciales


def definir_iniciales_nombre(heroe)->bool:
  """
  Función que define las iniciales del nombre de un superhéroe.

  Args:
    heroe: Diccionario con los datos del superhéroe.

  Returns:
    True si la función se ejecutó correctamente, False en caso contrario.
  """

  if not isinstance(heroe, dict):
    return False

  if "nombre" not in heroe:
    return False

  heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

  return True

def agregar_iniciales_nombre(lista_heroes)->bool:
  """
  Agrega las iniciales de los nombres de los héroes a una nueva lista.

  Args:
    lista_heroes: lista de personajes.

  Returns:
    True si la función se ejecutó con éxito, False en caso contrario.
  """

  if not isinstance(lista_heroes, list):
    print("El parámetro 'lista_heroes' debe ser del tipo lista.")
    return False
  if len(lista_heroes) < 1:
    print("La lista debe contener al menos un elemento.")
    return False

  lista_iniciales= []
  for heroe in lista_heroes:
    iniciales = definir_iniciales_nombre(heroe)
    
    if iniciales is False:
      print("El origen de datos no contiene el formato correcto.")
      return False
    lista_iniciales.append(iniciales)

  return True

def stark_imprimir_nombres_con_iniciales(lista_heroes):
  """
  Imprime los nombres de los héroes con sus iniciales.

  Args:
    lista_heroes: lista de personajes.
  """

  if not isinstance(lista_heroes, list):
    print("El parámetro 'lista_heroes' debe ser del tipo lista.")
    return
  if len(lista_heroes) < 1:
    print("La lista debe contener al menos un elemento.")
    return

  bandera_lista_iniciales = agregar_iniciales_nombre(lista_heroes)

  if(bandera_lista_iniciales):

    for i in range(len(lista_heroes)):
    
        print("* {} ({})".format(lista_heroes[i].get("nombre"), lista_heroes[i].get("iniciales")))

def generar_codigo_heroe(id_heroe, genero_heroe)->str:
  """
  Genera un código de héroe con el formato especificado.

  Args:
    id_heroe: identificador del héroe.
    genero_heroe: género del héroe.

  Returns:
    Código de héroe generado.
  """

  if not isinstance(id_heroe, int):
    return "N/A"
  if not genero_heroe:
    return "N/A"
  if not re.match("^[MFN]$", genero_heroe):
    return "N/A"

  codigo = genero_heroe + "-"
  codigo += str(id_heroe).zfill(9 - len(genero_heroe))

  return codigo

def agregar_codigo_heroe(heroe, id_heroe)->bool:
  """
  Agrega un código de héroe a un diccionario.

  Args:
    heroe: diccionario con los datos del personaje.
    id_heroe: identificador del héroe.

  Returns:
    True si la función se ejecutó con éxito, False en caso contrario.
  """

  if not heroe:
    return False
  codigo = generar_codigo_heroe(id_heroe, heroe["genero"])

  
  if len(codigo) != 10:
     return False

  heroe["codigo_heroe"] = codigo

  return True

def stark_generar_codigos_heroes(lista_heroes):
  """
  Genera los códigos de héroe para una lista de personajes.

  Args:
    lista_heroes: lista de personajes.

  Returns:
    Sin retorno.
  """

  # Validaciones

  if not lista_heroes:
    print("La lista debe contener al menos un elemento.")
    return
  if not isinstance(lista_heroes[0], dict):
    print("Todos los elementos de la lista deben ser del tipo diccionario.")
    return
  if not lista_heroes[0].get("genero"):
    print("Todos los elementos de la lista deben contener la clave 'genero'.")
    return
  
  id_heroe = 1
  for heroe in lista_heroes:
    agregar_codigo_heroe(heroe, id_heroe)

    id_heroe += 1

  print("Se asignaron {} códigos".format(len(lista_heroes)))
  print("El código del primer héroe es: {}".format(lista_heroes[0]["codigo_heroe"]))
  print("El código del del último héroe es: {}".format(lista_heroes[-1]["codigo_heroe"]))

def sanitizar_entero(numero_str)->int:
  """
  Sanitiza un número entero.

  Args:
    numero_str: string que representa un posible número entero.

  Returns:
    Número entero si el string es válido, -1 si contiene carácteres no numéricos,
    -2 si es negativo, -3 si ocurre un error al convertirlo a entero.
  """

  numero_str = numero_str.strip()

  if not numero_str.isdigit():
    return -1

  if numero_str[0] == "-":
    return -2

  numero = int(numero_str)

  if not isinstance(numero, int):
    return -3

  # Retorno

  return numero

def sanitizar_flotante(numero_str)->float:
  """
  Sanitiza un número flotante.

  Args:
    numero_str: string que representa un posible número decimal.

  Returns:
    Número flotante si el string es válido, -1 si contiene carácteres no numéricos,
    -2 si es negativo, -3 si ocurre un error al convertirlo a flotante.
  """

  numero_str = numero_str.strip()

  if not numero_str.replace(".", "").isdigit():
    return -1

  if numero_str[0] == "-":
    return -2

  numero = float(numero_str)

  if not isinstance(numero, float):
    return -3

  if numero < 0:
    return -2

  return numero

def sanitizar_string(valor_str, valor_por_defecto="-")->str:
  """
  Sanitiza un string.

  Args:
    valor_str: string que representa el texto a validar.
    valor_por_defecto: string que representa un valor por defecto
    (parámetro opcional, inicializarlo con ‘-’).

  Returns:
    String validado, "N/A" si contiene números, valor por defecto convertido a
    minúsculas si el string a validar está vacío y nos pasaron un valor por defecto.
  """

  valor_str = valor_str.strip()
  valor_por_defecto = valor_por_defecto.strip()

  if re.match("^[a-zA-Z ]*$", valor_str):
    valor_str = valor_str.lower()
  else:
    return "N/A"

  # if any(c.isdigit() for c in valor_str):
  #   return "N/A"

  if "/" in valor_str:
    valor_str = valor_str.replace("/", " ")

  # Conversión a minúsculas

  # valor_str = valor_str.lower()

  # Retorno

  if valor_str == "":
    return valor_por_defecto.lower()
  else:
    return valor_str

def sanitizar_dato(heroe, clave, tipo_dato):
  """
  Sanitiza un dato en un diccionario.

  Args:
    heroe: diccionario con los datos del personaje.
    clave: string que representa la clave del dato a sanitizar.
    tipo_dato: string que representa el tipo de dato a sanitizar.

  Returns:
    True si se sanitizó algún dato, False en caso contrario.
  """

  tipo_dato = tipo_dato.lower()
  if tipo_dato not in ["string", "entero", "flotante"]:
    print("Tipo de dato no reconocido")
    return False

  if clave.lower() not in heroe.keys():
    print("La clave especificada no existe en el héroe")
    return False

  valor = heroe[clave]
  if tipo_dato == "string":
    valor = sanitizar_string(valor)
  elif tipo_dato == "entero":
    valor = sanitizar_entero(valor)
  elif tipo_dato == "flotante":
    valor = sanitizar_flotante(valor)

  heroe[clave] = valor

  return True

def stark_normalizar_datos(lista_heroes):
  """
  Normaliza los datos de una lista de héroes.

  Args:
    lista_heroes: lista de diccionarios con los datos de los héroes.

  Returns:
    Nada.
  """

  if not lista_heroes:
    print("Error: Lista de héroes vacía")
    return

  for heroe in lista_heroes:
    for clave in ["color_ojos", "color_pelo", "inteligencia"]:
      sanitizar_dato(heroe, clave, "string")

    for clave in ["altura", "peso"]:
      sanitizar_dato(heroe, clave, "flotante")

    for clave in ["fuerza"]:
      sanitizar_dato(heroe, clave, "entero")

  print("Datos normalizados")

def generar_indice_nombres(lista_heroes)->list:
  """
  Genera un índice de nombres a partir de una lista de héroes.

  Args:
    lista_heroes: lista de diccionarios con los datos de los héroes.

  Returns:
    Lista de strings con las palabras que componen los nombres de los héroes.
  """

  if not lista_heroes:
    print("Error: Lista de héroes vacía")
    return

  for heroe in lista_heroes:
    if not isinstance(heroe, dict):
      print("Error: El origen de datos no contiene el formato correcto")
      return

    if "nombre" not in heroe.keys():
      print("Error: El origen de datos no contiene el formato correcto")
      return

  indice_nombres = []
  for heroe in lista_heroes:
    nombre = heroe["nombre"]
    palabras = re.findall(r"\w+", nombre)
    indice_nombres.extend(palabras)
    # nombre = heroe["nombre"].split()
    # for palabra in nombre:
    #   indice_nombres.append(palabra)

  return indice_nombres


def stark_imprimir_indice_nombre(lista_heroes):
  """
  Imprime un índice de nombres a partir de una lista de héroes.

  Args:
    lista_heroes: lista de diccionarios con los datos de los héroes.

  Returns:
    Nada.
  """

  indice_nombres = generar_indice_nombres(lista_heroes)

  print("Índice de nombres:")
  for palabra in indice_nombres:
    print(f"{palabra}-",end="")

def convertir_cm_a_mtrs(valor_cm):
  """
  Convierte una medida en centímetros a metros.

  Args:
    valor_cm: número que representa una medida en centímetros.

  Returns:
    Número flotante que representa la medida en metros.
  """

  # Validación del valor recibido

  if not isinstance(valor_cm, float) or valor_cm < 0:
    return -1

  return valor_cm / 100

def generar_separador(patron, largo, imprimir=True)->str:
  """
  Genera un separador de acuerdo a los parámetros recibidos.

  Args:
    patron: carácter que se utilizará como patrón para generar el separador.
    largo: cantidad de caracteres que va a ocupar el separador.
    imprimir: parámetro opcional del tipo booleano. Si se encuentra en True,
              el separador se imprime por pantalla antes de retornarlo.

  Returns:
    String que representa el separador generado.
  """

  if len(patron) < 1 or len(patron) > 2:
    return "N/A"

  if not isinstance(largo, int) or largo < 1 or largo > 235:
    return "N/A"

  separador = patron * largo

  if imprimir:
    print(separador)

  return separador

def generar_encabezado(titulo)->str:
  """
  Genera un encabezado de acuerdo al parámetro recibido.

  Args:
    titulo: string que representa el título de una sección de la ficha.

  Returns:
    String que representa el encabezado generado.
  """

  titulo = titulo.upper()

  largo_titulo = 70

  separador = generar_separador("*", largo_titulo)
  encabezado = f"{titulo}\n{separador}"

  return encabezado

def imprimir_ficha_heroe(heroe):
  """
  Imprime la ficha de un héroe.

  Args:
    heroe: diccionario con los datos del héroe.

  Returns:
    Nada.
  """

  encabezado_principal = generar_encabezado("PRINCIPAL")
  print(encabezado_principal)

  for key, value in heroe.items():
    
    if key in ["nombre", "iniciales"]:
      if key == "nombre":
        print(f"\t{key.upper()} DEL HÉROE:\t\t{value}",end="")
      else:
        print(f" ({value})",end="")
  print("")
     
  for key, value in heroe.items():
  
    if key in ["identidad", "empresa", "codigo_heroe"]:
      
      if key == "identidad":
        print(f"\t{key.upper()} SECRETA:\t\t{value.title()}")
      elif key == "empresa":
        print(f"\tCONSULTORA:\t\t\t{value.title()}")
      else:
        print(f"\tCÓDIGO DEL HÉROE:\t\t{value}")

  encabezado_fisico = generar_encabezado("FISICO")
  print(encabezado_fisico)


  for key, value in heroe.items():
    if key in ["altura", "peso", "fuerza"]:
      if key == "altura":
        print(f"\t{key.upper()}:\t\t\t\t{value} Mtrs.")
      elif key == "peso":
        print(f"\t{key.upper()}:\t\t\t\t{value} Kg.")
      else:
        print(f"\t{key.upper()}:\t\t\t\t{value} N")

  encabezado_senales_particulares = generar_encabezado("SEÑAS PARTICULARES")
  print(encabezado_senales_particulares)

  for key, value in heroe.items():
    if key in ["color_ojos", "color_pelo"]:
      if key == "color_ojos":
        print(f"\tCOLOR DE OJOS:\t\t\t{value.capitalize()}")
      else:
        print(f"\tCOLOR DE PELO:\t\t\t{value.title()}")


def stark_navegar_fichas(lista_heroes):
  """
  Navega por las fichas de los héroes de la lista.

  Args:
    lista_heroes: lista de diccionarios con los datos de los héroes.

  Returns:
    Nada.
  """

  indice_actual = 0


  heroe_actual = lista_heroes[indice_actual]
  imprimir_ficha_heroe(heroe_actual)

  while True:
    opcion = input(
        f"[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir: ")

    if opcion == "1":
      if indice_actual > 0:
        indice_actual = (indice_actual - 1)
      else:
        indice_actual = len(lista_heroes) - 1
     
    elif opcion == "2":
      if indice_actual < len(lista_heroes) - 1:
        indice_actual = (indice_actual + 1)
      else:
        indice_actual = 0
    elif opcion == "S":
      break
    else:
      print("Opción inválida")

    heroe_actual = lista_heroes[indice_actual]
    imprimir_ficha_heroe(heroe_actual)

def imprimir_menu():
  """
  Imprime el menú de opciones.

  Returns:
    Nada.
  """

  # Imprimir el menú

  print("""

1 - Imprimir la lista de nombres junto con sus iniciales
2 - Generar códigos de héroes
3 - Normalizar datos
4 - Imprimir índice de nombres
5 - Navegar fichas
S - Salir

____________________________________________________________
""")


def generar_codigos_heroes(lista_heroes):
  """
  Genera códigos de héroes.

  Args:
    lista_heroes: lista de diccionarios con los datos de los héroes.

  Returns:
    Nada.
  """

  for heroe in lista_heroes:

    if not isinstance(heroe["id_heroe"], int):
      heroe["codigo_heroe"] = "N/A"
      continue

    heroe["codigo_heroe"] = generar_codigo_heroe(heroe["id_heroe"], heroe["genero_heroe"])

def stark_menu_principal():
  """
  Imprime el menú de opciones y recibe la respuesta del usuario.

  Returns:
    Respuesta del usuario.
  """

  imprimir_menu()

  respuesta = input("Ingrese la opción deseada: ")

  while respuesta not in ["1", "2", "3", "4", "5", "S"]:
    respuesta = input("Opción inválida. Ingrese la opción deseada: ")

  return respuesta

def stark_marvel_app_3(lista_heroes):
  """
  Ejecuta el programa principal de la aplicación Marvel.

  Args:
    lista_heroes: lista de diccionarios con los datos de los héroes.

  Returns:
    Nada.
  """

  while True:

    respuesta = stark_menu_principal()

    if respuesta == "1":
      stark_imprimir_nombres_con_iniciales(lista_heroes)
    elif respuesta == "2":
      stark_generar_codigos_heroes(lista_heroes)
    elif respuesta == "3":
      stark_normalizar_datos(lista_heroes)
    elif respuesta == "4":
      stark_imprimir_indice_nombre(lista_heroes)
    elif respuesta == "5":
      stark_navegar_fichas(lista_heroes)
    elif respuesta == "S":
      break
    else:
      print("Opción inválida")

stark_marvel_app_3(lista_personajes)