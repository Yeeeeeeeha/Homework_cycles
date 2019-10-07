born_year = 1799

while True:
    guess = int(input('Укажите год рождения А.С. Пушкина : '))
    if guess == born_year:
        print('Поздравляю, это правильный ответ!')
        break
    else:
        print('Неверно, попробуйте ещё раз...')

print('Завершение.')