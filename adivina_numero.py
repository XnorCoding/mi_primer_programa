from random import seed
from random import random

while True:
    numero_oculto = round(random()*10)
    print("Cheto del programador: El número que ha elegido la máquina es el {}. No se lo digas o se enfadará...".format(numero_oculto))
    intentos = 0
    acertado = False
    print("\nYa he elegido un número del 0 al 10, tienes 3 intentos para adivinarlo.\n")
    while intentos < 3:
        numero_elegido = int(input("Introduce un número entero del 0 al 10: "))
        if numero_elegido == numero_oculto:
            print("Genial! Lo has adivinado!, mi número era el {}!.".format(numero_oculto))
            print("Has ganado!")
            acertado = True
            break
        else:
            intentos += 1
            print("No, ese no es! \nTe quedan {} intentos!".format(str(3-intentos)))
    if intentos == 3: #es decir, si hemos salido del anterior bucle po9r quedarnos sin intentos...
        print("Oh, lo siento, has perdido! \nQuieres que te gane otra vez?")
    elif acertado == True: #o sea, si hemos salido del anterior bucle por acertar el número...
        print("Eh! quiero la revancha, jugamos otra vez?")
    else:
        print("Quieres jugar otra vez?")

    revancha = input("Quieres jugar otra partida?: (Sí/No)   ")
    if revancha == "No":
        break

print("Vale, ya nos veremos. Cuídate!! \nPrograma finalizado.")