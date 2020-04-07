#При решении задачи не понял, как можно список и словарь заставить работать вместе
#Поэтому просто их задействовал, а решил, как понял через if
month = (int(input('Введите номер месяца ')))
year = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
season = dict(winter = 'Зима', spring = 'Весна', summer = 'Лето', autumn = 'Осень')
if 0 < month < 13 :
    x = year.index(month)
    if 1 <= x <= 2 or x == 12 :
        print(season.get('winter'))
    elif 3 <= x <= 5 :
        print(season.get('spring'))
    elif 6 <= x <= 8 :
        print(season.get('summer'))
    elif 9 <= x <= 11 :
        print(season.get('autumn'))
else :
    print('Число месяца введено неверно')