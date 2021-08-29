"""

Имеется набор файлов, каждый из которых, кроме последнего, 
содержит имя следующего файла.

Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

"""

import requests
with open(r"C:\Users\belou\Desktop\Python\Stepic\We are the champions\dataset.txt") as data:
    r = requests.get(data.readline().strip())
    while True:
        if not r.text.startswith('We'):
            r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/' + r.text)
            print(r.text)
            continue
        else:
            break




