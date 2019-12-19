"""
Obtener la tabla de multiplicar pero del 5 al 15 de un numero especificado  por el usuario
"""

numero_tabla = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range(5, 16):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))