pokemon_elegido="MisigNo"


while pokemon_elegido != "Squirtle" and pokemon_elegido != "Charmander" and pokemon_elegido != "Bulbasaur":
    pokemon_elegido = input("Contra qué Pokemon quieres combatir? (Squirtle / Charmander / Bulbasaur): ")

print("Muy bien, lucharás contra " + pokemon_elegido + "!")

vida_pikachu = 100
vida_enemigo = 0
ataque_enemigo = "Placaje"
poder_enemigo = 0

if pokemon_elegido == "Squirtle":
    vida_enemigo = 90
    ataque_enemigo = "Burbuja"
    poder_enemigo = 7
elif pokemon_elegido == "Charmander":
    vida_enemigo = 80
    ataque_enemigo = "Ascuas"
    poder_enemigo = 9
elif pokemon_elegido == "Bulbasaur":
    vida_enemigo = 100
    ataque_enemigo = "Látigo cepa"
    poder_enemigo = 6

while vida_pikachu > 0 and vida_enemigo > 0:
    #print("Código del combate") #comprobador de flujo

    ataque_elegido = input("Qué ataque quieres realizar? (Impactrueno / Bola Voltio): ")

    # comprobando que el usuario haya introducido el nombre del ataque correctamente...
    while ataque_elegido != "Impactrueno" and ataque_elegido != "Bola Voltio":
        print("Pikachu no conoce el ataque " + ataque_elegido + ", prueba otra vez")
        ataque_elegido = input("Qué ataque quieres realizar? (Impactrueno / Bola Voltio): ")


    if ataque_elegido == "Impactrueno":
        poder_pikachu = 10
        vida_enemigo -= 10
    else:
        poder_pikachu = 12
        vida_enemigo -= 12

    #print("Pikachu utilizó " + ataque_elegido + "!")
    print("Pikachu utilizó {} que hace {} de daño!".format(ataque_elegido, poder_pikachu))

    if vida_enemigo < 0:
        print("La salud de " + pokemon_elegido + " bajó a 0!")
        break
    else:
        #print("La salud de " + pokemon_elegido + " bajó a " + str(vida_enemigo) + "!")
        print("La salud de {} bajó a {}!".format(pokemon_elegido, vida_enemigo))

    print("")
    print("Es el turno del enemigo.")
    print("")
    #print(pokemon_elegido + " utilizó " + ataque_enemigo + "!")
    print("{} utilizó {} que hace {} de daño!".format(pokemon_elegido, ataque_enemigo, poder_enemigo))

    vida_pikachu -= poder_enemigo
    print("La salud de Pikachu bajó a " + str(vida_pikachu) + "!")
    print("")
    if vida_enemigo > 0:
        print("Es tu turno otra vez.")
    else:
        print(pokemon_elegido + " ha sido debilitado!")

    if vida_pikachu < 0:
        print("Pikachu ha sido debilitado!")


print("El combate ha terminado")

if vida_pikachu < 0 and vida_enemigo < 0:
    print("Ambos pokémon se han debilitado a la vez! Esto es un empate!")
elif vida_pikachu < 0:
    print("El rival te ha vencido!")
else:
    print("Has ganado el combate!")

