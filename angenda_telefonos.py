
salida = False
agenda = dict()

while not salida:
    accion = input("Que quieres hacer? [Añadir numero[A] / Consultar numero[B] / Salir[C]]: ")

    # Accion agregar
    if accion.upper() == "A":
        print("Vamos a añadir un numero de telefono: ")
        print("--------------------------------------")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda[nombre] = numero

    # Accion consultar
    elif accion.upper() == "B":
        print("Vamos a consultar un numero: ")
        print("-----------------------------")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])

    # Accion salir
    elif accion.upper() == "C":
        salida = True
