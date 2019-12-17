"""
Escribir las vocales de una frase
"""

frase_del_usuario = input("Introduce una frase: ")

vocales = ["a", "e", "i", "o", "u"]
vocales_print = []

n_vocales = 0
n_consonantes = 0

for letra in frase_del_usuario:
    if letra in vocales:
        vocales_print.append(letra)

print("Las vocales de la frase son: {}".format(vocales_print))