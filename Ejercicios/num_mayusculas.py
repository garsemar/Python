"""
Numero de mayusculas en una frase
"""

frase_del_usuario = input("Introduce una frase: ")

n_mayus = 0

for letra in frase_del_usuario:
    if letra != " ":
        letra_mayus = letra.upper()
        if letra == letra_mayus:
            n_mayus += 1

print("Hay {} mayusculas".format(n_mayus))