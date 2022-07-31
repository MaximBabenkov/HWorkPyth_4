import os

def get_data_from_file(path: os) -> str:
    with open(path, 'r') as file:
        data = str(file.read())
    return data

def get_coeffs(data: list) -> list: 
    poly = data.split()   
    coeffs = []
    for i in poly:
        if ('x' in i) and ('^' in i):
            coeffs.append([int(i[i.find('^')+1]), int(i[0:i.find('*')])])
        elif ('x' in i) and ('^' not in i):
            coeffs.append([1, int(i[0:i.find('*')])])
        elif ('x' not in i) and (i != '+') and (i != '=') and (i != '0'):        
            coeffs.append([0, int(i)])
    return coeffs

def get_poly_sum(list1:list, list2: list) -> str:
    poly_sum = ''
    for i in list1:
        for j in list2:
            if (j[0] == i[0] > 1):
                poly_sum += f'{i[1] + j[1]}*x^{i[0]} + '
            elif (j[0] == i[0] == 1):
                poly_sum += f'{i[1] + j[1]}*x + '
            elif (j[0] == i[0] == 0):
                poly_sum += f'{i[1] + j[1]} + '
    poly_sum = poly_sum[0:len(poly_sum)-2] + '= 0'
    return poly_sum

path_1 = os.path.join('Folder', 'FileTask_5_1.txt')
path_2 = os.path.join('Folder', 'FileTask_5_2.txt')

data_1, data_2 = get_data_from_file(path_1), get_data_from_file(path_2)

print('Your polynomials:')
print(data_1)
print(data_2)

list_1, list_2  = get_coeffs(data_1), get_coeffs(data_2)

summ_poly = get_poly_sum(list_1, list_2)
print('The sum of polynomials:\n', summ_poly)
   
path_3 = os.path.join('Folder', 'FileTask_5_3.txt')  
with open(path_3, 'w') as data:
    data.write(summ_poly)

print('The sum of polynomials is recorded in your file')
