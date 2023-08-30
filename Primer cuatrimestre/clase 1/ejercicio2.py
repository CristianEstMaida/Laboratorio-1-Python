# Pedir la edad
edad = int(input("Por favor, introduce tu edad: "))
while edad < 0:
    cantidad = int(input("Edad inválida. Ingrese nuevamente (mayor o igual que 0): "))

# Determinar la categoría
if edad > 18:
    categoria = "mayor de edad"
elif 13 <= edad <= 17:
    categoria = "adolescente"
else:
    categoria = "niño"

# Informar la categoría
print(f"Tú tienes {edad} años, por lo tanto eres {categoria}.")