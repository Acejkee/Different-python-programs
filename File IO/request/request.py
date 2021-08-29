"""
Скачайте файл. В нём указан адрес другого файла, 
который нужно скачать с использованием модуля requests 
и посчитать число строк в нём.

"""

import requests
with open(***path to file***) as data:
    r = requests.get(data.readline().strip())
    print(len(r.text.splitlines()))
