""" 6) Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести словарь на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) ​ — ​ 10(лаб)
Физкультура: ​ — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


file_name = 'quest_6.txt'
my_dict = {}
""" Чтение данных из файла """
try:
    with open(file_name, 'r') as f_obj:
        for line in f_obj:
            key = ''
            sum_val = 0
            char_ind = line.find(':')

            if char_ind + 1:
                key = line[:char_ind]
            else:
                print(f'Не найден предмет в строке {line}')
                continue
            tmp_list = line[char_ind + 1:].split(' ')

            for itr in tmp_list[1:]:
                char_ind = itr.find('(')        # если не найдено - возвращает -1
                if char_ind + 1:                # -1 + 1 = 0
                    try:
                        sum_val += int(itr[0:char_ind])
                    except ValueError:
                        print(f'Ошибка преобразования в строке {itr}')
            my_dict.setdefault(key, sum_val)
except FileNotFoundError:
    print(f'Ошибка: файл {file_name} не найден!')
except IOError:
    print(f'Ошибка чтения файла {file_name}!')
finally:
    print(f'Данные успешно прочитаны из файла {file_name}\n{my_dict}')
