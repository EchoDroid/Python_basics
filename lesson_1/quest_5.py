"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


def try_type(var, var_type):
    try:
        var_type(var)
        return True
    except ValueError:
        return False


def get_value(quest_promt, wron_promt, type_1, type_2):
    while True:
        user_str = input(quest_promt + '\n')
        if try_type(user_str, type_1):
            return type_1(user_str)
        elif try_type(user_str, type_2):
            return type_2(user_str)
        else:
            print(wron_promt)


profitability = 0
employ_count = 0

income = get_value('Введите выручку вашей фирмы (руб):', 'Это не число!', int, float)
costs = get_value('Введите затраты вашей фирмы (руб):', 'Это не число!', int, float)

if income > costs:
    print('Поздравляю! Ваша фирма рентабельна!')
    profit = income - costs
    profitability = round(profit / income, 2)
    print(f'Рентабельность вашего предприятия составляет {profitability}')
    employ_count = get_value('Введите количество работников фирмы', 'Это не число!', int, int)
    profit_per_emp = round(profit / employ_count, 2)
    print(f'Прибыль фирмы в пересчёте на каждого работника составляет {profit_per_emp}')
else:
    print('Ваша фирма убыточна! Вам стоит оптимизировать расходы!')
