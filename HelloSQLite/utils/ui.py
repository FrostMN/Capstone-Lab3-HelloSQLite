import HelloSQLite.utils.database as db
import HelloSQLite.utils.valid as valid


def main_menu():
    menu = """
    1: show jugglers
    2: add juggler
    3: edit juggler
    4: delete juggler
    5: quit
    """
    return menu


def show_menu(menu=None):
    if menu:
        print(menu)
    else:
        print(main_menu())


def get_option():
    choice = input("What option would you like to take? ")
    while True:
        if valid.int_input(choice):
            return int(choice)
        choice = input("PLease enter a valid number:")


def do_action(action):
    if action == 1:
        show_jugglers()
    elif action == 2:
        add_juggler()
    elif action == 3:
        edit_juggler()
    elif action == 4:
        delete_juggler()
    elif action == 5:
        quit()


def show_jugglers():
    print(db.get_jugglers())


def add_juggler():
    db.add_juggler()
    pass


def edit_juggler():
    pass


def delete_juggler():
    pass
