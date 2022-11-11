import os


def show(player:tuple) -> tuple:
    # делаем ссылки на статы игрока
    money = player[5]
    potions = player[6]

    while True:
        # очищаем экран и показываем текст лавки
        os.system("cls")
        print(f"{player[0]} приехал в лавку алхимика")

        # показываем персонажа
        print("Персонаж: ")
        print("имя:", player[0])
        print("здоровье:", player[1])
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
            return (player[0], player[1], player[2], player[3], player[4], money, potions)