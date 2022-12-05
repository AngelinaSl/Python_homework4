# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random

power = int(input("Введите степень k: "))
my_list = []
y = power
j = 0
for i in range(0, power - 1):
    w = random.randint(0, 101)
    if w != 0:
        my_list.append(f"{w}*(x**{y})")
        j += 1
        y -= 1
s1 = ""
for j in range(0, len(my_list)):
    s1 += f"{(my_list[j])} + "
q1 = random.randint(0, 101)
q2 = random.randint(0, 101)
if q1 == 0 and q2 == 0:
    s = " = 0"
elif q1 == 0:
    s = f"{q2} = 0"
elif q2 == 0:
    s = f"{q1}*x = 0"
else:
    s = f"{q1}*x + {q2} = 0"
result = s1 + s
print(result)

with open('text.txt', 'w') as task_4:
    task_4.write(result)