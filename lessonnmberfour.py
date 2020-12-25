s = []


def list () :
    mark = input("Введите марку авто:")
    model = input("Введите модель авто:")
    year = input("Введите год авто:")
    s.append(mark)
    s.append(model)
    s.append(year)
for i in range (3):
    list()
    print(s)
