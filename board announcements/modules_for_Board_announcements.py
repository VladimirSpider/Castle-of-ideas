import copy
admin_login = 'admin'
admin_password = 'admin'
my_list = []
users = {
    'login': {admin_login},
    'password': {admin_password}
}

def create_announcement(func):
    def wrapper(user):
        print("\nРазмещение объявления!")
        rule = ["Введите сегодняшнее число: ", "Введите сегодняшний месяц: ", "Введите своё объявление: ", "Введите ваше имя: "]
        for el in rule:
            new = input(el)
            my_list.append(str(new))
        func(user)
        my_list.clear()
        print("Объявление размещено!")
    return wrapper

@create_announcement
def add_in_file(user):
    f = open("announcements.txt", "a")
    for el in my_list:
        f.write(el + '\n')
    f.write(user + '\n')
    f.close()

def read_announcement():
    output_rule = ["День", "Месяц", "Обявление", "Имя"]
    f = open("announcements.txt", "r")
    print()
    for el in output_rule:
        print(el, end = " " * 10)
    count = 0
    print("\n")
    for line in f:
        count += 1
        if count == 1:
            number = (len(output_rule[0]) - (len(line)-1)) + 10
            print(line.replace('\n', ''), end = " " * number)
        elif count == 2:
            number = (len(output_rule[1]) - (len(line) - 1)) + 10
            print(line.replace('\n', ''), end=" " * number)
        elif count == 3:
            number = (len(output_rule[2]) - (len(line) - 1)) + 10
            print(line.replace('\n', ''), end=" " * number)
        elif count == 4:
            print(line.replace('\n', ''))
        elif count == 5:
            count = 0
    f.close()

#Авторизация
def authorization(func):
    def wrapper():
        print("\nАвторизация!")
        user = "user"
        log_in = []
        func()
        rule_create_profile = ["Введите ваш логин: ", "Введите ваш пароль: "]
        while True:
            for el in rule_create_profile:
                while True:
                    my_txt = input(el)
                    if " " in  my_txt or len(my_txt) == 0 or len(my_txt) > 10:
                        print("-Логин и пароль не должны содержать ' '."
                              "\n-Длина логина и пароля не может быть равна 0 символов"
                              "\nи не должна превышать длину в 10 символов.")
                    else:
                        log_in.append(my_txt)
                        break
            a = False
            a_name_user = ""
            b = False
            a_admin = False
            b_admin = False
            count = 0
            for el in log_in:
                count += 1
                if el in users['login'] and count == 1:
                    a = True
                    a_name_user = el
                    if el == admin_login:
                        a_admin = True
                if el in users['password'] and count == 2:
                    b = True
                    if el == admin_password:
                        b_admin = True
            if a_admin and b_admin:
                print("Вы вошли как администратор!")
                user = "administrator"
                break
            elif a and b:
                print("Вы вошли!")
                user = a_name_user
                break
            else:
                print("Вы ввели неправильный логин или пароль!"
                      "\nПопробуйте ещё раз!")
                log_in.clear()
        print("Авторизация прошла успешно!")
        return user
    return wrapper

@authorization
def our_users():
    f = open("users.txt", "r")
    count = 0
    for line in f:
        count += 1
        if count == 1 and line not in users['login']:
            users['login'].add(line.replace('\n', ''))
        elif count == 2 and line not in users['password']:
            users['password'].add(line.replace('\n', ''))
            count = 0
    f.close()

#Создание профиля(Логин пароль)
def main_create_profile(func):
    def wrapper():
        print("\nРегистрация!")
        func()
        print("Вы зарегистрировались!")
    return wrapper

@main_create_profile
def create_profile():
    f = open("users.txt", "a")
    rule_create_profile = ["Введите ваш логин: ", "Введите ваш пароль: "]
    for el in rule_create_profile:
        while True:
            my_txt = input(el)
            if " " in my_txt or len(my_txt) == 0 or len(my_txt) > 10:
                print("-Логин и пароль не должны содержать ' '."
                      "\n-Длина логина и пароля не может быть равна 0 символов"
                      "\nи не должна превышать длину в 10 символов.")
            else:
                f.write(my_txt + '\n')
                break
    f.close()

