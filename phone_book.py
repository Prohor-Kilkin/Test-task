"""Программа предназначена для записи, хранения, отображения, удаления и редактирования данных.
Данные хранятся в файле json-формата. Данные выводятся постранично, по 10 записей
на странице, есть возможность пролистывания вперед и назад. Поиск и удаление происходит по любой характеристике (это может быть
фамилия, имя, отчество, рабочий и домашний телефон). Редактирование производится по фамилии, введя фамилию человека,
 редактируем его профиль."""


import json


class AddressBook:
    data = []

    @staticmethod
    def rewrite_dz_json():
        with open("dz_json.json", "w") as f:
            json.dump(AddressBook.data, f, indent=4)

    @staticmethod
    def add_data():
        """Добавление данных в файл, функция записывает фамилию, имя, отчество,
         телефон рабочий, телефон домашний в json файл."""
        try:
            AddressBook.data = json.load(open("dz_json.json"))
        except FileNotFoundError:
            AddressBook.data = []

        AddressBook.data.append({
            'surname': input("Фамилия:"),
            'name': input("Имя:"),
            'patronymic': input("Отчество:"),
            'work_phone': input("Рабочий телефон:"),
            'home_phone': input("Домашний телефон:")
        })

        AddressBook.rewrite_dz_json()
        print("Данные добавлены.")

    @staticmethod
    def del_data(key):
        """Функция принимает ключ (ключом может быть фамилия, имя, отчество, рабочий и домашний телефон)
        и удаляет из json файла словарь с профилем по этому ключу."""
        with open("dz_json.json", "r") as f:
            persons = json.load(f)
            if not any(key in person.values() for person in persons):
                print("Такой профиль не найден")
            else:
                for person in persons:
                    if key in person.values():
                        persons.remove(person)
                    with open('dz_json.json', 'w') as f:
                        json.dump(persons, f, ensure_ascii=False, indent=4)
                print("Профиль удален.")

    @staticmethod
    def find_data(key):
        """Функция принимает ключ(ключом может быть фамилия, имя, отчество, рабочий и домашний телефон)
        и выводит на экран профиль из адресной книги."""
        with open("dz_json.json", "r") as f:
            persons = json.load(f)
            if not any(key in person.values() for person in persons):
                print("Такой профиль не найден")
            else:
                for person in persons:
                    if key in person.values():
                        print(person['surname'], person['name'], person['patronymic'], person['work_phone'],
                              person['home_phone'])

    @staticmethod
    def edit_data(key):
        """Функция принимает ключ(фамилию) и изменяет данные в профиле с этой фамилией."""
        with open("dz_json.json", "r") as f:
            persons = json.load(f)
            if not any(person['surname'] == key for person in persons):
                print("Такая фамилия не найдена.")
            else:
                for person in persons:
                    if key in person.values():
                        person['surname'] = input("Фамилия:")
                        person['name'] = input("Имя:")
                        person['patronymic'] = input("Отчество:")
                        person['work_phone'] = input("Рабочий телефон:")
                        person['home_phone'] = input("Домашний телефон:")
                        with open('dz_json.json', 'w') as f:
                            json.dump(persons, f, ensure_ascii=False, indent=4)
                        print("Данные профиля изменены.")

    @staticmethod
    def show_data(n):
        """Функция постранично выводит данные из json файла. На странице отображено 10 записей."""
        with open("dz_json.json", "r") as f:
            persons = json.load(f)
            i = 0
        for i in range(n, 10 + n):
            print(
                f"{i + 1}. {persons[i]['surname']} {persons[i]['name']} {persons[i]['patronymic']}  "
                f"Рабочий:  {persons[i]['work_phone']}  "
                f"Домашний: {persons[i]['home_phone']}""\n")
            i += 1
        x = int(input("Следующая страница, нажмите 1;" "\n"
                      "Предыдущая страница, нажмите 2;" "\n"
                      "Выход из режима просмотра, нажмите любую другую цифру" "\n"
                      "Ввод:  "))
        if x == 1:
            n += 10
            AddressBook.show_data(n)

        if x == 2:
            n -= 10
            AddressBook.show_data(n)


while True:
    print("*" * 50)
    print('''Выбор действия:
            1- Добавление данных
            2- Удаление данных
            3- Поиск данных
            4- Редактирование данных
            5- Просмотр данных
            6- завершение работы''')
    x = int(input("Ввод: "))
    if x <= 0 or x > 6:
        print("Введите цифру от 1 до 6.")

    if x == 1:
        AddressBook.add_data()
    elif x == 2:
        AddressBook.del_data(
            input("Чтобы удалить профиль введите один из параметров: фамилия, имя, отчество, телефон: "))
    elif x == 3:
        AddressBook.find_data(
            input("Чтобы найти профиль введите один из параметров: фамилия, имя, отчество, телефон: "))
    elif x == 4:
        AddressBook.edit_data(input("Введите фамилию для изменения профиля:  "))
    elif x == 5:
        AddressBook.show_data(0)
    elif x == 6:
        print("Программа завершена")
        break
