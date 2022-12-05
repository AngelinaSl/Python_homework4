# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]


import random


def non_repeating_list(lst: list):
    lst_second = lst
    new_lst = str(lst)
    new_lst = new_lst[1:len(new_lst):3]
    n = 0
    for i in range(0, len(lst)):
        c = 0
        n += 1
        for j in range(n, len(lst_second)):

            if lst[i] == lst_second[j]:
                c += 1
        if c != 0:
            symbol_del = str(lst[i])
            new_lst = new_lst.replace(f'{symbol_del}', '')
    result = []
    for m in range(0, len(new_lst)):
        result.append(int(new_lst[m]))
    return result

my_lst = []
lst_len = random.randint(5, 8)
for t in range(0, lst_len):
    my_lst.append(random.randint(1, 5))
print(f"Ввод: {my_lst}")
print(f"Вывод: {non_repeating_list(my_lst)}")