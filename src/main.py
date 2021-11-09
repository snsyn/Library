from menus import Menus
from utils import cli_cleaner
from browse import Booklist


def about():
    while True:
        cli_cleaner()
        print(
            'This program has the objective of reviewing from basic python concepts to advanced ones by means of '
            'creating a library which functionality will gradually increase\n')
        print('(Q)uit')
        action = input()
        if action == 'Q':
            break


# Main
def main():
    menu_Printer = Menus()
    option = 0
    while option != 3:
        cli_cleaner()
        print('Welcome to the library.')
        print('Please, select an option')
        menu_Printer.printMenu('main')
        option = input()
        if option == '1':
            browse = Booklist()
            browse.browse()
        elif option == '2':
            about()
        elif option == '3':
            break

    cli_cleaner()
    print('Thanks for visiting the library')


if __name__ == '__main__':
    main()

