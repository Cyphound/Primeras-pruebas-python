
import random

# A ver... Miedo tengo, no te mentire xd

titulo = "Escapa de la Prision"

print("\n" + titulo + "\n" + "_" * len(titulo) + "\n")

print("Un amigo y tu se escapan de la prision galactica, capturan a tu amigo\n"
      "y tu logras resguardarte, pero tienes que escapar antes de que te atrapaen\n"
      "pero ahora tienes que tomar una decision\n")

salida = input("¿Te escapas por la [P]uerta o la [T]rampilla? ")

numero = random.randint(0, 20)
operatoria = 13 * numero

victoria = "Te has escapado ¡Felicidades!"
derrota = "Has muerto"

if salida == "P":
    decision1 = input("\nTe vas por una puerta que hay, pero a tu desgracia encuentras un\n"
                      "alien con casco, ¿Te haces el [D]ormido o [C]orres? ")

    if decision1 == "D":
        print("\nMala decision, el alien te ve y decide matarte igual\n")
        print("\n" + derrota)
        exit()

    elif decision1 == "C":
        print("\nDespues de correr un buen rato y esquivar golpes logras safarte y escapar\n")
        print("\n" + victoria)
        exit()

elif salida == "T":

    decision1 = input("\nVes un trampilla y escapas por ahi, esta lleva a una alcantarilla\n"
                      "Cuando llegas al centro ves un gran palo. ¿Lo llevas? (S/N) ")

    print("\nLa alcantarilla te lleva donde un gran raton y este te hace una pregunta...\n")

    decision2 = int(input("\n¿Cuanto es {} * {}? \n".format(13, numero)))
    if decision2 == operatoria:
        print("\nOkey te puedes ir\n")

        if decision1 == "S":
            print("\nLogras escapar pero el peso del palo hace que te caigas y te atrapen\n")
            print("\n" + derrota)
            exit()

        elif decision1 == "N":
            print("\nTe escapas y logras encontrar una salida para escapar\n")
            print("\n" + victoria)
            exit()

    else:
        print("\nNo calculaste bien...\n")

        if decision1 == "S":
            print("\nCon el palo que traes lo golpeas y logras escapar de el y encontrar la salida\n")
            print("\n" + victoria)
            exit()

        elif decision1 == "N":
            print("\nAl no tener nada con quien golpear, el te atrapa y te mata\n")
            print("\n" + derrota)
            exit()

else:
    print("\nRespuesta no valida")


