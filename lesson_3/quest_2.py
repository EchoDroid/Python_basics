""" Реализовать функцию, принимающую несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Реализовать вывод данных о
пользователе одной строкой.

"""


def my_print(name, surname, year_birth, city, email, phone):
    print(f'{name} {surname}, {year_birth} года рождения. Проживает в городе {city}. Контактный телефон: {phone}, '
          f'email: {email}')


my_name = input('Введите Ваше имя:\n')
my_surname = input('Введите Вашу фамилию:\n')
my_birth = input('Введите Ваш год рождения:\n')
my_city = input('Введите Ваш город проживания:\n')
my_email = input('Введите Ваш адрес электронной почты:\n')
my_phone = input('Введите Ваш телефон:\n')

my_print(phone=my_phone, year_birth=my_birth, city=my_city, email=my_email, name=my_name, surname=my_surname)
