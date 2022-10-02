from time import sleep
import user_menu


def employee_register():
    # Path where is save the register list
    register_listTXT = 'list.txt'

    # Ending the register
    end_register = False

    # Register loop
    with open(register_listTXT, 'a') as listTXT:
        while (not end_register):
            # List of register
            reg_list(listTXT)

            sleep(2)

            end(listTXT)
            break

    close = input('Press ENTER for exit the module')

def reg_list(listTXT):

    print(" Type the informations about the employee do you want register!")
    identifier = int(input('Company Identifier (3 numbers): '))
    name = str(input('Full name: ')).title().strip()
    age = int(input('Age: '))
    position = str(input('Position (Director, Manager, Technican, Assistant): '))
    sleep(3)
    print('Register Successful!')

    # Salvar em TXT
    print(f'{identifier:==3} {name:<3} {age:<15} {position:<3}', file=listTXT)

def end(listTXT):
    more_one = int(input("""Do you want register more one employee?
(1) Yes
(2) No
Select the option: """))
    if more_one != 1:
        listTXT.close()

if (__name__ == '__main__'):
    employee_register()