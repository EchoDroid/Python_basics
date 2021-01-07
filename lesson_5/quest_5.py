""" 5) Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """


from random import randint

file_name = 'quest_5.txt'
gen_num_list = [str(randint(1, 100)) for _ in range(20)]
int_list = []
with open(file_name, 'w') as f_obj:
    print(' '.join(gen_num_list), file=f_obj)
print(f'В файл {file_name} успешно записана строка')

try:
    with open(file_name, 'r') as f_obj:
        int_list = [int(el) for el in f_obj.readline().split(' ')]
except FileNotFoundError:
    print(f'Ошибка: файл {file_name} не найден!')
except IOError:
    print(f'Ошибка чтения файла {file_name}!')
finally:
    print(f'Сумма чисел в строке: {sum(int_list)}')
