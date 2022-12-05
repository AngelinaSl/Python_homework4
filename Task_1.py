# Вычислить число Пи c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141
# Ввод: 0.01
# Вывод: 3.14

import math

number = float(input("Введите точность: "))
print(round(math.pi, (len(str(number)) - 2)))