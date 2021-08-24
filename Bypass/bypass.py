import os

path = "C:\\Street"

def bypass(path ,level=1):
    print(f"Level: {level}, Content: {os.listdir(path)}")
    for i in os.listdir(path):
        if os.path.isdir(path + "\\" + i):
            print("Спускаемся на уровень ниже!" , path + "\\" + i)
            bypass(path + "\\" + i, level+1)
            print("Поднимаемся обратно! на уровень выше!")
bypass(path)

