import random
new_list_a = []
new_list_b = []
new_list_c = []
new_list_d = []
new_list_e = []
new_list_f = []
new_list_g = []
new_list_h = []
new_list_i = []
loto = [new_list_a, new_list_b, new_list_c, new_list_d, new_list_e, new_list_f, new_list_g, new_list_h, new_list_i]
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_c = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list_d = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
list_e = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
list_f = [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
list_g = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
list_h = [71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
list_i = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
all_numbers = [list_a, list_b, list_c, list_d, list_e, list_f, list_g, list_h, list_i]
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
for el in all_numbers:
    for count in range(0,list_number_in_column[k]):
        our_number = random.choice(el)
        el.remove(our_number)
        loto[k].append(our_number)
        if len(loto[k]) < 6 and count == list_number_in_column[k]-1:
            while len(loto[k]) < 6:
                loto[k].append(0)
        if count == list_number_in_column[k]-1:
            random.shuffle(loto[k])
            k += 1
print(all_numbers)
print(loto)
k = 0
print("\n")
print("--LOTO--")
for i in range(0,6):
    for j in range(0,len(loto)):
        print("|",loto[j][i], end = "")
        if loto[j][i]>9:
            print(" |",end = "")
        else:
            print("  |", end="")
    if i == 2:
        print("\n\n")
    print("\n")