"""
Cuenta cuantos numeros hay en una lista introducida por el usuario
"""

numeros_usuario = []
numero_del_usuario = ""
while numero_del_usuario != "Fin":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un numero(Fin para terminar): ")
        if numero_del_usuario == "Fin":
            break
        elif not numero_del_usuario.isdigit():
            numero_del_usuario = ""
        else:
            numeros_usuario.append(int(numero_del_usuario))
            numero_del_usuario = ""
            print("Numero añadido!")
numero_numeros = 0

for numero in numeros_usuario:
    numero_numeros += 1

print("Hay {} numeros en la lista".format(numero_numeros))