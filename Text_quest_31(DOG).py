food = 5
water = 5
variable = True

def picture():
    print("----------------"
          "\n|         =    |"
          "\n| |       ==== |"
          "\n| --=======    |"
          "\n|   |     |    |"
          "\n   FOOD: " + "*" * food + ""
          "\n  WATER: " + "*" * water + ""
          "\n----------------")

def yes_or_no(text):
    step = input(text)
    if step.lower() != "y" and step.lower() != "n":
        print('Вы должны ввести "y" или "n"')
    return step

def one_or_two(text):
    step = input(text)
    if step != "1" and step != "2":
        print('Вы должны ввести "1" или "2"')
    return step

def end(step):
    def outer(func):
        def wrapper():
            if water != 0 and food != 0 and step == '1':
                print("Ты подбегаешь к бездомным псам, начинаешь с ними резвиться и понимаешь, что тебе с ними хорошо. "
                    "\nТы вступаешь в их ряды и становишься членом банды 'Шерстяные скотинки'."
                    "\nЭта жизнь тожа будет хороша.")
                func()
                print("FIN!")
            elif water != 0 and food != 0 and step == '2':
                print("Ты решаешь искать дальше своего хозяина. Ты пересекаешь весь парк и забегаешь "
                      "\nв сам микрорайон Лошица. Добираешься до двери своей квартиры и начинаешь громко лаять. "
                      "\nДверь открывается и тебя встречает радостный хозяин. Ты дома. Ура.")
                func()
                print("FIN!")
            elif water == 0 and food == 0:
                func()
                print("Ты сдох от обезвоживания и голода. Надо было пить и кушать!"
                      "\nGAME OVER!")
            elif water == 0 and food != 0:
                func()
                print("Ты сдох от обезвоживания. Надо было пить!"
                      "\nGAME OVER!")
            elif water != 0 and food == 0:
                func()
                print("Ты сдох от голода. Надо было кушать!"
                      "\nGAME OVER!")
        return wrapper
    return outer

print("Правила: Следите за значениями еды и воды."
      "\nЗначения еды и воды не должны быть меньше 0 или превышать 5!"
      "\n\nВы красивый, сильный, молодой и юный ПЁС! Вы немного загуляли."
      "\nВам предстоит добраться от микрорайона Уручье до микрорайона Лошица,"
      "\nчтобы вернуться к своему хозяину! ")
picture()
print("Будете добираться через МКАД или через город?")
step = input("Буду добираться через: ")
if step.lower() == "мкад":
    food -= 1
    water -= 1
    picture()
    print("Легкой трусцой ты побежал по летнему зеленому уручью в сторону МКАДа.")
    print("По пути ты увидел остановку. Тебе надо принять решение: 1. Идти дальше пешком, 2. Проехать на автобусе. "
          "\nВведите 1 / 2")
    while variable:
        step = one_or_two("Ваш вариант: ")
        if step == "1":
            food -= 1
            water -= 1
            picture()
            print("Ты добрался до МКАДа и в это время пошел дождь")
            break
        elif step == "2":
            food -= 1
            water -= 1
            picture()
            print("Ты доехал на автобусе до МКАДа и в это время пошел дождь")
            break
    print("Выбери вариант: 1. Ты хочешь пойти под дождем, 2. Ты хочешь переждать дождь.")
    while variable:
        step = one_or_two("Ваш вариант: ")
        if step == "1":
            food -= 1
            water += 1
            picture()
            print('Ты пошел под дождем. Шёл сильный ливень и по дороге ты утолил подкравшуюся жажду,'
                  '\nпопив дождевой воды из лужи.'
                  '\nТы сильно намок, через некоторое время выглянуло солнце, '
                  '\nпод которым ты решил погреться.')
            print('Укажите время которое ты будешь греться на солнце: 1. 5 минут, 2. 20 минут, 3. 1 час.')
            time_bask = 0
            while variable:
                while time_bask < 20:
                    if time_bask != 0:
                        print('Укажите время которое ты будешь греться на солнце: 1. 5 минут, 2. '+ str(20 - time_bask) +' минут, 3. 1 час.')
                    time = input("Введи время: ")
                    if time != "1" and time != "2" and time != "3":
                        print('Вы должны ввести "1" или "2" или "3"')
                    if (time == "1"):
                        time_bask += 5
                        if time_bask < 20:
                            print(str(time_bask) + ' минут не хватило чтобы высохнуть.')
                        if time_bask == 20:
                            food -= 1
                            water -= 1
                            picture()
                            print('20 минут хватило чтобы высохнуть.'
                                  '\nМожно идти дальше в путь.'
                                  '\nТы дошел по мкаду до чижовки и свернул в город, направившись'
                                  '\n в сторону лошицкого парка.')
                    elif (time == "2"):
                        food -= 1
                        water -= 1
                        picture()
                        print('20 минут хватило чтобы высохнуть.'
                              '\nМожно идти дальше в путь.'
                              '\nТы дошел по мкаду до чижовки и свернул в город, направившись'
                              '\n в сторону лошицкого парка.')
                        break
                    elif (time == "3"):
                        food -= 1
                        water -= 1
                        print('1 час')
                        picture()
                        print('Вы грелись слишком долго и заснули.'
                              '\nТебя забрала служба по отлову бездомных животных. Квест окончен за решеткой!'
                              '\nGAME OVER')
                        variable = False
                        break
                break
            break
        elif step == "2":
            food -= 1
            water += 1
            picture()
            print('Шёл приличный ливень и пока ты пережидал его под козырьком остановки,'
                  '\nты утолил подкравшуюся жажду, попив дождевой воды из лужи.'
                  '\nТы переждал дождь.'
                  '\nМожно идти дальше в путь.'
                  '\nТы дошел по мкаду до чижовки и свернул в город, направившись'
                  '\nв сторону лошицкого парка.')
            break
