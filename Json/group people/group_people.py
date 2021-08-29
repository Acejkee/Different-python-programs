"""
В json-файле содержится информация о нескольких групп людей, 
при этом у каждой группы есть свой идентификатор. 

Ваша задача скачать файлик и самостоятельно найти идентификатор группы, 
в которой находится самое большое количество женщин, 
рожденных после 1977 года. 
В качестве ответа необходимо указать через пробел идентификатор найденной группы и 
сколько в ней было женщин, рожденных после 1977 года.

"""

import json
max_count = 0
id_group = 0  # переменные
with open(r'C:\Users\belou\Desktop\Python\json\group people\group_people.json') as file:
    data = json.load(file)
    id_group = 0
    max_count = 0
    for element in data:
        count = 0
        for person in element["people"]:
            if person["gender"] == "Female" and person["year"] > 1977:
                count += 1
        if count > max_count:
            id_group = element["id_group"]
            max_count = count
    print(id_group,max_count)