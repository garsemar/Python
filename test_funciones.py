def input_con_confirmacion(pregunta):
    confirmacion = False
    dato_usuario = ""
    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, Estas seguro? [Si / No]".format(dato_usuario))
        if seguro.upper() == "SI":
            confirmacion = True
    return dato_usuario

nombre = input_con_confirmacion("Como")
print("Has confirmado que te llamas {}".format(nombre))