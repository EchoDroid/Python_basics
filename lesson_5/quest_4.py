""" 4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """


from excluded.common_fun import try_type


def text_by_numbers(word_dict: dict, *var):
    for itr in var:
        if itr < 19:
            tmp_str = word_dict.get(itr)
            return tmp_str[0].upper() + tmp_str[1:]
        elif itr < 100:
            tmp_str_1 = word_dict.get((itr // 10) * 10)     # взятие десятка
            tmp_str_2 = '' if not word_dict.get(itr % 10) else word_dict.get(itr % 10)  # взятие единиц, если нет то ''
            return tmp_str_1[0].upper() + tmp_str_1[1:] + ' ' + tmp_str_2
        else:
            return f'{itr} нет в словаре'


src_file_name = 'quest_4_src.txt'
res_file_name = 'quest_4_res.txt'
src_list = []
res_list = []
my_word_dict = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять',
                10: 'десять', 11: 'одинадцать', 12: 'двенадцать', 13: 'тренадцать', 14: 'четырнадцать',
                15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать',
                20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
                80: 'восемьдесят', 90: 'девяносто',}
""" Чтение данных из файла """
try:
    with open(src_file_name, 'r') as f_obj:
        while True:
            tmp_str = f_obj.readline().split(' — ')
            if tmp_str == ['']:
                break
            elif try_type(int, tmp_str[1]):
                src_list.append([tmp_str[0], int(tmp_str[1])])
            else:
                print(f'Ошибка в структуре данных файла {src_file_name}.\nСтрока {tmp_str}')
                exit(1)
except FileNotFoundError:
    print(f'Ошибка: файл {src_file_name} не найден!')
except IOError:
    print(f'Ошибка чтения файла {src_file_name}!')
finally:
    print(f'Данные успешно прочитаны из файла {src_file_name}')

""" Обработка данных """
for itr in src_list:
    tmp_str = text_by_numbers(my_word_dict, itr[1])
    res_list.append([tmp_str, itr[1]])

""" Запись обработанных данных в файл """
try:
    with open(res_file_name, 'w') as f_obj:
        for itr in res_list:
            print(itr[0] + ' — ' + str(itr[1]), file=f_obj)
except IOError:
    print(f'Ошибка записи в файл {res_file_name}!')
finally:
    print(f'Данные обработаны и успешно записаны в файл {res_file_name}')
