""" 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
подсчет количества строк, количества слов в каждой строке. """


file_name = 'quest_2.txt'
try:
    with open(file_name, 'r') as f_obj:
        line_counter = 0
        while True:
            tmp_str = f_obj.readline().split(' ')
            if tmp_str == ['']:
                break
            line_counter += 1
            print(f'Стока № {line_counter} содержит {len(tmp_str)} слова')
        print(f'В файле {f_obj.name} всего {line_counter} строки')
except FileNotFoundError:
    print(f'Ошибка: файл {file_name} не найден!')
except IOError:
    print(f'Ошибка чтения файла {file_name}!')
