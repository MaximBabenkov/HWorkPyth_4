# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N

def find_prime_factors(number: int) -> list:
    prime_factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            prime_factors.append(divisor)
            number /=  divisor
        else:
            divisor += 1
    return prime_factors

numb = int(input('Enter your number: '))
multipliers = find_prime_factors(numb)
print('Your prime factors:', multipliers)
