"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]

while True:
    while True:
        user_tmp = input('Введите натуральное число:\n')
        if user_tmp.isdigit():
            user_num = int(user_tmp)
            break
        print('Ошибка при вводе, введите число!')

    if user_num in my_list:
        el_ind = my_list.index(user_num)
        el_count = my_list.count(user_num)
        my_list.insert(el_ind + el_count, user_num)
    else:
        for imt in my_list[:]:
            if user_num > imt:
                el_ind = my_list.index(imt)
                my_list.insert(el_ind, user_num)
                break
        else:
            my_list.append(user_num)
    print(my_list)
