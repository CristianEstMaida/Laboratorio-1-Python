from funciones import *

bandera = True
while bandera == True:
  mostrar_menu()
  opcion = input("Ingrese una opción: ").upper()
  bandera = procesar_opcion(opcion, bandera)