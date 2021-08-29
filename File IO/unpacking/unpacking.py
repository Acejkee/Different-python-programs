"""
Напишите программу, которая считывает из файла строку, 
соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.
"""

with open(r'C:\Users\belou\Desktop\Python\Stepic\unpacking\dataset.txt') as data:
    for i in data:
        for j in range(len(i)):
            if i[j].isalpha():
                if i[j+1].isdigit() and i[j+2].isdigit():
                    print(i[j] * int(i[j+1]) + i[j+2], end="")
                elif i[j+1].isdigit():
                    print(i[j] * int(i[j+1]), end = "")

