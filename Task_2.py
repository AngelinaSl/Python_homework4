# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def search_prime_numbers(x: int):
    prime_numbers = []
    y = 2
    while y * y <= x:
        if x % y == 0:
            prime_numbers.append(y)
            x //= y
        else:
            y += 1
    prime_numbers.append(x)
    return prime_numbers


number = int(input("Введите число: "))
print(f'{number} = {search_prime_numbers(number)}')