#Удаление объявления
def delete_announcement(user):
    f = open("announcements.txt", "r")
    your_announcement = []
    all_your_announcements = []
    count = 0
    for line in f:
        count += 1
        your_announcement.append(line.replace('\n', ''))
        if count == 5:
            if user == your_announcement[count-1]:
                all_your_announcements.append(list(your_announcement))
                all_your_announcements[len(all_your_announcements) - 1].insert(0,(str(len(all_your_announcements)) + ":"))
            your_announcement.clear()
            count = 0
    f.close()
    if len(all_your_announcements) == 0:
        print("У вас нету объявлений.")
    else:
        print("ВАШИ ОБЪЯВЛЕНИЯ:")
        output_rule = ["№", "День", "Месяц", "Обявление", "Имя", "Пользователь"]
        print()
        for el in output_rule:
            print(el, end=" " * 10)
        count = 0
        print("\n")
        for el_outer in all_your_announcements:
            for el_inner in el_outer:
                if count < 5:
                    number = (len(output_rule[count]) - len(el_inner)) + 10
                    print(el_inner, end=" " * number)
                    count += 1
                elif count == 5:
                    print(el_inner)
                    count = 0
        while True:
            print("Какое объявление вы хотите удалить?")
            answer = input("№: ")
            try:
                it_is_int = int(answer)
                if 0 < it_is_int <= len(all_your_announcements):
                    copy_all_your_announcements = copy.deepcopy(all_your_announcements)
                    for el in copy_all_your_announcements:
                        if (answer + ":") not in el:
                            all_your_announcements.remove(el)
                    all_your_announcements[0].remove(answer + ":")
                    break
                else:
                    print("Введите целое не отрицательное число(номер объявления, которое вы хотите удалить)!")
            except ValueError:
                print("\nВведите целое не отрицательное число(номер объявления, которое вы хотите удалить)!")
        f = open("announcements.txt", "r")
        announcement = []
        all_announcements = []
        count = 0
        for line in f:
            count += 1
            announcement.append(line.replace('\n', ''))
            if count == 5:
                all_announcements.append(list(announcement))
                announcement.clear()
                count = 0
        f.close()
        f = open("announcements.txt", "w")
        for el_outer in all_announcements:
            if el_outer != all_your_announcements[0]:
                for el_inner in el_outer:
                    f.write(el_inner + '\n')
        f.close()

#Удаление пользователя
def admin():
    list_for_admin = []
    technical_list = []
    count = 0
    f = open("announcements.txt", "r")
    for line in f:
        count += 1
        technical_list.append(line.replace('\n', ''))
        if count == 5:
            count = 0
            list_for_admin.append(list(technical_list))
            list_for_admin[len(list_for_admin) - 1].insert(0, (str(len(list_for_admin)) + ":"))
            technical_list.clear()
    f.close()
    if len(list_for_admin) == 0:
        print("Нету объявлений пользователей в базе данных."
              "Пользователя не за что удалять.")
    else:
        print("\nВСЯ ДОСКА ОБЪЯВЛЕНИЙ:")
        output_rule = ["№", "День", "Месяц", "Обявление", "Имя", "Пользователь"]
        print()
        for el in output_rule:
            print(el, end=" " * 10)
        count = 0
        print("\n")
        for el_outer in list_for_admin:
            for el_inner in el_outer:
                if count < 5:
                    number = (len(output_rule[count]) - len(el_inner)) + 10
                    print(el_inner, end=" " * number)
                    count += 1
                elif count == 5:
                    print(el_inner)
                    count = 0
        print("\n")
        print("Введите имя пользователя, которого вы хотите удалить."
              "\nПри удалении пользователя удаляются все его объявления.")
        variable = True
        while variable:
            answer = input("Введите имя пользователя: ")
            for el in list_for_admin:
                if answer == el[len(el) - 1] and answer != admin_login:
                    variable = False
            if variable:
                print("Такого пользователя нет в базе!")
        f = open("announcements.txt", "r")
        announcement = []
        all_announcements = []
        count = 0
        for line in f:
            count += 1
            announcement.append(line.replace('\n', ''))
            if count == 5:
                all_announcements.append(list(announcement))
                announcement.clear()
                count = 0
        f.close()
        f = open("users.txt", "r")
        user = []
        all_users = []
        count = 0
        for line in f:
            count += 1
            user.append(line.replace('\n', ''))
            if count == 2:
                all_users.append(list(user))
                user.clear()
                count = 0
        f.close()
        f = open("announcements.txt", "w")
        for el_outer in all_announcements:
            if answer not in el_outer:
                for el_inner in el_outer:
                    f.write(el_inner + '\n')
        f.close()
        f = open("users.txt", "w")
        for el_outer in all_users:
            if answer not in el_outer:
                for el_inner in el_outer:
                    f.write(el_inner + '\n')
        f.close()

