import os  # Импортируем библиотеки для работы
import time as t 
import random 
import datetime


def clear():  # Чистка консоли  
    os.system('cls')


fl = 0


def lovlya():  
    dt1, fail = 0, 0
    print("Сундук находится на другом берегу пещерной речки, к этому берегу никак не подобраться, \
если прыгнешь в речку - то живым уже не выберешься (слишком сильное течение, да оно еще и в ущелье). \
Выбора нет - приходится дернуть на себя рукой веревку, чтобы клад упал в речку. Ваша же цель - не упустить веревку и \
вытащить клад из западни. Чтобы этого добиться, как можно чаще нажимайте клавишу Enter.")
    input()
    for i in range(100):
        if dt1 == 0:
            dt1 = datetime.datetime.now()
        input()
        dt2 = datetime.datetime.now()
        if (dt2 - dt1).total_seconds() > 0.18:
            fail += 1
            print("Поднажми!")
            if fail == 31:
                print("Все. Вы выпустили из рук веревку, сундук попал в подземную реку, его подхватило течением \
и он бесследно исчез.")
                t.sleep(5)
                input()
                quit()
            elif fail == 11:
                print("Крышка сундука внезапно открылась... Сундук накренился и антикварная ваза в сундуке разбилась \
ВЗДРЕБЕЗГИ (а она дороже любого количества монет).")
            elif fail > 19 and fail < 31:
                print("И монеты начали падать...")
                if fail == 25:
                    print("Вот уже и половина монет в пучине.")
                if fail >= 25:
                    print("Налегай, спаси хоть что-то!")
        dt1 = dt2
    if fail > 19:
        print("Все-таки не зря фермер пошел в поход: он нашел " + str(90000 * (31 - fail)) + " монет.")
        t.sleep(10)
        quit()
    elif fail <= 19 and fail > 10:
        print("Ваза разбилась, конечно, но фермер нашел целый МИЛЛИОН монет!")
        t.sleep(10)
        quit()
    elif fail <= 10:
        print("Теперь наш герой сможет каждый день любоваться на вазу, богато украшенную хрусталем и золотом, \
и жить припеваючи на найденный в кладе миллион монет.")
        t.sleep(10)
        quit()
        
        
def loter_bil():
    global fl, r, ind
    for j in range(inventary[4]):
        inventary[4] = 0
        r, ind = int(random.choices([0, 1], weights=[90, 10])[0]), -1
        if r == 1:
            ind = random.randint(0, 19)
        for i in range(20):
            print("Билет " + str(i + 1) + ", стопка " + str(j + 1) + "... ", end="")
            if i != ind:
                print("Ничего.")
            else:
                print("Найдено!")
                fl = 1
                t.sleep(2)
                break
        if fl == 1:
            break
    if fl == 0:
        t.sleep(3)
        
        
