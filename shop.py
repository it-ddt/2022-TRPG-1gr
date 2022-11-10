import os


def show(player):
    # делаем ссылки на статы игрока
    name = player[0]
    hp = player[1]
    money = player[2]
    potions = player[3]

    while True:
        # очищаем экран и показываем текст лавки
        os.system("cls")
        print(f"{name} приехал в лавку алхимика")

        # показываем персонажа
        print("Персонаж: ")
        print("имя:", name)
        print("здоровье:", hp)
        print("деньги:", money)
        print("зелья:", potions)
        print("")

        # показываем варианты в лавке
        print("1 - купить зелье за 10 монет")
        print("2 - уехать обратно к камню")
        answer = input("\nВведите номер варианта и нажмите ENTER: ")

        if answer == "1":
            os.system("cls")
            if money >= 10:
                money -= 10  # изменит деньги
                potions += 1
                print("Купили зелье")
            else:
                print("Недостаточно монет!")
            input("\nНажмите ENTER чтобы продолжить")
        elif answer == "2":
            return (name, hp, money, potions)
