import os
import shop
import hero_engine


def make_hero(name="Безымянный", hp=1, money=0, potions=0) -> tuple:
    return (name, hp, money, potions)


def start_game():
    os.system("cls")
    print("Игра началась")

    # создаем игрока - КОРТЕЖ!!!
    player = hero_engine.make_hero()

    # начался главный цикл игры
    while True:
        os.system("cls")

        # показываем персонажа
        # TODO: отправить в модуль hero_engine
        print("Персонаж: ")
        print("имя:", player[0])
        print("здоровье:", player[1])
        print("деньги:", player[2])
        print("зелья:", player[3])
        print("------------------")

        # показываем варианты
        print("1 - Поехать в лавку алхимика")
        print("0 - Выйти в главное меню")
        
        # выбираем вариант и проверяем его
        answer = input("\nВведите номер варианта и нажмите ENTER: ")
        if answer == "1":
            player = shop.show(player)

            
start_game()
