"""
Напишите программу, которая считывает текст из файла 
(в файле может быть больше одной строки) 
и выводит самое частое слово в этом тексте и через пробел то, 
сколько раз оно встретилось. Если таких слов несколько, 
вывести лексикографически первое 
(можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

"""

with open(***path to file***) as data:
    data = data.read().lower().split()
    word = ""
    max_count = 0
    for i in data:
        if data.count(i) > max_count:
            max_count = data.count(i)
            word = i
    print(word , max_count)
        

    #with open(r'C:\Users\belou\Desktop\Python\Stepic\search_max\dataset.txt') as data:
        #text = data.read().lower().split()
        #popular_word = max(set(text), key=text.count)
        #print(popular_word, text.count(popular_word))
