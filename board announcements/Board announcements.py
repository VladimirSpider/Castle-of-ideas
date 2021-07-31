from modules_for_Board_announcements import add_in_file, read_announcement, our_users, create_profile, delete_announcement, admin

print("Добро пожаловать на нашу площадку объявлений."
      "\nОбявления могут размещать только зарегистри-"
      "\nрованные пользователи.")
user = ""
while True:
    print("\nПользователь:", user)
    if user != "" and user !="administrator":
        print("\n1: Просмотр объявлений."
              "\n2: Выйти."
              "\n3: Покинуть площадку."
              "\n4: Разместить объявление."
              "\n5: Удалить объявление.")
    elif user == "administrator":
        print("\n1: Просмотр объявлений."
              "\n2: Выйти."
              "\n3: Покинуть площадку."
              "\n4: Удалить пользователя.")
    elif user == "":
        print("\n1: Просмотр объявлений."
              "\n2: Войти."
              "\n3: Покинуть площадку.")
    answer = input("Ваш ответ: ")
    if answer == '1':
        print("\nНАША ДОСКА ОБЪЯВЛЕНИЙ!!!")
        read_announcement()
    elif answer == '2' and user == "":
        while True:
            print("\nУ вас есть профиль?(y/n)")
            answer = input("Ваш ответ: ")
            if answer.lower() == 'y':
                user = our_users()
                break
            elif answer.lower() == 'n':
                create_profile()
                break
            else:
                print("Вы должны ввести 'y' или 'n'.")
    elif answer == '2' and user != "":
        user = ""
        print("Вы вышли из своего профиля!")
    elif answer == '3':
        print("Всего доброго.")
        break
    elif answer == '4' and user != "" and user !="administrator":
        add_in_file(user)
    elif answer == '4' and user == "administrator":
        print("Удаление пользователя")
        admin()
        print("Пользователь удалеён!")
    elif answer == '5' and user != "" and user !="administrator":
        print("\nУдаление объявления!")
        delete_announcement(user)
        print("\nОбъявление удалено!")
    else:
        if user != "" and user !="administrator":
            print("Вы должны ввести '1', '2', '3', '4' или '5'.")
        elif user =="administrator":
            print("Вы должны ввести '1', '2', '3' или '4'.")
        else:
            print("Вы должны ввести '1', '2' или '3'.")







