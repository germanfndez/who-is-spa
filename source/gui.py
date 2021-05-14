import logging
import time
from settings import *
from user import User

logged = None

def main():
    logged = False
    while not logged:
        print(GWORK_NAME)
        print("Selecciona")
        print("[1] Login")
        print("[2] Register")
        print("[3] Exit")

        try:
            user = User()
            action = int(input("Acction: "))
            if action == 1:
                email = str(input("Email : "))
                password = str(input("Password : "))
                if user.login(email, password):
                    inApp(user)

            elif action == 2:
                name = str(input("Name : "))
                email = str(input("Email : "))
                password = str(input("Password : "))
                user = User()
                if user.register(name, email, password):
                    inApp(user)

            elif action == 3:
                break
            else:
                print("Opcion no encontrada")
                time.sleep(5)
        except:
            print("Ha ocurrido un error, intentalo de nuevo")
            time.sleep(3)
            main()
            break

def inApp(user):
    logged = True
    while logged:
        print(f'{GWORK_NAME} | {user.name}')
        print("Selecciona")
        print("[1] Show homeworks")
        print("[2] Modify homework")
        print("[3] Delete homework")
        print("[4] Loadout")
        print("[5] Exit")

        try:
            action = int(input("Acction: "))
            if action == 1:
                print("homeworks")
                print(user.homeworksObj.homeworks)

            elif action == 2:
                print("modify")

            elif action == 3:
                print("delete")
            elif action == 4:
                print("loadoug")
                del user
                main()
            else:
                print("Opcion no encontrada")
                time.sleep(5)
        except:
            print("Ha ocurrido un error, intentalo de nuevo")
            time.sleep(3)
            main()
            break

