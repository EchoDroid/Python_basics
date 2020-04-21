""" 4) Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """


from excluded.common_fun import try_type

src_file_name = 'quest_4_src.txt'
res_file_name = 'quest_4_res.txt'
src_list = []
res_list = []
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


""" Запись обработанных данных в файл """
try:
    with open(res_file_name, 'w') as f_obj:
        for itr in res_list:
            print(itr[0] + ' — ' + itr[1], file=f_obj)
except IOError:
    print(f'Ошибка чтения файла {res_file_name}!')
finally:
    print(f'Данные обработаны и успешно записаны в файл {res_file_name}')