def store():
    global coins
    sale_flag, sale_string, s, es, choice = 0, "", 0, 0, ""
    while choice != "Хватит":
        clear()
        print("Денег: " + str(coins), end="\n\n")
        for i in range(len(products)):
            if sale_flag == 0 and available[i] > 0:
                s = float(random.choices([0, 0.1, 0.2, 0.3, 0.4, 0.5], weights=[90, 3, 3, 2, 1, 1])[0])
                if s == 0.0:
                    sale_string = ""
                else:
                    sale_string = " (скидка " + str(int(s * 100.0)) + "%)"
                    sale_flag = 1
            if i == 0:
                print(
                    "Товар" + " " * (len(max(products, key=len)) - len("Товар") + 20) + 
                    "Стоимость" + " " * 15 + "Осталось", end="\n\n")
            print(
                products[i] + " " * (len(max(products, key=len)) - len(products[i]) + 20) + 
                str(int(cost[i] * (1.0 - s))) + sale_string + " " * 
                (len(str(max(cost))) - len(str(int(cost[i] * (1.0 - s)))) + 20 - len(sale_string)) + str(available[i]) + 
                " " * (len(str(max(available))) - len(str(available[i])) + 5) + 
                "(очень мало в наличии!)" * (available[i] <= 10 and available[i] > 0) + 
                "(нет в наличии!)" * (available[i] == 0))
            sale_string = ""
            if s != 0:
                es = s
            s = 0
        print()
        print("Вводите в формате - количество позиций товара (неотрицательное число) - пробел - \
наименование товара или же слово 'Хватит'.")
        choice = input()
        if choice == "Хватит":
            break
        try:
            quant, good = int(choice.split()[0]), choice.split()[1]
            if quant >= 0:
                for i in range(len(products)):
                    if products[i].lower() == good.lower():
                        if quant > available[i]:
                            if coins >= available[i] * (int(cost[i] * (1.0 - es))):
                                coins -= available[i] * (int(cost[i] * (1.0 - es)))
                                print("Извините, у нас только " + str(available[i]) + " позиций данного \
                                товара, их вам и продаем.")
                                t.sleep(1.5)
                                inventary[i] = available[i]
                                available[i] = 0
                            else:
                                print("Недостаточно денег.")
                                t.sleep(1.5)
                        else:
                            if coins >= quant * (int(cost[i] * (1.0 - es))):
                                coins -= quant * (int(cost[i] * (1.0 - es)))
                                available[i] -= quant
                                inventary[i] += quant
                            else:
                                print("Недостаточно денег.")
                                t.sleep(1.5)
                        es = 0
            else:
                print("Где вы видели отрицательное количество товара?")
                t.sleep(2)
        except ValueError:
            print("Введите в вышеуказанном формате.")
            t.sleep(2)
    clear()
    
    
products = ["Яблоко", "Фонарик", "Пещ.ботинки", "Лассо", "Лотер.Билет"]
available = [10, 15, 9, 20, 10]
cost, coins, inventary = [50, 400, 5000, 1000, 200], 20000, [0, 0, 0, 0, 0]
print("Чтобы выйти из магазина, пишите Хватит (писать это слово так же, как здесь).")
print("Итак, наш герой летним вечером прогуливается по побережью. Он гуляет здесь почти \
каждый день (и зимой тоже), но только сейчас он обратил внимание на одиноко стоящую \
сосну и особенно на большое дупло в ней. Подойдя к дереву ближе, он заметил чуть выглядывающее \
из отверстия горлышко бутылки. Оно наглухо залито сургучом, а цвет \
стекла бутылки такой темный, что можно было только потрясти, чтобы хоть примерно определить \
ее содержимое (что наш герой и сделал). Конечно, если она была бы пуста, \
наш герой свернул бы на лесную тропку и пошёл бы дальше неспешно прогуливаться. \
Но нет, в бутыли что-то было, то ли бумажка, то ли нечто похожее на бумажку. Так \
бутылка еще оказалась сделанной из небьющегося стекла, разбить ее, бросив оземь, \
не получится. Конечно, желание гулять у нашего героя пропало, схватив бутылку \
(и чуть не выронив ее в дельту реки), он побежал к своему маленькому домику.")
input()
clear()
print("Сургуч легко растопился над свечой, и, очистив палочкой горлышко бутылки от еще горячей смеси, \
достать послание было проще пареной репы (эта поговорка отлично применима к нашему герою, \
который по профессии фермер). Но в послании - нечто зашифрованное цифрами:")
input()
clear()
print("16 3-6-13-10-12-10-11 17-16-12-16-18-10-20-6-13-30 19-16-19-15-16-3-29-23 \
5-21-17-6-13! 5-10-3-21 5-1-6-14-19-33, 25-20-16 20-29 15-1-26-6-13 31-20-21 \
2-21-20-29-13-30, 15-16 18-1-9 15-1-26-6-13, \
2-21-5-6-26-30 17-6-18-3-29-14 (17-16-25-20-10 17-6-18-3-29-14) 19-20-18-1-15-15-10-12-16-14, \
3-16-26-6-5-26-10-14 3 17-6-27-6-18-21 englestead cavern. 12-16-4-5-1-20-16 12-21-17-24-29 9-5-6-26-15-10-6, \
19-17-1-19-1-33-19-30 16-20 14-1-18-16-5-6-18-16-3, 17-6-18-6-2-18-16-19-10-13-10 25-6-18-6-9 \
26-21-14-15-29-11 12-1-15-30-16-15 31-20-16-11 17-6-27-6-18-29 19-21-15-5-21-12 19 20-1-12-10-14-10 \
19-16-12-18-16-3-10-27-1-14-10, \
25-20-16 20-6-2-6, 16 3-6-13-10-12-10-11 17-16-12-16-18-10-20-6-13-30 5-21-17-6-13, \
10 15-6 19-15-10-13-16-19-30. 5-1 3-16-20, 12-1-12 16-17-1-19-15-16-19-20-30 14-10-15-16-3-1-13-1, \
3-29-20-1-27-10-20-30 16-2-18-1-20-15-16 \
16-15-10 6-4-16 15-6 19-14-16-4-13-10 (13-1-19-19-16 21 15-10-23 15-6 2-29-13-16, 25-20-16 13-10?). \
3-16-20 20-6-2-6 17-6-18-3-1-33 17-16-5-19-12-1-9-16-25-12-1... 13-1-5-15-16, \
17-18-16-2-16-13-20-1-13-19-33 33, 20-3-16-33 \
3-6-5-30 9-1-2-16-20-1 12 17-16-23-16-5-21 4-16-20-16-3-10-20-30-19-33")
input()
clear()
print("'Нет, конечно, можно и самому эту головоломку разгадывать, но зачем, вдруг есть подсказки?' \
- подумал фермер.\n1. В магазин (там тоже надо подумать над выбором). \n2. Подумать своей головой")
a = input()
while a != "1" and a != "2":
    print("Введите корректный ответ на вопрос.")
    a = input() 
