import easygui
food = 5
water = 5
variable = True
dict_image = {
    'dog': "img/dog.jpg",
    'start': "img/way.jpg"
}
easygui.msgbox("Правила: Следите за значениями еды и воды."
      "\nЗначения еды и воды не должны быть меньше 0 или превышать 5!"
      "\n\nВы красивый, сильный, молодой и юный ПЁС! Вы немного загуляли."
      "\nВам предстоит добраться от микрорайона Уручье до микрорайона Лошица,"
      "\nчтобы вернуться к своему хозяину! "
      "\n----------------"
      "\n|         =    |"
      "\n| |       ==== |"
      "\n| --=======    |"
      "\n|   |     |    |"
      "\n   FOOD: " + "*" * food + ""
      "\n  WATER: " + "*" * water + ""
      "\n----------------",image=dict_image['dog'])
step = easygui.buttonbox("Будете добираться через МКАД или через город?", image=dict_image['start'],
                         choices = ["Мкад", "Город", "Надо подумать"])
if step.lower() == "мкад":
    food -= 1
    water -= 1
    easygui.msgbox("----------------"
          "\n|         =    |"
          "\n| |       ==== |"
          "\n| --=======    |"
          "\n|   |     |    |"
          "\n   FOOD: " + "*" * food + ""
          "\n  WATER: " + "*" * water + ""
          "\n----------------"
          "\nЛегкой трусцой ты побежал по летнему зеленому уручью в сторону МКАДа.")
    while variable:
        stop = easygui.buttonbox("По пути ты увидел остановку. Тебе надо принять решение: "
                                 "\n1. Идти дальше пешком, 2. Проехать на автобусе. ",
                                 choices=["1", "2"])
        if stop == "1":
            food -= 1
            water -= 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы добрался до МКАДа и в это время пошел дождь")
            break
        elif stop == "2":
            food -= 1
            water -= 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы доехал на автобусе до МКАДа и в это время пошел дождь")
            break
    while variable:
        rain = easygui.buttonbox("Выбери вариант:"
                                 "\n1. Ты хочешь пойти под дождем, 2. Ты хочешь переждать дождь.",
                                 choices = ['1','2'])
        if (rain) == "1":
            food -= 1
            water += 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  '\nТы пошел под дождем. Шёл сильный ливень и по дороге ты утолил подкравшуюся жажду,'
                  '\nпопив дождевой воды из лужи.'
                  '\nТы сильно намок, через некоторое время выглянуло солнце, '
                  '\nпод которым ты решил погреться.')
            time_bask = 0
            while variable:
                while time_bask < 20:
                    time = easygui.choicebox("Укажите время которое ты будешь греться на солнце: "
                                                "\n1. 5 минут, 2. "+ str(20 - time_bask) +" минут, 3. 1 час.",
                                                choices = ['1', '2', '3'])
                    if (time == "1"):
                        time_bask += 5
                        if time_bask < 20:
                            easygui.msgbox(str(time_bask) + ' минут не хватило чтобы высохнуть.')
                        if time_bask == 20:
                            food -= 1
                            water -= 1
                            easygui.msgbox("----------------"
                                  "\n|         =    |"
                                  "\n| |       ==== |"
                                  "\n| --=======    |"
                                  "\n|   |     |    |"
                                  "\n   FOOD: " + "*" * food + ""
                                  "\n  WATER: " + "*" * water + ""
                                  "\n----------------"
                                  '\n20 минут хватило чтобы высохнуть.'
                                  '\nМожно идти дальше в путь.'
                                  '\nТы дошел по мкаду до чижовки и свернул в город, направившись'
                                  '\n в сторону лошицкого парка.')
                    elif (time == "2"):
                        food -= 1
                        water -= 1
                        easygui.msgbox("----------------"
                              "\n|         =    |"
                              "\n| |       ==== |"
                              "\n| --=======    |"
                              "\n|   |     |    |"
                              "\n   FOOD: " + "*" * food + ""
                              "\n  WATER: " + "*" * water + ""
                              "\n----------------"
                              '\n20 минут хватило чтобы высохнуть.'
                              '\nМожно идти дальше в путь.'
                              '\nТы дошел по мкаду до чижовки и свернул в город, направившись'
                              '\n в сторону лошицкого парка.')
                        break
                    elif (time == "3"):
                        food -= 1
                        water -= 1
                        easygui.msgbox("----------------"
                              "\n|         =    |"
                              "\n| |       ==== |"
                              "\n| --=======    |"
                              "\n|   |     |    |"
                              "\n   FOOD: " + "*" * food + ""
                              "\n  WATER: " + "*" * water + ""
                              "\n----------------"
                              '\nВы грелись слишком долго и заснули.'
                              '\nТебя забрала служба по отлову бездомных животных. Квест окончен за решеткой!'
                              '\nGAME OVER')
                        variable = False
                        break
                break
            break
        elif (rain) == "2":
            food -= 1
            water += 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  '\nШёл приличный ливень и пока ты пережидал его под козырьком остановки,'
                  '\nты утолил подкравшуюся жажду, попив дождевой воды из лужи.'
                  '\nТы переждал дождь.'
                  '\nМожно идти дальше в путь.'
                  '\nТы дошел по мкаду до чижовки и свернул в город, направившись'
                  '\nв сторону лошицкого парка.')
            break
