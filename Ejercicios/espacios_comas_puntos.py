"""
Numero de espacios, comas y puntos en una frase
"""

frase_del_usuario = input("Introduce una frase: ")

n_espacios = 0
n_comas = 0
n_puntos = 0

for simbolo in frase_del_usuario:
    if simbolo == " ":
        n_espacios += 1
    elif simbolo == ",":
        n_comas += 1
    elif simbolo == ".":
        n_puntos += 1

print("Hay {} espacios".format(n_espacios))
print("Hay {} comas".format(n_comas))
print("Hay {} puntos".format(n_puntos))