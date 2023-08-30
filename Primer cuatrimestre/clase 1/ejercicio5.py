# Tarifa base
tarifa_base = 15000

# Pedir estación del año y localidad
estacion = input("Ingrese la estación del año (Invierno/Verano/Otoño/Primavera): ").capitalize()
localidad = input("Ingrese la localidad (Bariloche/Cataratas/Mar del Plata/Córdoba): ").capitalize()

# Validar el ingreso de datos
while estacion not in ["Invierno", "Verano", "Otoño", "Primavera"] or localidad not in ["Bariloche", "Cataratas", "Mar del Plata", "Córdoba"]:
    print("Estación o localidad ingresada no válida. Intente nuevamente.")
    estacion = input("Ingrese la estación del año (Invierno/Verano/Otoño/Primavera): ").capitalize()
    localidad = input("Ingrese la localidad (Bariloche/Cataratas/Mar del Plata/Córdoba): ").capitalize()

# Calcular precio final
precio_final = tarifa_base

if estacion == "Invierno":
    if localidad == "Bariloche":
        precio_final *= 1.20
    elif localidad in ["Cataratas", "Córdoba"]:
        precio_final *= 0.90
    elif localidad == "Mar del Plata":
        precio_final *= 0.80
elif estacion == "Verano":
    if localidad == "Bariloche":
        precio_final *= 0.80
    elif localidad in ["Cataratas", "Córdoba"]:
        precio_final *= 1.10
    elif localidad == "Mar del Plata":
        precio_final *= 1.20
elif estacion in ["Otoño", "Primavera"]:
    if localidad == "Bariloche" or localidad == "Cataratas" or localidad == "Mar del Plata":
        precio_final *= 1.10

# Mostrar precio final
print(f"El precio final del viaje a {localidad} en {estacion} es: ${precio_final:}")