
precio_unitario_plato = 800
precio_unitario_bebida = 200
contador_amigos = 0
contador_jugo = 0
contador_total_platos = 0
contador_platos_pizza = 0
contador_platos_hamburguesa = 0
contador_platos_ensalada = 0
lista_pizza = []
lista_hamburguesa = []
lista_ensadala = []
lista_agua = []
lista_mas_tres = []
lista_mas_cinco = []
lista_mas_siete = []
lista_menos_tres = []
lista_menos_cinco = []


total_acumulado = 0

# respuesta = 's'
# while(respuesta == 's'):
#     respuesta = input("¿Desea continuar? (s/n) ")

respuesta = "SI"

while respuesta == "SI":
    
    contador_amigos +=1
    nombre = input("Ingrese nombre: ")

    plato = input("Plato principal elegido: ")
    
    while plato not in ["pizza", "hamburguesa", "ensalada"]:
        plato = input("Plato principal elegido inválido. Ingrese nuevamente (pizza, hamburguesa, ensalada): ")

    cant_platos = int(input("Cantidad de platos principales pedidos: "))
    
    while cant_platos < 1:
        cant_platos = int(input("La cantidad debe ser al menos 1 uno"))
        
    if plato =="pizza":
        contador_platos_pizza = cant_platos
        lista_pizza.append(nombre)
        
    elif plato == "hamburguesa":
        contador_platos_hamburguesa = cant_platos
        lista_hamburguesa.append(nombre)
    else:
        contador_platos_ensalada = cant_platos
        lista_ensadala.append(nombre)
    
    bebida = input("Bebida elegida: ")
    while plato not in ["jugo", "agua"]:
        plato = input("Bebida elegida inválida. Ingrese nuevamente (jugo, agua): ")

    cant_bebidas = int(input("Cantidad de bebidas pedidas"))
    
    while cant_bebidas < 1:
        cant_bebidas = int(input("La cantidad debe ser al menos 1 uno"))
        
    if bebida == "jugo":
        contador_jugo += 1
    elif bebida == "agua":
        lista_agua.append(nombre)
        
    cantidad_pedidos = cant_platos + cant_bebidas
    
    if cantidad_pedidos >= 3:
        lista_mas_tres.append(nombre)
    elif cantidad_pedidos >= 5:
        lista_mas_cinco.append(nombre)
    elif cantidad_pedidos >= 7: 
        lista_mas_siete.append(nombre)
    elif cantidad_pedidos <= 3:
        lista_menos_tres.append(nombre)
    elif cantidad_pedidos <= 5:
        lista_menos_cinco.append(nombre)
        
    
    contador_total_platos = contador_total_platos + cant_platos
    total_plato = cant_platos * precio_unitario_plato
    total_bebida = cant_bebidas * precio_unitario_bebida
    total_gastado = total_plato + total_bebida
    total_acumulado = total_acumulado + total_gastado
    
    respuesta = input("¿Desea continuar? (SI/NO) ").upper()
    
porcentaje_pizza = (contador_platos_pizza * 100) / contador_total_platos
porcentaje_ensalada = (contador_platos_pizza * 100) / contador_total_platos
porcentaje_hamburguesa = (contador_platos_pizza * 100) / contador_total_platos

if contador_jugo == 0:
    promedio_jugo = 0
else:
   promedio_jugo = (contador_jugo * precio_unitario_bebida) / contador_amigos
    
propina = total_acumulado * 0.1
    
print("A) El total gastado por el grupo es ", total_acumulado)
print("La propina sugerida para el personal es ", propina)
print("B) El promedio gastado en jugo es ", format(promedio_jugo, '.2f'))
print("C) Los porcentajes de pizza: {:.2f}%, ensalada: {:.2f}%, hamburguesa: {:.2f}%".format(porcentaje_pizza, porcentaje_ensalada, porcentaje_hamburguesa))
print(lista_pizza)
print(lista_hamburguesa)
print(lista_ensadala)
print(lista_mas_tres)
print(lista_mas_cinco)
print(lista_mas_siete)
print(lista_menos_tres)
print(lista_menos_cinco)
