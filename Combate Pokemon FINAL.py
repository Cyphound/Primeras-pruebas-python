
import random
import os

from random import randint

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

TAMAÑO_VIDA = 20

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE

os.system("cls")

while vida_pikachu != 0 and vida_squirtle != 0:
    # Se prosigue con el combate

    # Ataque de pikachu
    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ha elegido Bola Voltio")
        vida_squirtle -= 10
    else:
        print("Pikachu ha elegido Onda Trueno\n")
        vida_squirtle -= 13

    # Se mostrara la vida de los dos pokemons

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0

    barrita_pikachu = int(vida_pikachu * TAMAÑO_VIDA / VIDA_INICIAL_PIKACHU)
    print("\nPikachu:    [{}{}] ({}/{})".format("#" * barrita_pikachu, " " * (TAMAÑO_VIDA - barrita_pikachu), 
    vida_pikachu, VIDA_INICIAL_PIKACHU))

    barrita_squirtle = int(vida_squirtle * TAMAÑO_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("#" * barrita_squirtle, " " * (TAMAÑO_VIDA - barrita_squirtle), 
    vida_squirtle, VIDA_INICIAL_SQUIRTLE))
    
    input("\n\nEnter para continuar...\n\n")

    os.system("cls")

    # Ataque de Squirtle
    print("Es turno de Squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "A" and ataque_squirtle != "B" and ataque_squirtle != "P" and ataque_squirtle != "N":
        ataque_squirtle = input("¿Que ataque desea realizar?\n"
        "[P]lacaje\n"
        "Pistola de [A]gua\n"
        "[B]urbuja\n"
        "[N]ada ")

    if ataque_squirtle == "P":
        print("\nSquirtle ataca con Placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("\nSquirtle ataca con Pistola de Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("\nSquirtle ataca con Burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("\nSquirtle no ha echo nada")

    # Se mostrara la vida de los dos pokemons

    if vida_pikachu < 0:
        vida_pikachu = 0

    if vida_squirtle < 0:
        vida_squirtle = 0
 
    barrita_pikachu = int(vida_pikachu * TAMAÑO_VIDA / VIDA_INICIAL_PIKACHU)
    print("\nPikachu:    [{}{}] ({}/{})".format("#" * barrita_pikachu, " " * (TAMAÑO_VIDA - barrita_pikachu), 
    vida_pikachu, VIDA_INICIAL_PIKACHU))

    barrita_squirtle = int(vida_squirtle * TAMAÑO_VIDA / VIDA_INICIAL_SQUIRTLE)
    print("Squirtle:   [{}{}] ({}/{})".format("#" * barrita_squirtle, " " * (TAMAÑO_VIDA - barrita_squirtle), 
    vida_squirtle, VIDA_INICIAL_SQUIRTLE))

    input("\nEnter para continuar...\n\n")

    os.system("cls")

os.system("cls") 

# Se dira el ganador, una vez termine el combate
if vida_pikachu > vida_squirtle:
    print("¡Pikachu ha ganado el combate!")
else:
    print("¡Squirtle ha ganado el combate!")

input("\n\nEnter para cerrar el juego...")