elif step.lower() == "город":
    food -= 1
    water -= 1
    easygui.msgbox("----------------"
          "\n|         =    |"
          "\n| |       ==== |"
          "\n| --=======    |"
          "\n|   |     |    |"
          "\n   FOOD: " + "*" * food + ""
          "\n  WATER: " + "*" * water + ""
          "\n----------------"
          "\nОблегчившись на ногу, задумывшегося и говорящего по телефону "
          "\nслучайного прохожего около ТЦ Спектр,ты начал движение сквозь"
          "\nзнойный и жаркий центр города!")
    while variable:
        step = easygui.buttonbox("Пробежав приличное число км. и добежав до парка "
                                 "\nЧелюскинцев ты почувствовал голод и жажду!"
                                 "\nХочешь утолить жажду?",
                                 choices = ["Y", "N"])
        if step.lower() == "y":
            food -= 1
            water += 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы забежал в сам парк и попил из фантана!")
            break
        elif step.lower() == "n":
            food -= 1
            water -= 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТебя мучает жажда, но ты решил потерпеть!")
            break
    while variable:
        step = easygui.buttonbox("Пришло время пожрать! Ты видишь продовца хот-догов "
                                 "\nс передвижной тележкой.Хочешь проявить инициативу?",
                                 choices=["Y", "N"])
        if step.lower() == "y":
            food -= 1
            water -= 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы очень умный, хитрый и решительный ПЁС. "
                  "\nТы быстро подбегаешь к продавцу хот-догов "
                  "\nсзади, нежно кусаешь его за попку и происходит "
                  "\nто что тебе нужно..."
                  "\nПродавец вскрикивает, случайным движением руки "
                  "\nопракидывает тележку и на земле оказываются 10-ть "
                  "\nхот-догов. Видя это, ты понимаешь, что это твой шанс"
                  "\nутолить голод!")
            while variable:
                step1 = 0
                step = easygui.choicebox("Сколько ты хочешь съесть хотдогов? Будь аккуратным, "
                                         "\n1 хот-дог равен одной единице пищевого запаса!",
                                         choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
                if step == None:
                    easygui.msgbox("Не нажимайте 'Cancel'!")
                elif step != None:
                    step = int(step)
                    food = food + step * 1
                    step1 = step
                if food > 5 and 0 < step1 < 11:
                    easygui.msgbox("----------------"
                          "\n|         =    |"
                          "\n| |       ==== |"
                          "\n| --=======    |"
                          "\n|   |     |    |"
                          "\n   FOOD: " + "*" * food + ""
                          "\n  WATER: " + "*" * water + ""
                          "\n----------------"
                          "\nТы съел много хот-догов. Ты так обожрался, "
                          "\nчто не смог двигаться. Тебя нагнал разгневанный "
                          "\nпродавец и пустил тебя на хот-дог."
                          "\nGAME OVER")
                    variable = False
                elif food <= 5 and 0 < step1 < 11:
                    easygui.msgbox("----------------"
                          "\n|         =    |"
                          "\n| |       ==== |"
                          "\n| --=======    |"
                          "\n|   |     |    |"
                          "\n   FOOD: " + "*" * food + ""
                          "\n  WATER: " + "*" * water + ""
                          "\n----------------"
                          "\nСкушав несколько хот-догов(" + str(step) + "), "
                          "\nты почувствовал прилив сил и решил побежать дальше.")
                    break
            break
        elif step.lower() == "n":
            food -= 1
            water -= 1
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы очень умный, хитрый и решительный ПЁС. Но также ты очень хороший. "
                  "\nТы решил потерпеть и покушать позже. Отправляешься дальше в путь.")
            break
