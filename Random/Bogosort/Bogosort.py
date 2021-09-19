import random

def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):                  # реализация алгоритма болотной сортировки
    while not is_sort(nums):
        random.shuffle(nums)
    return nums

numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print(numbers)                       # выводим начальный список

sorted_numbers = bogosort(numbers)

print(sorted_numbers)                # выводим отсортированный список




#Кол-во элементов	10	     11	     12 	13	      14	       15	      16
#Среднее время	0,0037 с  0,045 с	0,59 с	8,4 с	2,1 мин	    33,6 мин	9,7 ч
