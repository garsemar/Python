import pickle
from tkinter import *
from tkinter import ttk
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACT = 4
ACTION_EXIT = 5

SAVE_FILE_NAME = "contacts.save"

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACT, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("Que opcion deseas? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponibles: ")
    print("1 - Añadir contactos")
    print("2 - Eliminar contactos")
    print("3 - Buscar un contacto")
    print("4 - Exportar contactos a un CSV")
    print("5 - Salir")
    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Telefono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def remove_contact(contacts):
    pass


def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introducir nombre del contacto o parte de el: ")
    found_contacts = []

    print("He encontrado los siguientes contactos: ")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{} - {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se ha encontrado ninguno.")
        return

    print("\nInformacion sobre {}\n".format(found_contacts[contact_index]["name"]))
    print("Nombre: {name}, Telefono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))
    sleep(2)


def export_contact():
    pass


def load_contacts():
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb"))
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)
    print("Contactos guardados correctamente.")


def main():
    root = Tk()
    frame_add_contacts = ttk.Frame(root, padding="12 12 12 12")
    frame_add_contacts.grid()

    feet_entry = ttk.Entry(frame_add_contacts, width=7, textvariable=feet)
    feet_entry.grid(column=2, row=1, sticky=(W, E))
    ttk.Label(frame_add_contacts, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
    ttk.Button(frame_add_contacts, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

    contact_list = ttk.Frame(root, padding="12 12 12 12")
    contact_list.grid()

if __name__ == "__main__":
    main()
