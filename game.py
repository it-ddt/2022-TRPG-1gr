import os
import shop

def start_game():
    os.system("cls")
    print("Игра началась")

    # создаем игрока - КОРТЕЖ!!!
    player_name = "Вася Питонов"
    player_hp = 100
    player_money = 50
    player_potions = 1
    player = (player_name, player_hp, player_money, player_potions)

    # начался главный цикл игры
    while True:
        os.system("cls")

        # показываем персонажа
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
