import copy
vegetables = ["Томат", "Огурец", "Лук", "Картофель", "Капуста цветная", "Петрушка", "Кабачок"]
calorie_content = (19, 15, 43, 83, 29, 45, 27)
cost = (2, 1.5, 1, 1, 2.5, 2.5, 2)
salad = {}
vegetables_calorie_content = {
    "Томат" : 19,
    "Огурец" : 15,
    "Лук" : 43,
    "Картофель" : 83,
    "Капуста цветная" : 29,
    "Петрушка" : 45,
    "Кабачок" : 27
}
vegetables_cost = {
    "Томат" : 2,
    "Огурец" : 1.5,
    "Лук" : 1,
    "Картофель" : 1,
    "Капуста цветная" : 2.5,
    "Петрушка" : 2.5,
    "Кабачок" : 2
}
while True:
    i_am_chef = input("Ты шеф-повар?(y/n)")
    if i_am_chef.lower() == "y":
        while True:
            print("Вот список овощей, имеющихся на вашей кухне.")
            print("-" * 50)
            for el in vegetables:
                print(vegetables.index(el) + 1, ")", el, "(цена -", cost[vegetables.index(el)],
                      "$, калорийность -", calorie_content[vegetables.index(el)], "кал.)")
            print("-" * 50)
            i_want = input("Хочешь добавить ещё овощей на свою кухню?(y/n)")
            if i_want.lower() == "y":
                add_vegetable = input("Введи овощ, который хочешь добавить: ")
                add_vegetable_cost = int(input("Введи стоимость добавляемого овоща: "))
                add_vegetable_calorie_content = int(input("Введи калорийность добавляемого овоща: "))
                vegetables.append(add_vegetable)
                cost_list = []
                for i in cost:
                    cost_list.append(i)
                cost_list.append(add_vegetable_cost)
                cost = tuple(cost_list)
                calorie_content_list = []
                for i in calorie_content:
                    calorie_content_list.append(i)
                calorie_content_list.append(add_vegetable_calorie_content)
                calorie_content = tuple(calorie_content_list)
                vegetables_cost[add_vegetable] = add_vegetable_cost
                vegetables_calorie_content[add_vegetable] = add_vegetable_calorie_content
            elif i_want.lower() == "n":
                print("Тогда читай дальше")
                break
            else:
                print("Вы должны ввести 'y' или 'n'")
        break
    elif i_am_chef.lower() == "n":
        print("Тогда читай дальше")
        break
    else:
        print("Вы должны ввести 'y' или 'n'")
print("\nИерархия овощей согласно стоимости:\n")
copy_vegetables = copy.deepcopy(vegetables)
for value in sorted(vegetables_cost.values()):
    for key in copy_vegetables:
        if vegetables_cost[key] == value:
            copy_vegetables.remove(key)
            print(key, "-", value, "$")
print("\nИерархия овощей согласно калорийности:\n")
copy_vegetables = copy.deepcopy(vegetables)
for value in sorted(vegetables_calorie_content.values()):
    for key in copy_vegetables:
        if vegetables_calorie_content[key] == value:
            copy_vegetables.remove(key)
            print(key, "-", value, "кал.")
while True:
    our_answer = input("Хотите сделать салат(y/n): ")
    if our_answer.lower() == "y":
        print("Сделайте свой салат из овощей, находящихся в иерархии!")
        while True:
            our_vegetable = input("Введите название овоща или закончите делать салат('название овоща'/e): ")
            if our_vegetable.lower() != "e":
                if our_vegetable in vegetables_calorie_content:
                    if our_vegetable not in salad:
                        salad[our_vegetable] = vegetables_calorie_content[our_vegetable]
                    elif our_vegetable in salad:
                        print("Этот овощ уже в салате, добавьте другой овощ!")
                else:
                    print("Такого овоща нет в иерархии!")
            elif our_vegetable.lower() == "e":
                if len(salad) > 0:
                    print("Вот какой рецепт салата у тебя получился:")
                    for key in salad:
                        print(key)
                    print("Сортировка овощей в салате на основе калорийности:")
                    copy_vegetables = copy.deepcopy(vegetables)
                    for value in sorted(salad.values()):
                        for key in copy_vegetables:
                            if key in salad:
                                if salad[key] == value:
                                    copy_vegetables.remove(key)
                                    print(key, "-", value, "кал.")
                    break
                elif len(salad) == 0:
                    print("Ты не сделал свой салат. Пока!")
                    break
        break
    elif our_answer.lower() == "n":
        print("Пока")
        break
    else:
        print("Вы должны ввести 'y' или 'n'")
if len(salad) != 0:
    while True:
        my_answer = input("Хочешь найти овощи в салате, соответствующие заданному диапазону калорийности(y/n)?")
        if my_answer.lower() == "y":
            print("Овощи в салате из какого диапазона вам интересны"
                  "(введите положительные целые числа от 0 до необходимого вам значения)")
            while True:
                my_calorie_content_1 = input("Нижний диапазон:")
                my_calorie_content_2 = input("Верхнийний диапазон:")
                if my_calorie_content_1.isnumeric() and my_calorie_content_2.isnumeric():
                    count = 0
                    for value_calorie in salad.values():
                        if int(my_calorie_content_1) <= value_calorie <= int(my_calorie_content_2):
                            for key in salad:
                                if salad[key] == value_calorie:
                                    print("Овощ", key, ", содержащий", salad[key], "кал., "
                                          "лежит в вашем диапазоне от", my_calorie_content_1, "до", my_calorie_content_2)
                                    count += 1

                    if count == 0:
                        print("Овощ, содержащий колличество калорий "
                              "в вашем диапазоне от", my_calorie_content_1, "до",my_calorie_content_2,
                              "отсутствует в салате!")
                        break
                    break
                else:
                    print("введите положительные целые числа от 0 до необходимого вам значения")
        elif my_answer.lower() == "n":
            print("Пока!")
            break
        else:
            print("Вы должны ввести 'y' или 'n'")