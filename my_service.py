""" Скрип для хранения общеупотребих функций """


def try_type(var, var_type):
    try:
        var_type(var)
        return True
    except ValueError:
        return False
