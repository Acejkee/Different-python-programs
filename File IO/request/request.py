"""
Скачайте файл. В нём указан адрес другого файла, 
который нужно скачать с использованием модуля requests 
и посчитать число строк в нём.

"""

import requests
with open(r"C:\Users\belou\Desktop\Python\Stepic\request\dataset.txt") as data:
    r = requests.get(data.readline().strip())
    print(len(r.text.splitlines()))
