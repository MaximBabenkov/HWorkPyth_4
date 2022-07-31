#  Вычислить число π c заданной точностью d

#  Пример:

#  при d = 0.001, π = 3.141.   10^-1 ≤ d ≤ 10^-10

def get_numb_decim_places(accuracy: float) -> int: 
    numb = 0
    while accuracy != 1:
        accuracy *= 10
        numb += 1
    return numb

def pi_Bailey_Borwein_Plouffe(value: int) -> float:
    pi = 0.0 
    for i in range (value):
        pi += (1 / (16 ** i)) * ((4 / (8 * i + 1)) -
            (2 / (8 * i + 4)) - (1 / (8 * i + 5)) - (1 / (8 * i + 6)))
    return pi

d = float(input('Enter the desired accuracy: '))
amount = get_numb_decim_places(d)
print('Your number of decimal places:', amount)
numb_pi = pi_Bailey_Borwein_Plouffe(amount)
print('Your number π:', round(numb_pi, amount))