else:
    easygui.msgbox("Ты долго думал! Тебя забрала служба по отлову бездомных животных. Квест окончен за решеткой!"
          "\n----------------"
          "\n|         =    |"
          "\n| |       ==== |"
          "\n| --=======    |"
          "\n|   |     |    |"
          "\n   FOOD: " + "*" * food + ""
          "\n  WATER: " + "*" * water + ""
          "\n----------------"
          "\nGAME OVER")
    variable = False
while variable:
    step1 = -1
    step = easygui.choicebox("Вот ты уже вбегаешь в Лошицкий, пробежав приличное расстояние, ты почти у цели."
                                "\nТы видишь в траве лежит два кусочка курочки. Сколько кусочков курочки ты хочешь съесть?"
                                "\nБудь аккуратным, 1 кусочек курочки равен одной единице пищевого запаса!",
                                choices=["0", "1", "2"])
    if step == None:
        easygui.msgbox("Не нажимайте 'Cancel'!")
    elif step != None:
        step = int(step)
        food = food + step * 1
        step1 = step
    if food <= 5 and step1 == 1:
        water -= 1
        easygui.msgbox("Ты подкрепился и у тебя появились силы двигаться дальше."
                "\n----------------"
                "\n|         =    |"
                "\n| |       ==== |"
                "\n| --=======    |"
                "\n|   |     |    |"
                "\n   FOOD: " + "*" * food + ""
                "\n  WATER: " + "*" * water + ""
                "\n----------------")
        break
    elif food <= 5 and step1 == 2:
        water -= 1
        easygui.msgbox("Ты подкрепился и у тебя появились силы двигаться дальше."
                "\n----------------"
                "\n|         =    |"
                "\n| |       ==== |"
                "\n| --=======    |"
                "\n|   |     |    |"
                "\n   FOOD: " + "*" * food + ""
                "\n  WATER: " + "*" * water + ""
                "\n----------------")
        break
    elif food > 5 and (step1 == 2 or step1 == 1):
        water -= 1
        easygui.msgbox("Ты обожрался. Не можешь двигаться. Как раз в это время по парку"
                "\nпроходила служба отлова бездомных животных. Они тебя поймали."
                "\nКвест закончен за решёткой"
                "\n----------------"
                "\n|         =    |"
                "\n| |       ==== |"
                "\n| --=======    |"
                "\n|   |     |    |"
                "\n   FOOD: " + "*" * food + ""
                "\n  WATER: " + "*" * water + ""
                "\n----------------"
                "\nGAME OVER")
        variable = False
    elif food <= 5 and step1 == 0:
        food -= 1
        water -= 1
        if food == 0:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nТы был слишком голодным и сдох от голода. Надо было кушать!"
                    "\nGAME OVER!")
            variable = False
            break
        else:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nТы решил не есть кусок курочки и начал движение дальше.")
            break
