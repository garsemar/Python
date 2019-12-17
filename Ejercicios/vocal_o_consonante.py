"""
Numero de consonantes y vocales en una frase
"""

frase_del_usuario = input("Introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]

n_vocales = 0
n_consonantes = 0

for letra in frase_del_usuario:
    if letra in vocales:
        n_vocales += 1
    else:
        n_consonantes += 1

print("Hay {} vocales".format(n_vocales))
print("Hay {} consonantes".format(n_consonantes))