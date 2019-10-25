frase_usuario = input("Introduce la frase que quieras analizar: ")

vocales = ["a", "e", "i", "o", "u"]
numero_vocales = 0
numero_consonantes = 0
numero_puntos = 0
numero_espacios  = 0
numero_mayusculas = 0
lista_vocales = []

for i in frase_usuario:
    if i in vocales:
        numero_vocales += 1
        lista_vocales.append(i)
    elif i == " ":
        numero_espacios += 1
    elif i == "." or i == ",":
        numero_puntos += 1
    else:
        numero_consonantes += 1

    if i.isupper():
        numero_mayusculas +=1


print("Aquí está el análisis de tu frase:")
print("Vocales: {}".format(numero_vocales))
print("Consonantes: {}".format(numero_consonantes))
print("Espacios: {}".format(numero_espacios))
print("Puntos: {}".format(numero_puntos))
print("Mayúsculas: {}".format(numero_mayusculas))
print("Las vocales que has utilizado, en el mismo orden son: {}".format(lista_vocales))