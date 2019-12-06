mi_lista = []
input_usuario = input("Que necesitas comprar? (Escribe FIN para salir): ")

while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario = input("Que necesitas comprar? (Escribe FIN para salir): ")

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de la compra")