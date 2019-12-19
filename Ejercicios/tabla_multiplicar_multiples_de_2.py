"""
Obtener la tabla de multiplicar de un numero especificado por el usuario pero multiple de 2
"""

numero_tabla = int(input("De que numero quieres la tabla de multiplicar: "))

for multiplo in range(1, 11):
    if multiplo % 2 == 0:
        mul = multiplo / 2
        print(mul)