"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с
параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать
программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

import time

"""
# Запрашиваем у пользователя стуктуру данных
key_list = []
while True:
    user_tmp = input('Введите структуру данных, разделяя заголовки пробелом.\nНапример: Название Цена Количество Ед\n')
    if user_tmp:
        key_list = user_tmp.split(' ')
        break
    print('Вы оставили строку пустой, нужно хотя-бы одно слово!')

# Запрашиваем у пользователя количество строк с данными
data_count = 0
while True:
    user_tmp = input('Введите количество вводимых строк:\n')
    if user_tmp.isdigit():
        data_count = int(user_tmp)
        break
    print('Ошибка при вводе, введите натуральное число!')

# Запрашиваем у пользователя данные
data_summary = []
counter = 0
while counter < data_count:
    user_tmp = input(f'Введите строку данных №{counter+1} разделяея значения пробелом:\n')
    if not user_tmp:
        print('Вы оставили строку пустой, нужно хотя-бы одно слово!')
        continue

    data_list = user_tmp.split(' ')
    data_len = len(data_list)
    key_len = len(key_list)
    if data_len > key_len:
        print(f'Вы ввели на {data_len - key_len} больше данных чем имеется параметров, попробуйте снова')
        continue
        # Запрос у пользователя решения по 'лишним' данным
        # flag = False
        # while True:
        #     user_tmp = input(f'Вы ввели на {data_len - key_len} больше данных чем имеется параметров.\n'
        #                      f'Чтобы добавить новые параметры введите "Да"\n'
        #                      f'Чтобы отбросить {data_list[key_len - 1:]} введите "Нет"\n')
        #     if user_tmp.find('Д'):
        #         flag = True
        #         break
        #     elif user_tmp.find('Н'):
        #         flag = False
        #         break
        #     else:
        #         print('Ошибка ввода! Введите Да или Нет')
        #
        # # Запрос у пользователя новых параметров, если он выбрал этот вариант
        # while flag and len(key_list) < data_len:
        #     diff_tmp = data_len - key_len
        #     user_tmp = input(f'Введите {diff_tmp} новых параметра через пробел\n')
        #     key_tmp = user_tmp.split(' ')
        #     if len(key_tmp) == diff_tmp:
        #         key_list.extend(key_tmp)
        #         key_len = len(key_list)
        #         break
        #     elif len(key_tmp) < diff_tmp:
        #         print('Вы ввели меньше параметров, чем требовалось')
        #     else:
        #         print('Вы ввели меньше больше, чем требовалось')
    elif data_len < key_len:
        print(f'Вы ввели на {key_len - data_len} меньше данных чем имеется параметров, попробуйте снова')
        continue
    if data_len == key_len:
        temp_dict = {}
        # temp_dict.fromkeys(key_list)
        for i in range(data_len):
            temp_dict.setdefault(key_list[i], data_list[i])
        data_summary.append((counter + 1, temp_dict))
    counter += 1
print('data_tuple', data_summary)
"""
data_summary = [(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
                (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
                (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})]

avg_keys_time = 0.0
avg_analytics_time = 0.0

for i in range(1000000):

    time_start = time.time() * 10**6

# Создание списка ключей с использованием set ~0.99 нс
    key_list = set()
    for imt in data_summary:
        key_list.update(imt[1].keys())
    key_list = list(key_list)

# Создание списка ключей только с list ~1.68 нс
    # key_list = []
    # for imt in data_summary:
    #     for key in imt[1].keys():
    #         if not key_list.count(key):
    #             key_list.append(key)

    time_end = time.time() * 10**6
    # print(f'Создание списка ключей {time_end - time_start} нс')
    avg_keys_time += time_end - time_start

    time_start = time.time() * 10**6

# Аналитика с использованием set ~3.54 нс
    data_len = len(data_summary)
    # new_dict = {key: set() for key in key_list}
    # for data in data_summary:
    #     for key in key_list:
    #         new_dict.get(key).add(data[1].get(key))
    # print(new_dict)
# Аналитика только с list ~5.24 нс
    # new_dict = {key: [] for key in key_list}
    # for data in data_summary:
    #     for key in key_list:
    #         if not new_dict.get(key).count(data[1].get(key)):
    #             new_dict.get(key).append(data[1].get(key))
    # print(new_dict)
# Аналитика только с list и in ~4.78 нс
    new_dict = {key: [] for key in key_list}
    for data in data_summary:
        for key in key_list:
            if not (data[1].get(key) in new_dict.get(key)):
                new_dict.get(key).append(data[1].get(key))
    # print(new_dict)

    time_end = time.time() * 10**6
    # print(f'Аналитика {time_end - time_start} нс')
    avg_analytics_time += time_end - time_start

avg_keys_time /= 1000000
avg_analytics_time /= 1000000

print(f'Создание списка ключей в среднем {avg_keys_time} нс')
print(f'Аналитика в среднем {avg_analytics_time} нс')
