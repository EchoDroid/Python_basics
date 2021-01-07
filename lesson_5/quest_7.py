""" 7) Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее ​ не включать​Далее реализовать список. Он должен содержать
словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{​
"firm_1": 5000, ​
"firm_2": 3000, ​
"firm_3": 1000​ },
{"average_profit": 2000​}]
Подсказка: использовать менеджер контекста. """

import json
from excluded.common_fun import try_type

src_file_name = 'quest_7.txt'
res_file_name = 'quest_7_json.txt'
data_list = [{}, {}]
try:
    with open(src_file_name, 'r') as f_obj:
        while True:
            tmp_str = f_obj.readline().split(' ')
            if tmp_str == ['']:
                break
            elif try_type(float, tmp_str[2], tmp_str[3]):
                tmp_profit = round(float(tmp_str[2]) - float(tmp_str[3]), 2)
                data_list[0].setdefault(tmp_str[0], tmp_profit)
            else:
                print(f'Ошибка в структуре данных файла {src_file_name}.\nСтрока {tmp_str}')
                exit(1)
except FileNotFoundError:
    print(f'Ошибка: файл {src_file_name} не найден!')
except IOError:
    print(f'Ошибка чтения файла {src_file_name}!')
finally:
    print(f'Данные успешно прочитаны из файла {src_file_name}')

""" Вычисление средней прибыли """
if not data_list:
    print(f'Файл {src_file_name} был пуст!')
tmp_list = [el for el in data_list[0].values() if el > 0]
avg_profit = round(sum(tmp_list)/len(tmp_list), 2)
data_list[1].setdefault('average_profit', avg_profit)

""" Запись json данных в файл """
try:
    with open(res_file_name, 'w') as f_obj:
        json.dump(data_list, f_obj)
except IOError:
    print(f'Ошибка записи в файл {res_file_name}!')
finally:
    print(f'Данные обработаны и успешно записаны в файл {res_file_name}')
