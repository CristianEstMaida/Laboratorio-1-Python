# Pedir el nombre y el sueldo
nombre = input("Por favor, introduce tu nombre: ")
sueldo = float(input("Introduce tu sueldo actual: "))
while sueldo < 0:
    cantidad = float(input("Sueldo inválido. Ingrese sueldo nuevamente (mayor o igual que 0): "))

# Calcular el aumento del 10%
aumento = sueldo * 0.10
nuevo_sueldo = sueldo + aumento

# Informar el aumento de sueldo
print(f"Hola {nombre}, tu sueldo ha sido incrementado en un 10%.")
print(f"Sueldo anterior: {sueldo}")
print(f"Aumento: {aumento}")
print(f"Nuevo sueldo: {nuevo_sueldo}")
