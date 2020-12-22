import random
print ("Juego del mundo mágico\n"
        "----------------------\n"
        "\n"
        "Has sido reclutado por un grupo de magos de un mundo paralelo para que les ayudes en su lucha con las fuerzas oscuras que se quieren apoderar \n"
        "de su mundo. Recién llegas a su mundo, te incluyen en un ritual de iniciación junto a varios nuevos magos reclutados de diferentes mundos. \n"
        "En el ritual debes elegir cuál va a ser tu poder como mago, te dan 2 opciones para elegir \n"
        "\n"
        "Puedes tener la habilidad de hacerte invisible en cualquier momento o puedes tener la habilidad de teletransportarte al lugar que imagines \n")
opcion = input("[OPCION (A) - Invisibilidad] | [OPCION (B) - Teletransportación]: ")
if opcion == "A":
    print ("Has elegido la capacidad de hacerte invisible, veamos si eso es de utilidad en este mundo. Sales en compañía de otros dos magos hacía tu primera batalla, \n"
            "uno de ellos se teletransportó y el otro va volando, así que debes tomar un vehículo, para llegar al lugar donde se librará la batallas, tiens dos opciones, un dragón o bisonte")
    opcion = input ("[OPCION (A) - Volar en el dragón] | [OPCION (B) - Correr sobre el Bisonte]: ")
    if opcion == "A":
        print ("El dragón no simpatiza contigo y en pleno vuelo te deja caer, mueres antes de iniciar la batalla \n FIN")
    elif opcion == "B":
        print ("Es un bisonte bastante veloz, llegan justo a tiempo para iniciar la batalla, te encuentra un duende mágico que te ofrece una daga que puede llenar de luz a cuaqluier miembro de las fuerzas oscuras. \n"
                " Pero usarala tiene un costo muy alto, que solamente será revelado después de usarla, la aceptas?")
        opcion = input("[OPCION (A) - Si] | [OPCION (B)] - No]: ")
        if opcion == "A":
            print("Tomas la daga y avanzas hacía la batalla, enfrente hay dos guerreros de las fuerzas oscuras, uno de ellos tiene un gran espada y el otro un arco con felchas \n"
                "decides hacerte invisible y atacar a uno de ellos, ¿cuál atacas?")
            opcion = input("[OPCION (A) - El del arco]|[OPCION (B) -  El de la espada]")
            if opcion == "A":
                print ("Las flechas de este arco, tienen la capacidad de clavarse en el corazón de cualquiera que esté intentando atacar a su dueño, así que se te clava en el coreazón \n"
                        "mueres a los 20 minutos de forma lenta y dolorosa. \n FIN")
                exit()
            elif opcion == "B":
                print ("Utilizando tu capacidad de invisibilidad, te ubicas en la espalda de este guerrero y le clavas la daga, lo cual lo llena de luz, tanta luz que termina afectando a su compañero \n"
                        "ambos mueren, puedes continuar en busca del lider de las fuerzas oscuras")
        elif opcion == "B":
            print ("Eres sorprendido por un guerrero de las fuerzas oscuras y dado que no tienes armas para enfrentarlo este te elimina fácilmente \n FIN")
elif opcion == "B":
    print("Debes salir hacía la gran batalla junto a dos de tus nuevos compañeros, como te puedes teletransportar, decides llegar lo más pronto al lugar de la batalla. Utilizas una imagen que te mostraron, para imaginar el lugar al que quieres llegar "
            "llegas a una zona repleta de guerreros de las fuerzas oscuras, al verte rodeado decides saltar a otro lugar, como no conoces más lugares en este mundo, regresas a la base desde la que partiste \n"
            "sin embargo eres perseguido por miembros de las fuerzas oscuras y al llegar a la base te das cuenta que los debes enfrentar o debes intentar volver a teletransportarte al lugar de la batalla ¿ Qué haces?")
    opcion = input("[OPCION (A) - Enfrentarlos] | [OPCION (B) - Regresar al sitio de la batalla]: ")
    if opcion == "A":
        print("Por más que luchas, son demasiados y terminas siendo derrotado. \n FIN")
        exit()
    elif opcion == "B":
        print ("Al regresar logras llegar al mismo lugar donde se encuentran tus compañeros de batalla, ellos ya han eliminado algunos rivales, mientras vas caminando un duende mágico te ofrece una semilla que puede convertirse en cualquier arma que imagines, pero mientras utilizas esta arma no puedes teletransportarte ¿ la tomas?")
        opcion = input("[OPCION (A) - SI] | [OPCION (B) - NO]: ")
        semilla_en_inventario = False
        if opcion == "A":
            print("Coges la semilla")
            semilla_en_inventario = True
        elif opcion == "B":
            print ("No coges la semilla")
            semilla_en_inventario = False
        print ("Sigues adelante, encuentras una línea de defensa del ejercito oscuro ¿Estás decidido a enfrentarlos?")
        opcion = input("[OPCION (A) - SI] | [OPCION (B) - NO]: ")
        if opcion == "A" and semilla_en_inventario :
            print ("Utilizas la magia de la semilla e imaginando una cadena de andromeda con 1000 puntas letales. Puedes continuar en busca del lider de las fuerzas oscuras \n FIN")
        else:
            print("Mala elección no logras huir, son demasiados guerreros, te capturan y te eliminan \n FIN")

else:
    print("No has elegido ninguna opción. Simplemente mueres")




