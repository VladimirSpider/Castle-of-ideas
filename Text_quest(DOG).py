print("Вы красивый, сильный, молодой и юный Хаски! "
      "\nВам предстоит добраться от микрорайона Уручье до микрорайона Серебрянка!")
print("----------------"
      "\n|         =    |"
      "\n| |       ==== |"
      "\n| --=======    |"
      "\n|   |     |    |"
      "\n|  FOOD: ***** |"
      "\n| WATER: ***** |"
      "\n----------------")
print("Будете добираться через МКАД или через город?")
step = input("Буду добираться через: ")
if step.lower() == "мкад":
    print("Легкой трусцой ты побежал по летнему зеленому уручью в сторону МКАДа")
elif step.lower() == "город":
    print("Облегчившись на ногу, задумывшегося и говорящего по телефону случайного прохожего около ТЦ Спектр,"
          "\nты начал движение сквозь знойный и жаркий центр города!"
          "\nПробежав приличное число км. и добежав до парка Челюскинцев ты почувствовал голод и жажду!"
          "\nХочешь утолить жажду? Y / N")
    step = input("Утолить жажду? ")
    thirst = 0
    if step.lower() == "y":
        print("Ты забежал в сам парк и попил из фантана!"
              "\nПришло время пожрать!")
    else:
        thirst = thirst + 1
        print("Тебя мучает жажда, но ты решил потерпеть!"
              "\nНо пожрать ты хочешь!")

else:
    print("Ты долго думал! Тебя забрала служба по отлову бездомных животных. Квест окончен за решеткой!")
