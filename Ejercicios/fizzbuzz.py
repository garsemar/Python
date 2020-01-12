"""
Dada una lista de enteros:
Vamos a sustituir los multiplos de 3 por un Fizz
Y los multiplos de 5 sustituir por un Buzz
Multiplos de 3 y de 5, vamos a sustituirlos por un FizzBuzz
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20, 15, 30, 60, 70]

for indice in range(len(numeros)):
    numero = numeros[indice]

    if numero % 3 == 0 or numero % 5 == 0:
        numeros[indice] = ""
        
        if numero % 3 == 0:
            numeros[indice] += "Fizz"

        if numero % 5 == 0:
            numeros[indice] += "Buzz"

print(numeros)