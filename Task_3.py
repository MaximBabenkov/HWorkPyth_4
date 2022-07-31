# Задайте последовательность чисел. Напишите программу, которая 
# # выведет список неповторяющихся элементов исходной последовательности

def get_unique_elements(elements: list) -> list:
    uniques = []
    for elem in elements:
        count = 0                  # счетчик повторяемости элементов
        for item in elements:
            if elem == item:
                count += 1
        if count == 1:
            uniques.append(elem)
    return uniques

list_in = list(map(int,input('Enter your space-separated numbers:\n').split()))
list_out = get_unique_elements(list_in)
print('Your list of non-repeating elements:\n', list_out)
