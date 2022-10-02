# Home
from time import sleep
import register
import os

# Welcome Menu
def Usr_Menu():
    print('Matheus Rodrigues, Portugal - 2022.')
    print('')
    print('|--------------------|')
    print('|',' Employee Control ', '|')
    print('|--------------------|')

    print("""\n.Hi, im Matheus. This is a project its in the Alpha version. You function is essential for Human Resources.
Your modules is Employee Register and Delete e Employee Consult (id, name, age, position and salary). """)

# Select a function
    print('\nSelect what do you want do:')
    print("""
(1) Register Employee
(2) Delete Employee
(3) Consult Employee
(4) Exit""")

    option = int(input('\nSelect a option: '))
    while(option != 4):
        if option == 1:
            print('Loading Register Module, please wait...')
            sleep(2)
            os.system('cls')
            print('')
            print('|--------------------|')
            print('|', ' Register Module  ', '|')
            print('|--------------------|')
            print('')
            register.employee_register()
            break
        else:
            print(f'The chosen option still in the development. Wait for the new version. ')
            opcao = int(input('Select other option, please: '))
    print('\nThanks for the collaboration for the Alpha version for my program! Comments will be appreciated!')
    encerrar = str(input('\nPress ENTER for exit the program.'))

if __name__ == '__main__':
    Usr_Menu()