""" Скрип для хранения общеупотребих функций """


def try_type(var_type, *var):
    try:
        for itr in var:
            var_type(itr)
        return True
    except ValueError:
        return False


def get_user_value(get_type: type):
    while True:
        tmp_str = input(f'Введите значение типа {get_type}: \n')
        if try_type(get_type, tmp_str):
            return get_type(tmp_str)
        print(f'Ошибка ввода!')