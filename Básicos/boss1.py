import random
print ("Juego de la mazmorra\n"
        "----------------------\n"
        "\n"
        "Tu y tu compañero de celda os acabaís de escapar de la prisión espacial, habeís burlado a los guardias y os \n"
        "dirigis hacia el exterior. Entrais en una mazmorra controlada por mounstruos alienigenas, uno de los guardias \n"
        "ataca a tu compañero, se lo lleva pero tu pasas desapercibido escondido en las sombras. El guardia se retira, \n"
        "es tu posibilidad de escapar. Hacia dónde te diriges? \n"
        "\n"
        "A la izquierda tienes una puerta semiabierta, a la derecha una escotilla en el suelo. \n")
opcion = input("[OPCION (A) - Puerta semiabierta] | [OPCION (B) - Escotilla en el suelo]: ")
if opcion == "A":
    print ("Entras en la puerta semiabierta y otro guardia te descubre, qué haces?")
    opcion = input ("[OPCION (A) - Te haces el dormido] | [OPCION (B) - Sales corriendo hacia la siguiente puerta]: ")
    if opcion == "A":
        print ("El guardia te atrapa, te encierran en una celda de máxima seguridad \n FIN")
    elif opcion == "B":
        print ("Después de esa puerta encuentras una rana mutante que te regala un puñal casero hecho con la pata de "
                "una mesa, lo aceptas?")
        opcion = input("[OPCION (A) - Si] | [OPCION (B)] - No]: ")
        if opcion == "A":
            print("Coges el pincho y avanzas, hay dos pasillos circulares , no ves el final de ninguno de los dos, uno \n"
                "está  a la derecha y el otro a la izquierda, cuál tomas?")
            opcion = input("[OPCION (A) - Izquierda]|[OPCION (B) -  Derecha]")
            if opcion == "A":
                print ("La habitación se hace cada vez más oscura, ves tan poco que caes en un agujero en el suelo con \n"
                        "pinchos, mujeres a las 2 horas de forma lenta y dolorosa. \n FIN")
            elif opcion == "B":
                print ("Encuentras la salida, en la puerta hay aparcado un Ferrari espacial, te montas, es tu dia de "
                        "Suerte, las llaves están puestas. Huyes hacia el horizonte")
        elif opcion = "B"
elif opcion == "B":
    print("Caes en una zona inundada, el agua te llega hasta las rodillas, avanzas durante media hora y finalmente  "
            "llegas a una zona abierta, seca y con luz, parecen unas alcantarillas \n\n encuentras un palo largo, parece"
            "algo pesado, pero podrías servir, lo coges?")
    opcion = input("[OPCION (A) - Si] | [OPCION (B) - No]: ")

    palo_en_inventario = False

    if opcion == "A":
        print("Coges el palo")
        palo_en_inventario = True
    elif opcion == "B":
        print ("No coges el palo")
        palo_en_inventario = False
    else:
        print("No has elegido ninguna opcion, simplemente mueres.")
        exit()

    numero_random_rata = random.randint(1, 100)
    print ("Sigues adelante, encuentras una rata de 2 metros, la rata te pregunta cuanto es 13 * {}).".format(numero_random_rata))
    opcion = int(input("Cuál es el resultado? "))
    if opcion == 13 * numero_random_rata:
        print ("La rata te asesina en el acto, resulta no tolera a los cerebritos. \n FIN")
    else:
        print("Mala elección pero buena suerte. La rata abre una pureta delante de ti, parece un pasillo que lleva hasta la salida. Lo recorres, "
            "llegas al final, el tunel se derrumba detrás de ti, no hay slaida más que una especie  de boca de "
            "alcantarilla, pero esta lejos de tu alcance, Qué haces?")
        
        opcion = input ("[OPCION (A) - Espera a que alguien te rescate] | [OPCION (B) - Intentas salir]")
        if opcion == "A":
            print ("Un monton de ratas aparecen y te devoran vivo, es tu fin\nFIN")
        elif opcion == "B" and palo_en_inventario == True:
            print ("Usas el palo que cogiste antes para impulsarte, consigues trepar y salir del laberinto. En la"
                    " puerta hay aparcado un ferrari espacial, te montas, es tu día de suerte, las llaves están puestas, "
                    "Huyes hacia el horizonte\nFIN")
        elif opcion == "B" and palo_en_inventario == False:
            print ("No tienes como subir, si solo tuvieras un palo... Pelo no lo tienes verdad? Así que finalmente te "
                    "quedas atrapado. \n\n Pasado un rato un monton de ratas aparecen y te devoranvivo. Es tu fin \n FIN")
else:
    print("No has elegido ninguna opción. Simplemente mueres")




