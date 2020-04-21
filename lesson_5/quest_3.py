""" 3) Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32 """


from excluded.common_fun import try_type

file_name = 'quest_3.txt'
try:
    with open(file_name, 'r') as f_obj:
        data_list = []
        while True:
            tmp_str = f_obj.readline().split(' ')
            if tmp_str == ['']:
                break
            elif try_type(float, tmp_str[1]):
                data_list.append([tmp_str[0], float(tmp_str[1])])
            else:
                print(f'Ошибка в структуре данных файла {file_name}.\nСтрока {tmp_str}')
                exit(1)
    if not data_list:
        print(f'Файл {file_name} был пуст!')
    low_list = [el for el in data_list if el[1] < 20000.00]
    average = sum([el[1] for el in data_list])/len(data_list)
    print('Следующие сотрудники имеют оклад менее 20 тыс.')
    for itr in low_list:
        print(itr[0])
    print(f'Среднее величина доходов сотрудников {round(average, 2)}')
except FileNotFoundError:
    print(f'Ошибка: файл {file_name} не найден!')
except IOError:
    print(f'Ошибка чтения файла {file_name}!')
