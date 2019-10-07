true_year = 1799
true_day = "06.06"
born_year = None
born_day = None

while born_year != true_year:
    born_year = int(input('Укажите год рождения А.С. Пушкина : '))
    if born_year != true_year:
        print('Неверно, попробуйте еще раз...')
    if born_year == true_year:
        print('Поздравляю! Это правильный ответ! ')
        print('Быть может вы знаете и его день рождения?')

while born_day != true_day:
    born_day = input('Укажите день рождения А.С. Пушкина (чч.мм): ')
    if born_day != true_day:
        print('Неверно, попробуйте еще раз...')
    if born_day == true_day:
        print('Поздравляю! Вы прекрасно справились с заданием! ')

print('Завершение')
