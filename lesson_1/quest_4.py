"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.
"""


user_str = ''
while True:
    user_str = input('Введите положительное целое число:\n')
    if user_str.isdigit():
        if int(user_str) > 0:
            break
        else:
            print('Число меньше 0!')
    else:
        print('Это не целое число!')

max_num = 0
i = 0
while i < len(user_str):
    if max_num < int(user_str[i]):
        max_num = int(user_str[i])

    i += 1

print(f'Наибольшая цифра в строке {max_num}')