elif step.lower() == "город":
    food -= 1
    water -= 1
    picture()
    print("Облегчившись на ногу, задумывшегося и говорящего по телефону "
          "\nслучайного прохожего около ТЦ Спектр,ты начал движение сквозь"
          "\nзнойный и жаркий центр города! Пробежав приличное число км. и "
          "\nдобежав до парка Челюскинцев ты почувствовал голод и жажду!"
          "\nХочешь утолить жажду? Y / N")
    while variable:
        step = yes_or_no("Утолить жажду? ")
        if step.lower() == "y":
            food -= 1
            water += 1
            picture()
            print("Ты забежал в сам парк и попил из фантана!")
            break
        elif step.lower() == "n":
            food -= 1
            water -= 1
            picture()
            print("Тебя мучает жажда, но ты решил потерпеть!")
            break
    print("Пришло время пожрать! Ты видишь продовца хот-догов "
          "\nс передвижной тележкой.Хочешь проявить инициативу?  Y / N")
    while variable:
        step = yes_or_no("Проявить инициативу?")
        if step.lower() == "y":
            food -= 1
            water -= 1
            picture()
            print("Ты очень умный, хитрый и решительный ПЁС. "
                  "\nТы быстро подбегаешь к продавцу хот-догов "
                  "\nсзади, нежно кусаешь его за попку и происходит "
                  "\nто что тебе нужно..."
                  "\nПродавец вскрикивает, случайным движением руки "
                  "\nопракидывает тележку и на земле оказываются 10-ть "
                  "\nхот-догов. Видя это, ты понимаешь, что это твой шанс "
                  "\nутолить голод. Сколько ты хочешь съесть хотдогов (введи число от 1 до 10)."
                  "\nБудьте аккуратным, 1 хот-дог равен одной единице пищевого запаса!")
            while variable:
                step1 = 0
                step = input("Число съеденных хот-догов: ")
                if step == "1" or step == "2" or step == "3" or step == "4" or step == "5" or step == "6" or step == "7" or step == "8" or step == "9" or step == "10":
                    step = int(step)
                    food = food + step
                    step1 = step
                else:
                    print('Вы должны ввести число от 1 до 10')
                if food > 5 and 0 < step1 < 11:
                    picture()
                    print("Ты съел много хот-догов. Ты так обожрался, "
                          "\nчто не смог двигаться. Тебя нагнал разгневанный "
                          "\nпродавец и пустил тебя на хот-дог."
                          "\nGAME OVER")
                    variable = False
                elif food <= 5 and 0 < step1 < 11:
                    picture()
                    print("Скушав несколько хот-догов(" + str(step) + "), "
                          "\nты почувствовал прилив сил и решил побежать дальше.")
                    break
            break
        elif step.lower() == "n":
            food -= 1
            water -= 1
            picture()
            print("Ты очень умный, хитрый и решительный ПЁС. Но также ты очень хороший. "
                  "\nТы решил потерпеть и покушать позже. Отправляешься дальше в путь.")
            break
