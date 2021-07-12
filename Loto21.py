import random, copy
loto = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
        ]
tickets_loto = []
all_numbers = [
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
                [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
                [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
                [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
                [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
                [81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
                ]
number_tickets  = input("Введите число билетов для создания: ")
our_count = 0
while our_count < int(number_tickets):
    '''loto = [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]
    all_numbers = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
        [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
        [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
        [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
        [81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    ]'''
    k = 0
    all_number_in_column = 0
    list_number_in_column = []
    while k < 9:
        k += 1
        number_in_column = random.randint(1,6)
        list_number_in_column.append(number_in_column)
        all_number_in_column += number_in_column
        if k == 9:
            if all_number_in_column != 30:
                k = 0
                list_number_in_column.clear()
                all_number_in_column = 0
            elif all_number_in_column == 30:
                print("-", all_number_in_column)
                print("-", list_number_in_column)
    k = 0
    #all_numbers_copy = all_numbers.copy()
    #loto_copy = loto.copy()
    #all_numbers_copy = all_numbers[:]
    #loto_copy = loto[:]
    all_numbers_copy = copy.deepcopy(all_numbers)
    loto_copy = copy.deepcopy(loto)
    print(all_numbers)
    print(all_numbers_copy)
    print(loto)
    print(loto_copy)
    for i in range(0,len(all_numbers_copy)):
        for count in range(0, list_number_in_column[k]):
            our_number = random.choice(all_numbers_copy[i])
            all_numbers_copy[i].remove(our_number)
            loto_copy[k].append(our_number)
            if len(loto_copy[k]) < 6 and count == list_number_in_column[k] - 1:
                while len(loto_copy[k]) < 6:
                    loto_copy[k].append(0)
            if count == list_number_in_column[k] - 1:
                random.shuffle(loto_copy[k])
                k += 1
    print(all_numbers)
    print(all_numbers_copy)
    print(loto)
    print(loto_copy)
    if len(tickets_loto) < 1:
        tickets_loto.append(loto_copy)
        our_count += 1
    elif len(tickets_loto) > 0:
        for el in tickets_loto:
            if el != loto_copy:
                if tickets_loto.index(el) == (len(tickets_loto) - 1):
                    our_count += 1
                    tickets_loto.append(loto_copy)
            else:
                our_count += 0
                break
    print(tickets_loto)
    print(our_count)
k = 0
print("\n")
print("--LOTO--")
for number_ticket in tickets_loto:
    print("-- Ticket", tickets_loto.index(number_ticket)+1, "--")
    for i in range(0,6):
        for j in range(0,len(number_ticket)):
            print("|",number_ticket[j][i], end = "")
            if number_ticket[j][i]>9:
                print(" |",end = "")
            else:
                print("  |", end="")
        if i == 2:
            print("\n")
        print("\n")
    print("\n")