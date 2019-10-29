def en_rango(numero, ran0, ran1):
    if ran0 == ran1:
        print("Es complicadete hacer un rango SI LOS DOS NUMEROS QUE LO COMPONEN SON IGUALES, GENIO!")
    else:
        if ran0 > ran1:
            if numero in range(ran1, ran0):
                return True
            else:
                return False
        else:
            if numero in range(ran0, ran1):
                return True
            else:
                return False

lista_numeros = [2,3,4,56,75,234,64,13]

def devuelve_pares(lista):
    lista_pares = []
    for i in lista:
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares



print(en_rango(50, 0, 100))
print(en_rango(99, 100, 10))
print(en_rango(21, 55, 23))

print(devuelve_pares(lista_numeros))