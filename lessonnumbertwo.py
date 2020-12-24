month = int(input("Введите мсяц рождения:"))
birthday = int(input("Введите день рождения:"))

mart = list(range(21, 31))
mart2 = list(range(22, 31))
mart3 = list(range(23, 31))
mart4 = list(range(24, 31))

aprel = list(range(1, 20))
aprel2 = list(range(1, 22))
aprel1 = list(range(1, 21))
aprel3 = list(range(1, 23))


if month == 3 and birthday in mart or month == 4 and birthday in aprel:
    print("Ваш гороскоп:Овен")
elif month == 4 and birthday in mart or month == 5 and birthday in aprel:
    print("Ваш гороскоп:Телец")
if month == 5 and birthday in mart or month == 6 and birthday in aprel1:
    print("Ваш гороскоп:Близнецы")
elif month == 6 and birthday in mart2 or month == 7 and birthday in aprel2:
    print("Ваш гороскоп:Рак")
if month == 7 and birthday in mart3 or month == 8 and birthday in aprel3:
    print("Ваш гороскоп:Лев")
elif month == 8 and birthday in mart4 or month == 9 and birthday in aprel3:
    print("Ваш гороскоп:Дева")
if month == 9 and birthday in mart4 or month == 10 and birthday in aprel3:
    print("Ваш гороскоп:Весы")
elif month == 10 and birthday in mart4 or month == 11 and birthday in aprel2:
    print("Ваш гороскоп:Скорпион")
if month == 11 and birthday in mart3 or month == 12 and birthday in aprel1:
    print("Ваш гороскоп:Стрелец")
elif month == 12 and birthday in mart2 or month == 1 and birthday in aprel:
    print("Ваш гороскоп:Козерог")
if month == 1 and birthday in mart or month == 2 and birthday in aprel:
    print("Ваш гороскоп:Водолей")
elif month == 2 and birthday in mart or month == 3 and birthday in aprel:
    print("Ваш гороскоп:Рыбы")
#else :
    #print("Введена неправильная дата")