edades = [25, 36, 18, 23, 45]
nombres = ["Juan", "Ana", "Sol", "Mario", "Sonia"]

indice_persona_mas_joven = 0

for i in range(1, len(edades)):
    if edades[i] < edades[indice_persona_mas_joven]:
        indice_persona_mas_joven = i

nombre_persona_mas_joven = nombres[indice_persona_mas_joven]

print("La persona más joven es:", nombre_persona_mas_joven)