clear()
if a == "1":
    print("Совет: используйте, то что нужно купить (подумайте сами, что), поштучно или в крайнем \
случае по две штуки.")
    input()
    while fl == 0:
        while inventary[4] == 0:
            store()
            if inventary[4] == 0:
                print("Еще раз.")
                t.sleep(2)
            else:
                loter_bil()
                if fl == 1:
                    clear()
                    print("https://planetcalc.ru/4884... Только... Тсс!")
                    input()
                    clear()
                    break
if a == "2" or a == "1":
    print("16 3-6-13-10-12-10-11 17-16-12-16-18-10-20-6-13-30 19-16-19-15-16-3-29-23 \
5-21-17-6-13! 5-10-3-21 5-1-6-14-19-33, \
25-20-16 20-29 15-1-26-6-13 31-20-21 2-21-20-29-13-30, \
15-16 18-1-9 15-1-26-6-13, 2-21-5-6-26-30 17-6-18-3-29-14 \
(17-16-25-20-10 17-6-18-3-29-14) 19-20-18-1-15-15-10-12-16-14, \
3-16-26-6-5-26-10-14 3 17-6-27-6-18-21 englestead cavern. \
12-16-4-5-1-20-16 12-21-17-24-29 9-5-6-26-15-10-6, \
19-17-1-19-1-33-19-30 16-20 14-1-18-16-5-6-18-16-3, \
17-6-18-6-2-18-16-19-10-13-10 25-6-18-6-9 26-21-14-15-29-11 \
12-1-15-30-16-15 31-20-16-11 17-6-27-6-18-29 19-21-15-5-21-12 \
19 20-1-12-10-14-10 19-16-12-18-16-3-10-27-1-14-10, \
25-20-16 20-6-2-6, 16 3-6-13-10-12-10-11 \
17-16-12-16-18-10-20-6-13-30 5-21-17-6-13, \
10 15-6 19-15-10-13-16-19-30. 5-1 3-16-20, 12-1-12 \
16-17-1-19-15-16-19-20-30 14-10-15-16-3-1-13-1, 3-29-20-1-27-10-20-30 \
16-2-18-1-20-15-16 16-15-10 6-4-16 15-6 \
19-14-16-4-13-10 (13-1-19-19-16 21 15-10-23 \
15-6 2-29-13-16, 25-20-16 13-10?). \
3-16-20 20-6-2-6 17-6-18-3-1-33 \
17-16-5-19-12-1-9-16-25-12-1... 13-1-5-15-16, \
17-18-16-2-16-13-20-1-13-19-33 33, 20-3-16-33 \
3-6-5-30 9-1-2-16-20-1 12 17-16-23-16-5-21 4-16-20-16-3-10-20-30-19-33")
    b = input("Введите правильную транскрипцию.\n")
    while b.lower() != "о великий покоритель сосновых дупел! \
диву даемся, что ты нашел эту бутыль, \
но раз нашел, будешь первым (почти первым) странником, вошедшим в пещеру englestead cavern. когдато купцы здешние, \
спасаясь от мародеров, перебросили через шумный каньон этой пещеры сундук с такими сокровищами, что тебе, \
о великий покоритель дупел, и не снилось. да вот, как опасность миновала, вытащить обратно они его не смогли \
(лассо у них не было, что ли?). вот тебе подсказочка... ладно, проболтался я, твоя ведь забота к походу \
готовиться".lower():
        print("Нет.")
        b = input()
