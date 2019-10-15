apetece_helado_input = input("Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("No te he entendido supondre que has dicho no")
    apetece_helado = False

tienes_dinero_input = input("Tienes dinero para un helado? (Si / No): ").upper()
esta_el_senyor_helados_input = input("Esta el senyor de los helados? (Si / No): ").upper()
esta_tu_tia_input = input("Estas con tu tia? (Si / No): ").upper()

tiene_dinero = tienes_dinero_input == "SI"
esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = tiene_dinero or esta_tu_tia
esta_el_senyor_helados = esta_el_senyor_helados_input == "SI"


if apetece_helado and puede_permitirselo and esta_el_senyor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")