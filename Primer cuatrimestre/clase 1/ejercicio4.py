# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
# distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
# ser soltero.'

edad = int(input("Ingrese la edad: "))
while edad < 0:
    cantidad = int(input("Edad inválida. Ingrese nuevamente (mayor o igual que 0): "))
    
estado_civil = input("Ingrese el estado civil: ")

if edad < 18 and estado_civil != "Soltero":
    print("Es muy pequeño para NO ser soltero.")
