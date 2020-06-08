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


def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    print("Contacto añadido correctamente.")
    return contact


def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, rows = frame_contact_list.grid_size()
    ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=rows)
    ttk.Label(frame_contact_list, text=contact["email"]).grid(column=2, row=rows)
    ttk.Label(frame_contact_list, text=contact["phone"]).grid(column=3, row=rows)


def ask_new_contacts(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "), input("Telefono: "), input("Email: "))

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
    contacts = []

    root = Tk()
    frame_add_contacts = ttk.Frame(root, padding="25 20 25 20")
    frame_add_contacts.grid()
    frame_add_contacts.grid_configure(padx=5, pady=2)

    frame_contact_list = ttk.Frame(root, padding="12 12 12 12")
    frame_contact_list.grid()

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    ttk.Label(frame_add_contacts, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_add_contacts, text="Email").grid(column=2, row=1)
    ttk.Label(frame_add_contacts, text="Telefono").grid(column=3, row=1)

    ttk.Entry(frame_add_contacts, width=15, textvariable=name).grid(column=1, row=2)
    ttk.Entry(frame_add_contacts, width=15, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contacts, width=15, textvariable=phone).grid(column=3, row=2)

    ttk.Label(frame_contact_list, text="Nombre").grid(column=1, row=1, sticky=W)
    ttk.Label(frame_contact_list, text="Email").grid(column=2, row=1, sticky=W)
    ttk.Label(frame_contact_list, text="Telefono").grid(column=3, row=1, sticky=W)

    ttk.Button(frame_add_contacts,
               text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3, sticky=E)
    root.mainloop()

if __name__ == "__main__":
    main()