else:
    print("Ты долго думал! Тебя забрала служба по отлову бездомных животных. Квест окончен за решеткой!")
    food -= 1
    water -= 1
    picture()
    print("GAME OVER")
    variable = False
while variable:
    print("Вот ты уже вбегаешь в Лошицкий, пробежав приличное расстояние, ты почти у цели.")
    print("Ты видишь в траве лежит два кусочка курочки. Сколько кусочков курочки ты хочешь съесть?"
          "\n(введи число 0, 1 или 2)."
          "\nБудьте аккуратным, 1 кусочек курочки равен одной единице пищевого запаса!")
    while variable:
        step1 = -1
        step = input("Сколько ты хочешь съесть кусочков курочки?")
        if step == "0" or step == "1" or step == "2":
            step = int(step)
            food = food + step
            step1 = step
        else:
            print('Вы должны ввести число число 0, 1 или 2')
        if food <= 5 and step1 == 1:
            water -= 1
            print("Ты подкрепился и у тебя появились силы двигаться дальше.")
            picture()
            break
        elif food <= 5 and step1 == 2:
            water -= 1
            print("Ты подкрепился и у тебя появились силы двигаться дальше.")
            picture()
            break
        elif food > 5 and (step1 == 2 or step1 == 1):
            water -= 1
            print("Ты обожрался. Не можешь двигаться. Как раз в это время по парку"
                  "\nпроходила служба отлова бездомных животных. Они тебя поймали."
                  "\nКвест закончен за решёткой")
            picture()
            print("GAME OVER")
            variable = False
        elif food <= 5 and step1 == 0:
            food -= 1
            water -= 1
            if  food == 0:
                picture()
                print("Ты был слишком голодным и сдох от голода. Надо было кушать!"
                      "\nGAME OVER!")
                variable = False
                break
            else:
                picture()
                print("Ты решил не есть кусок курочки и начал движение дальше.")
                break
    break
while variable:
    print("Летняя дикая жара на улице заставляет тебя задуматься о принятии жидкости."
          "\nХочешь попить? Y / N")
    while variable:
        step = yes_or_no("Хочешь попить?")
        if step.lower() == "y":
            food -= 1
            water += 1
            if water != 0 and food == 0:
                picture()
                print("Ты сдох от голода. Надо было кушать!"
                      "\nGAME OVER!")
                variable = False
                break
            elif water != 0 and food != 0:
                picture()
                print("Воды много не бывает в такую жару. Освежившись, ты дальше бежишь по зелёному парку.")
            break
        elif step.lower() == "n":
            food -= 1
            water -= 1
            if water != 0 and food == 0:
                picture()
                print("Ты сдох от голода. Надо было кушать!"
                      "\nGAME OVER!")
                variable = False
                break
            elif  water !=0 and food != 0:
                picture()
                print("Ты отказался от воды в такую жару."
                      "\nВсё же ты дальше бежишь по зелёному парку.")
                break
            elif water ==0 and food != 0:
                picture()
                print("Ты сдох от обезвоживания. Надо было пить!"
                      "\nGAME OVER!")
                variable = False
                break
            elif water == 0 and food == 0:
                picture()
                print("Ты сдох от обезвоживания и голода. Надо было пить и кушать!"
                      "\nGAME OVER!")
                variable = False
                break
    break
while variable:
    print("В парке ты видишь несколько резвящихся на поляне бродячих псов?"
          "\nХочешь с ними познакомиться? 1. Да, 2. Нет")
    break
while variable:
    step = one_or_two("Познакомиться? ")

    @end(step)
    def picture_end():
        print("----------------"
              "\n|         =    |"
              "\n| |       ==== |"
              "\n| --=======    |"
              "\n|   |     |    |"
              "\n   FOOD: " + "*" * food + ""
              "\n  WATER: " + "*" * water + ""
              "\n----------------")

    if step == "1":
        food -= 1
        water -= 1
        picture_end()
        break
    elif step == "2":
        food -= 1
        water -= 1
        picture_end()
        break