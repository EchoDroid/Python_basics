""" Реализовать функцию ​ int_func()​ , принимающую слово из маленьких латинских букв и
возвращающую его же, но с прописной первой буквой. Например, ​ print(int_func(‘text’))​ -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
использовать написанную ранее функцию ​ int_func()​ .

"""


def str_letter_up(my_str):
    return my_str if my_str == '' else ''.join([my_str[0].upper(), my_str[1:]])


def str_all_up(my_str):
    tmp_list = my_str.split(' ')
    tmp_new = []
    for itr in tmp_list:
        tmp_new.append(str_letter_up(itr))
    return ' '.join(tmp_new)


print(str_letter_up('text'))
print(str_all_up('my some text'))
