import pickle
from time import sleep

ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_SCHEDULE = 4
ACTION_EXIT = 5

ACTION_YES = 1
ACTION_NO = 2
ACTION_CANCEL = 100

ELECTION_YES_NO_CANCEL = [ACTION_YES, ACTION_NO, ACTION_CANCEL]
ELECTION_YES_NO = [ACTION_YES, ACTION_NO]

SAVE_FILE_NAME = "Agenda Contactos.xnor"
MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_SCHEDULE, ACTION_EXIT]


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and (int(selected_action) not in options)):
        selected_action = input("¿Qué quieres hacer?:   ")
    ''' como siempre, es equivalente a:
    while selected_action.isdigit() == false or (selected_action.isdigit() == true and (int(selected_action) not in MENU_OPTIONS))
    '''
    return int(selected_action)


def show_menu():
    print("Acciones disponibles:")
    print("=====================")
    print("1.- Añadir contacto")
    print("2.- Eliminar contacto")
    print("3.- Buscar contacto")
    print("4.- Exportar agenda a CSV")
    print("5.- Salir")

    return ask_until_option_expected(MENU_OPTIONS)

def add_contact(contact_list):
    print("\n\nAñadir Contacto:\n")
    #  contact es un diccionario (clave-valor) que irá dentro de una lista que los contendrá a todos.
    contact = {
        "name": (input("Nombre: ")).upper(),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contact_list.append(contact)
    print("Se ha añadido el contacto {} a la lista de contactos!.".format(contact["name"]))
    #  recordar que es un diccionario, por lo que los valores que hay en su interior se invocan llamando a su clave
    sleep(2)


def remove_contact(contact_list):
    print("\n\nEliminar Contacto: \n")
    search_term = (input("Introduce el nombre del contacto (o parte de él) que deseas eliminar de la agenda: ")).upper()
    found_contacts = []
    print("Con esos datos se han encontrado los siguientes contactos: ")

    for i in contact_list:
        if i["name"].find(search_term) >= 0: # recordar que da -1 si no lo ha encontrado
            found_contacts.append(i)
            print("Quieres borrar el contacto:\n {} con teléfono {} y email {}".format(i["name"], i["phone"], i["email"]))
            print("================================")
            print("1.- Sí, borrar\n2.- No, buscar siguiente\n100.-No, y dejar de buscar\n\n")
            election = ask_until_option_expected(ELECTION_YES_NO_CANCEL)

            #  si se elige 1 se borra el contacto, si se elige 3 se cancela la búsqueda y se vuelve al menú
            #  y si se elige 2, el programa sigue buscando la siguiente coincidencia
            if election == ACTION_YES:
                contact_list.remove(i)
                print("Contacto eliminado!!")
                sleep(2)
                return
            elif election == ACTION_CANCEL:
                print("Búsqueda para eliminación cancelada!")
                sleep(2)
                return
    print("No quedan más contactos que coincidan con los criterios aportados; realiza otra búsqueda o vuelve al menú:")
    print("1.- Realizar otra búsqueda\n2.-Volver al menú")
    question_repeat = ask_until_option_expected(ELECTION_YES_NO)

    if question_repeat == ACTION_YES:
        remove_contact(contact_list)
    else:
        print("Búsqueda para eliminación cancelada!")
        sleep(2)
        return



def find_contact(contact_list):
    print("\n\nBuscar Contacto:\n")
    search_term = (input("Introduce el nombre del contacto, o una parte de él: ")).upper()
    found_contacts = []

    print("Con esos datos se han encontrado los siguientes contactos: ")
    numbers_menu = [100] #se introduce prematuramente la opción 100 para cancelar
    contact_counter = 0
    for i in contact_list:
        if i["name"].find(search_term) >= 0:  # recordar que -1 es que no lo ha encontrado
            found_contacts.append(i)
            print("{} - {}".format(contact_counter, i["name"]))
            numbers_menu.append(contact_counter)
            contact_counter += 1

    contact_index = 0  #  índice a los únicos efectos de la lista 'virtual' para el usuario

    if len(numbers_menu) > 2:
        contact_index = ask_until_option_expected(numbers_menu)
    elif len(numbers_menu) > 50: # si hay un huevo de coincidencias, que te mande volver a buscar otra vez
        print("Hay demasiadas coincidencias (>50), introduce nuevamente los criterios de búsqueda")
        find_contact(contact_list)
    elif len(numbers_menu) == 1:
        print("No se ha encontrado ninguna coincidencia con tus contactos")
        print("\n Quieres realizar otra búsqueda?\n1.- Sí\n2.- No(regresar al menú)")
        question_repeat = ask_until_option_expected(ELECTION_YES_NO)
        if question_repeat == ACTION_YES:  #  yes
            find_contact(contact_list)
        elif question_repeat == ACTION_NO:  #  no
            return

    if contact_index == 100:
        print("Volviendo al menú principal")
        sleep(2)
        return

    print("Contact_Index= " + str(contact_index))
    print("Largo_lista= "+ str(len(found_contacts)))

    print("\nInformación sobre el contacto\n")
    try:
        print("Nombre: {name}\nTeléfono: {phone} \nEmail: {email}\n\n".format(**found_contacts[contact_index]))
    except:
        print("Error inesperado")
    sleep(5)

    del numbers_menu  # para reiniciar la variable
    del found_contacts  #  idem
    del contact_counter  #  idem de idem



def export_schedule():
    pass


def load_contacts():
    print("Cargando datos del programa...")
    sleep(0.5)
    print("...")
    sleep(0.5)
    try:
        return pickle.load(open(SAVE_FILE_NAME, "rb")) #cargar el save file y devuelve los datos
    except FileNotFoundError:
        return []




def save_contacts(contact_list):
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contact_list, save_file) #volcar en el save_file lo que contenga la variable contact_list
    print("Datos guardados correctamente!")


def main():
    contact_list = load_contacts()
    action = show_menu()

    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contact_list)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contact_list)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contact_list)
        elif action == ACTION_EXPORT_SCHEDULE:
            export_schedule()

        action = show_menu()

    save_contacts(contact_list)


# esto llamará automáticamente a la función main() al ejecutar este archivo
if __name__ == "__main__":
    main()
