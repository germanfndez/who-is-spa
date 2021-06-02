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
                    break

            elif action == 2:
                name = str(input("Name : "))
                email = str(input("Email : "))
                password = str(input("Password : "))
                if user.register(name, email, password):
                    inApp(user)
                    break

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
                if (len(user.homeworksObj.homeworks) > 0):
                    for homework in user.homeworksObj.homeworks:
                        today = 6
                        isHomeworkLate = "NOT Late"
                        if today > int(homework[5]): 
                            isHomeworkLate = "LATE"

                        print(f"{homework[1]} | {homework[2]} | {isHomeworkLate}")
                else:
                    print("No tienes ningun homework anotado")

            elif action == 2:
                print("modify")

            elif action == 3:
                try:
                    homeworkId = int(input("Homework id to delete: "))
                    user.homeworksObj.deleteHomework(homeworkId)
                except:
                    print("Ha ocurrido un error, intentalo de nuevo")
                    time.sleep(3)

            elif action == 4:
                print("loadoug")
                del user
                main()
                break
            else:
                print("Opcion no encontrada")
                time.sleep(5)
        except:
            print("Ha ocurrido un error, intentalo de nuevo")
            time.sleep(3)
            inApp(user)
            break