while variable:
    step = easygui.buttonbox("Летняя дикая жара на улице заставляет тебя задуматься о принятии жидкости."
                             "\nХочешь попить?",
                             choices=["Y", "N"])
    if step.lower() == "y":
        food -= 1
        water += 1
        if water != 0 and food == 0:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nТы сдох от голода. Надо было кушать!"
                    "\nGAME OVER!")
            variable = False
            break
        elif water != 0 and food != 0:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nВоды много не бывает в такую жару. Освежившись, ты дальше бежишь по зелёному парку.")
        break
    elif step.lower() == "n":
        food -= 1
        water -= 1
        if water != 0 and food == 0:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nТы сдох от голода. Надо было кушать!"
                    "\nGAME OVER!")
            variable = False
            break
        elif water !=0 and food != 0:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nТы отказался от воды в такую жару."
                    "\nВсё же ты дальше бежишь по зелёному парку.")
            break
        elif water ==0 and food != 0:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nТы сдох от обезвоживания. Надо было пить!"
                    "\nGAME OVER!")
            variable = False
            break
        elif water == 0 and food == 0:
            easygui.msgbox("----------------"
                    "\n|         =    |"
                    "\n| |       ==== |"
                    "\n| --=======    |"
                    "\n|   |     |    |"
                    "\n   FOOD: " + "*" * food + ""
                    "\n  WATER: " + "*" * water + ""
                    "\n----------------"
                    "\nТы сдох от обезвоживания и голода. Надо было пить и кушать!"
                    "\nGAME OVER!")
            variable = False
            break
while variable:
    step = easygui.buttonbox("В парке ты видишь несколько резвящихся на поляне бродячих псов?"
                             "\nХочешь с ними познакомиться? 1. Да, 2. Нет",
                             choices=["1", "2"])
    if step.lower() == "1":
        food -= 1
        water -= 1
        if  water != 0 and food != 0:
            easygui.msgbox("Ты подбегаешь к бездомным псам, начинаешь с ними резвиться и понимаешь, что тебе с ними хорошо. "
                  "\nТы вступаешь в их ряды и становишься членом банды 'Шерстяные скотинки'."
                  "\nЭта жизнь тожа будет хороша."
                  "\n----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nFIN!")
        elif  water == 0 and food == 0:
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы сдох от обезвоживания и голода. Надо было пить и кушать!"
                  "\nGAME OVER!")
        elif water == 0 and food != 0:
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы сдох от обезвоживания. Надо было пить!"
                  "\nGAME OVER!")
        elif water != 0 and food == 0:
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы сдох от голода. Надо было кушать!"
                  "\nGAME OVER!")
        break
    elif step.lower() == "2":
        food -= 1
        water -= 1
        if water != 0 and food != 0:
            easygui.msgbox("Ты решаешь искать дальше своего хозяина. Ты пересекаешь весь парк и забегаешь "
                  "\nв сам микрорайон Лошица. Добираешься до двери своей квартиры и начинаешь громко лаять. "
                  "\nДверь открывается и тебя встречает радостный хозяин. Ты дома. Ура."
                  "\n----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nFIN!")
        elif water == 0 and food == 0:
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы сдох от обезвоживания и голода. Надо было пить и кушать!"
                  "\nGAME OVER!")
        elif water == 0 and food != 0:
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "Ты сдох от обезвоживания. Надо было пить!"
                  "\nGAME OVER!")
        elif water != 0 and food == 0:
            easygui.msgbox("----------------"
                  "\n|         =    |"
                  "\n| |       ==== |"
                  "\n| --=======    |"
                  "\n|   |     |    |"
                  "\n   FOOD: " + "*" * food + ""
                  "\n  WATER: " + "*" * water + ""
                  "\n----------------"
                  "\nТы сдох от голода. Надо было кушать!"
                  "\nGAME OVER!")
        break