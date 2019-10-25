mi_lista = []
input_usuario = ""
largo_lista = 0

while input_usuario != "FIN" and input_usuario != "fin":
    input_usuario = input("Qué necesitas comprar?? : (Teclea 'FIN' para terminar)")
    if input_usuario == "FIN" or input_usuario == "fin":
        continue
    mi_lista.append(input_usuario) #añade cada input de usuario a la lista con cada iteración



largo_lista = len(mi_lista)
indice = 0

'''while indice < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice]))
    indice +=1
'''

# aquí i no toma valores numéricos, sino los valores de cada uno de los elementos que hay dentro de la lista
# esto ocurre porque no le hemos puesto un intervalo, sino una lista como flag

for i in mi_lista:
    print("Tengo que comprar {}".format(i))

# para darle un intervalo como flag, se puede hacer la función equivalente:
for i in range(largo_lista):
    print("Tengo que comprar {}".format(mi_lista[i]))
# aquí i SÍ toma valores numéricos