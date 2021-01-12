pole = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

for i in range(9):
    krestik = int(input("Введите номер столбика что бы поставить крестик "))
    krestikk = int(input("Введите номер ряда "))
    pole[krestik][krestikk] = 'X'
    print(pole)


    nolik = int(input("Введите номер столбика что бы поставить нолик "))
    nolikk = int(input("Введите номер ряда"))
    pole[nolik][nolikk] = 'O'
    print(pole)


