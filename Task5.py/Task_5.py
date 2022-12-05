# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

with open('task_5_1.txt', 'r') as t1:
    s_first = t1.readline()
print(f'Первый многочлен: {s_first}')

with open('task_5_2.txt', 'r') as t2:
    s_second = t2.readline()
print(f'Второй многочлен: {s_second}')

s1 = s_first
s2 = s_second

s1 = s1.replace(f')', '')
s1 = s1.replace(f' = 0', '')
s2 = s2.replace(f')', '')
s2 = s2.replace(f' = 0', '')

lst_1 = s1.split(" + ")
lst_2 = s2.split(" + ")


# Создание словарей, где ключ - это степень в выражении, а значение - множитель выражения
my_dict_1 = {}
for i in range(0, len(lst_1) - 1):
    my_str_1 = lst_1[i]
    if my_str_1[0] != '*' and my_str_1[1] != '*':
        my_dict_1[my_str_1[-1]] = int(f'{my_str_1[0]}{my_str_1[1]}')
    elif my_str_1[0] != '*' and my_str_1[1] == '*':
        my_dict_1[my_str_1[-1]] = int(f'{my_str_1[0]}')

my_dict_2 = {}
for i in range(0, len(lst_2) - 1):
    my_str_2 = lst_2[i]
    if my_str_2[0] != '*' and my_str_2[1] != '*':
        my_dict_2[my_str_2[-1]] = int(f'{my_str_2[0]}{my_str_2[1]}')
    elif my_str_2[0] != '*' and my_str_2[1] == '*':
        my_dict_2[my_str_2[-1]] = int(f'{my_str_2[0]}')


# Объединение списков в один, включая те значения, которые могут не повторяться в одном из многочленов
my_dict_control = {}
for key_1 in my_dict_1:
    for key_2 in my_dict_2:
        if key_1 == key_2:
            my_dict_control[key_1] = my_dict_1[key_1] + my_dict_2[key_2]
my_dict_1.update(my_dict_control)
my_dict_2.update(my_dict_1)


result = ''
for key_2 in my_dict_2:
    result += f"{my_dict_2[key_2]}*(x**{key_2}) + "
r1 = lst_1[-1]
r2 = lst_2[-1]
if s_first[-5] == ")" and s_second[-5] == ")":
    result = result[:-3]
    result = result + " = 0"
elif r2[-2] == '*':
    result = result + f'{r1[0]}{r1[1]} = 0'
elif r1[-2] == '*':
    result = result + f'{r2[0]}{r2[1]} = 0'
elif len(lst_1[-1]) == len(lst_2[-1]) and r1[-2] != '*' and r2[-2] != '*':
    r = int(f"{r1[0]}{r1[1]}") + int(f"{r2[0]}{r2[1]}")
    result = result + f'{r} = 0'
print(f'Сумма многочленов: {result}')


with open('task_5_result.txt', 'w') as t_result:
    t_result.write(result)