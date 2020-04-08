"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""


user_str = ''
while True:
    user_str = input('Введите любое целое число:\n')
    if user_str.isdigit():
        break

result = int(user_str) + int(user_str * 2) + int(user_str * 3)
print(f'Результат: {result}')