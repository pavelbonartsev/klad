import time as t, os
x, f, y, coins, s, ind  = 0, 1, 1, 100000, "", 0
weight = [2, 1.3]
current = [55, 32]
name = ["Лопата", "Металлоискатель"]
coin = [1000, 5000]
replics = {"1": ["Привет! Как дела?", "Бывает", "Ура!", "f:Наш робот определил, что у вас хорошее настроение."],
           "2": ["", "Я рад!", "Жаль.", "f:Наш робот определил, что у вас плохое настроение."]}
questions = {"1": ["Плохо.", "Точно плохое?", "А вдруг хорошее?"], #Вопросы либо же функции.
             "2": ["Хорошо.", "Точно хорошее?", "А вдруг плохое?"]}
indexes = {"1": [[1, 1], [1, 2], [1, 0]],           #Никто не говорил, что мы будем продвигаться по сюжету последовательно. Здесь данные, которые в зависимости от выбранного вопроса перенеправляют либо далее по сюжету, либо возвращают назад по сюжету либо оставляют на текущем месте.
           "2": [[2, 1], [2, 2], [2, 3]]}

def word_prof_righting(inp):
    numb = int(inp.split()[0])
    word = inp.split()[1]
    for i in name:
        if word.lower() == i.lower():
            ind = i
            break
    if ind != 0:
        coin -= numb * coin[ind]
        current[ind] -= numb
    ind = 0

def store():
    print("Денег", coins)
    for i in range(len(name)):
        print(name[i] + ", вес " + str(weight[i]) + " кг, цена " + str(coin[i]) + " рублей, на данный момент доступно " + str(current[i]) + ".")
    word_prof_righting(input())

store()
while f == 1:
    if replics[str(y)][x][0:2] == "f:":
        if f != 0:
            print(replics[str(y)][x][2:])
            print("ПОЗДРАВЛЯЕМ! ВЫ ПРОШЛИ КВЕСТ.")
            f = 0
    else:
        print(replics[str(y)][x])
    if f == 1:
        for i in range(1, len(questions) + 1):
            if questions[str(i)][x] == "":
                break
            print(str(i) + ". " + questions[str(i)][x])
        s = input()
        old_x = x
        x = indexes[s][x][1]
        y = indexes[s][old_x][0]

        
    
    
