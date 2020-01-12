"""
Programa un codigo que utilizando el metodo replace de las strings me sustituya las claves de mi string inicial por los
valores en orden de una lista.
"""

valores_a_sustituir = [1, 2, "hola", "adios"]
string_a_canviar = "Hola, numero {}, numero {}, {} y {}"

for valor in valores_a_sustituir:
    string_a_canviar = string_a_canviar.replace("{}", str(valor), 1)

print(string_a_canviar)