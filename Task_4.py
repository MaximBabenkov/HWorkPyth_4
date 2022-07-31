# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import os
path = os.path.join('Folder', 'FileTask_4.txt') 

import random

k = int(input('Enter your natural power of number: '))
polynomial = ""
while k >= 0:
    coef = random.randint(0, 100)
    if coef != 0:
        if k == 0:
            polynomial += (str(coef) + " = 0")
        elif k == 1:
            polynomial += (str(coef) + "*x" + " + ")            
        else: 
            polynomial += (str(coef) + "*x^" + str(k) + " + ")
    k -= 1
print('Your polynomial:\n', polynomial)

with open(path, 'w') as data:
    data.write(polynomial)

print('The polynomial is recorded in your file')