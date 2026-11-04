def can_vote():
    try:
        age = int(input("Введите возраст: "))
        citizen = bool(input("Является ли гражданином? Если нет, оставить пустым: "))
        disc = bool(input("Дисквалифицирован? Если нет, оставить пустым: "))
        print(age, citizen, disc)
        if age > 17 and citizen == True and disc == False:
            print("[can_vote]: Может голосовать!")
            return True
        else:
            print("[can_vote]: Не может голосовать!")
            return False

    except (ValueError, TypeError):
        print("Ошибка: Возраст должен быть целым числом, а гражданство и дисквалификация True|False!")
        return False


(can_vote())
