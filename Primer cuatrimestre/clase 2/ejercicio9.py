edades = [25, 36, 18, 23, 45]
nombres = ["Juan", "Ana", "Sol", "Mario", "Sonia"]

nombre_persona_mas_joven = None
edad_persona_mas_joven = None
indice_persona_mas_joven = 0


for indice_persona_mas_joven in range(len(nombres)):
    if edad_persona_mas_joven == None or edad_persona_mas_joven < edades[indice_persona_mas_joven]:
        nombre_persona_mas_joven = nombres[indice_persona_mas_joven]
        edad_persona_mas_joven = edades[indice_persona_mas_joven]

mensaje = f"La persona más joven es: {nombre_persona_mas_joven}"

print(mensaje)