clear()
if a == "2":
    print("А вы молодец, разгадали!")
    t.sleep(2)
input()
clear()
print("Но вдруг он вспомнил внезапно, что ему завтра работать на своем огороде. \
Соблазн как можно быстрее найти клад был велик, он долго думал, что же предпринять, но так и не выбрал. Помогите же ему.\
\n1. Пропустить работу (за свой счет, разумеется). \n2. Выйти завтра на работу")
a = input()
clear()
while a != "1" and a != "2":
    print("Введите корректный ответ на вопрос.")
    a = input()
if a == "1":
    for i in range(coins, coins - 2001, -200):
        print(i)
        coins -= 200
        t.sleep(0.2)
        clear()
elif a == "2":
    print("Прошел день...", end=" ")
    t.sleep(1)
    print("Два дня...", end=" ")
    t.sleep(0.5)
    print("Неделя...", end=" ")
    t.sleep(0.25)
    print("И копал наш фермер грядку, и тут тыква какого-то необычного сорта формой напомнила ему \
ту самую темную бутылку. \
Он вспомнил про свои планы недельной давности, и твердо решил: завтра и пойду на поиски.")
    input()
    clear()
print("Специальных ботинок для ходьбы по пещерам у фермера не было. Может, они есть у моего соседа-кожевника?")
input()
clear()
print("'Привет, старина. Не найдется ли у тебя случайно кожаных прочных ботинок?'")
input()
clear()
print("'Пока выгоднее продавать кожаные сумки, на них спрос больший, поэтому пока я такие ботинки не делаю. \
Но можешь прийти через неделю: вдруг сделаю.'")
input()
clear()
print("Ясно-понятно, значит, куплю ботинки и все к походу в магазине.")
input()
clear()
while inventary[1] == 0 or inventary[2] == 0 or inventary[3] == 0:
    store()
    if inventary[1] == 0 or inventary[2] == 0 or inventary[3] == 0:
        print("Видимо, чего-то не хватает.")
        t.sleep(3)
print("Итак, вещи собраны, можно выезжать по координатам, которые, как потом оказалось, были напечатаны на другой \
стороне послания. Доехать до пещеры можно только на электричке, при этом пещера находится в 30 км от железнодорожного \
полотна. ")
input()
clear()
print("Вход в пещеру был отлично виден даже в полукилометре. 'И почему никто не знает эту пещеру? - подумал фермер. \
Зайдя внутрь пещеры, он услышал шум воды и пошел к нему. И - да! - вот сундук. Мастерски обладая навыками \
забрасывания лассо, \
фермер подцепил сундук за массивную металлическую ручку.")
lovlya()
