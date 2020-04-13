"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""

i_stop = 0
while True:
    user_tmp = input('Введите желаемое количество элементов:\n')
    if user_tmp.isdigit():
        i_stop = int(user_tmp)
        break
    print('Ошибка при вводе, введите число!')

my_list = []
while len(my_list) < i_stop:
    user_tmp = input(f'Введите элемент списка № {len(my_list)}\n')
    my_list.append(user_tmp)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# i_stop = len(my_list)

i_stop = (i_stop - 1, i_stop - 2)[i_stop % 2]

print(f'Список до перестановки {my_list}')
for i in range(0, i_stop, 2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print(f'Список после перестановки {my_list}')
