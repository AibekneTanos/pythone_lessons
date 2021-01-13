import json
name = input("Введите ваша имя:")
print('Здраствуйте!', 'Хотите создать новый файл с вашими данными?')
doing = input("да, нет")

if doing == "да":
    fam = input("Введите вашу фамилию")
    birthday = input("Введите дату рождения")
    spisok = {
        'name': name,
        'family':fam,
        'birthday': birthday

    }


    json_filename = 'lesson/name'
    with open (json_filename, 'w') as f:
        json_str = json.dumps(spisok)
        print(">>", json_str)
        print('Готово')

if doing == 'нет':
    print('досвидание')


vopr = input('хоитите изменить данные файла?:')
if vopr == 'да':
    family = input('введите вашу фамилию:')
    date = input('введите вашу дату рождения:')
    spisok2 = {
        'name': name,
        'family': family,
        'birthday': date
    }
    json_filename = 'lesson/name'
    with open(json_filename, 'w') as f:
        json_str = json.dumps(spisok2)
        print(">>", json_str)
        print('Готово')
elif vopr == 'нет':
    print('закрыто')
