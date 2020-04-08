"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


time = 0
while True:
    user_str = input('Введите время в секундах:\n')
    if user_str.isdigit():
        time = int(user_str)
        break

hour = time // 3600
minute = (time - hour * 3600) // 60
second = time - minute * 60 - hour * 3600

print(f'Введнные {time} секунд это {hour:>02}:{minute:>02}:{second:>02}')