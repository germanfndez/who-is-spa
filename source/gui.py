import time
from settings import *
from user import user

def main():
    while True:
        print(GWORK_NAME)
        print("Selecciona")
        print("[1] Login")
        print("[2] Register")
        print("[3] Exit")

        try:
            action = int(input("Acction: "))
            if action == 1:
                email = str(input("Email : "))
                password = str(input("Password : "))
            elif action == 2:
                name = str(input("Name : "))
                email = str(input("Email : "))
                password = str(input("Password : "))
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
