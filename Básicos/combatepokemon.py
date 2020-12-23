from random import randint

vida_inicial_pikachu = 80
vida_inicial_squirtle = 90

vida_pikachu = vida_inicial_pikachu
vida_squirtle = vida_inicial_squirtle

while vida_squirtle>0 and vida_pikachu > 0:
    # se desarrollan los turnos de combate
    
    
    # turno de pikachu

    print("Turno de Pikachu")
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        #bola voltio
        print("Pikachu ataca con bola voltio")
        vida_squirtle -= 10
    else :
        print("Pikachu ataca con onda trueno")
        vida_squirtle -= 11
    barras_de_vida_pikachu = int(vida_pikachu * 10 / vida_inicial_pikachu)
    print ("Pikachu:      [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu),vida_pikachu, vida_inicial_pikachu))

    barras_de_vida_squirtle = int(vida_squirtle * 10 / vida_inicial_squirtle)
    print ("Squirtle:     [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (10 - barras_de_vida_squirtle), vida_squirtle, vida_inicial_squirtle))

    input (" Enter para continuar... \n\n")

    #Turno para Squirtle
    print ("Turno Squirtle")

    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle !="B":
        ataque_squirtle = input("¿Qué ataque deseas realizar? [P]lacaje. Pistola [A]gua, [B]urbuja: ")

    if ataque_squirtle == "P":
        print("Squirtle ataca con placaje")
        vida_pikachu -= 10
    elif ataque_squirtle == "A":
        print("Squirtle ataca con Pistola de Agua")
        vida_pikachu -= 12
    elif ataque_squirtle == "B":
        print("Squirtle ataca con Burbuja")
        vida_pikachu -= 9

    barras_de_vida_pikachu = int(vida_pikachu * 10 / vida_inicial_pikachu)
    print ("Pikachu:      [{}{}] ({}/{})".format("*" * barras_de_vida_pikachu, " " * (10 - barras_de_vida_pikachu),vida_pikachu, vida_inicial_pikachu))

    barras_de_vida_squirtle = int(vida_squirtle * 10 / vida_inicial_squirtle)
    print ("Squirtle:     [{}{}] ({}/{})".format("*" * barras_de_vida_squirtle, " " * (10 - barras_de_vida_squirtle), vida_squirtle, vida_inicial_squirtle))

    input("Enter para continuar... \n\n")

if vida_pikachu > vida_squirtle:
    print("Pikachu gana!")
else:
    print("Squirtle gana!")

