import os
from random import randint, choice

first_names = ("Жран", "Дрын", "Брысь", "Жлыг")
last_names = ("Ужасный", "Зловонный", "Борзый", "Кровавый")


def make_hero(
        name=None,
        hp_now=None,
        hp_max=None,
        lvl=1,
        xp_now=0,
        attack=1,
        defence=1,
        weapon=None,
        shield=None,
        luck=1,
        money=None,
        inventory=None,
) -> dict:

    if not name:
        name = choice(first_names) + " " + choice(last_names)

    if not hp_now:
        hp_now = randint(1, 100)
    
    if not hp_max:
        hp_max = hp_now

    xp_next = lvl * 100

    if money is None:
        money = randint(0, 100)

    if not inventory:
        inventory = []

    if not weapon:
        weapon = {
            "тип": "оружие",
            "название": "Обычный меч",
            "стат": "атака",
            "модификатор": 2,
            "цена": 10
        }
    
    return {
        "имя": name,
        "здоровье": hp_now,
        "здоровье макс": hp_max,
        "уровень": lvl,
        "опыт": xp_now,
        "опыт след": xp_next,
        "оружие": weapon,
        "щит": shield,
        "атака": attack,
        "защита": defence,
        "удача": luck,
        "деньги": money,
        "инвентарь": inventory
    }


def equip_item(hero: dict) -> None:
    """
    Показать пронумерованные предметы:
        Только щиты и оружие?
        Или все?

    Выбирается предмет
    Если другой предмет был экипирован:
        Текущий предмет положить в инвентарь
        Оружие персонажа становится выбранным предметом
        Выбранный предмет исчезает из инвентаря
    Если никакого предмета не было экипировано:
        Оружие персонажа становится выбранным предметом
        Выбранный предмет исчезает из инвентаря
    Пересчитать статы
    """
    pass


def show_item(item: dict) -> None:
    """
    Показывает предмет: название модификатор стат
    TODO: вернуть строку
    """
    if item:
        if item['модификатор'] >= 0:
            print(f"{item['название']} +{item['модификатор']} {item['стат']}")
        else:
            print(f"{item['название']} {item['модификатор']} {item['стат']}")
    else:
        print("-нет-")


def show_items(items: list) -> None:
    print("предметы:")
    if items:
        for num, item in enumerate(items):
            print(f"{num}.", end=" ")
            show_item(item)
    else:
        print("-нет-")


def show_equipped(hero: dict) -> None:
    print("оружие:", end=" ")
    show_item(hero['оружие'])
    print("щит:", end=" ")
    show_item(hero['щит'])


def show_hero(hero: dict) -> None:
    print("имя:", hero['имя'])
    print("здоровье:", hero['здоровье'], "/", hero['здоровье макс'])
    print("уровень:", hero['уровень'])
    print("опыт:", hero['опыт'], "/", hero['опыт след'])
    show_equipped(hero)
    print("атака:", hero['атака'])
    print("защита:", hero['защита'])
    print("удача:", hero['удача'])
    print("деньги:", hero['деньги'])
    show_items(hero['инвентарь'])
    print("")


def levelup(hero: dict) -> None:
    """
    TODO: что растет с уровнем?
    """
    while hero['опыт'] >= hero['опыт след']:
        hero['уровень'] += 1
        hero['опыт след'] = hero['уровень'] * 100
        print(f"{hero['имя']} получил {hero['уровень']} уровень\n")


def buy_item(hero: dict, price: int, item: str) -> None:
    """
    Покупает предмет item за price монет и кладет его в инвентарь героя
    """
    os.system("cls")
    if hero['деньги'] >= price:
        hero['деньги'] -= price
        hero['инвентарь'].append(item)
        print(f"{hero['имя']} купил {item} за {price} монет!")
    else:
        print(f"У {hero['имя']} нет столько монет! Не хватило {price - hero['деньги']}")
    input("\nНажмите ENTER чтобы продолжить")


def consume_item(hero: dict) -> None:
    """
    Удаляет предмет из инвентаря по индексу и дает герою эффект этого предмета
    """
    show_options(hero, hero['инвентарь'])
    idx = choose_option(hero, hero['инвентарь'])

    if idx is not None:
        if idx <= len(hero['инвентарь']) - 1 and idx > -1:
            print(f"{hero['имя']} употребил {hero['инвентарь'][idx]}")
            if hero['инвентарь'][idx] == "зелье":
                hero['здоровье'] += 10
                if hero['здоровье'] > hero['здоровье макс']:
                    hero['здоровье'] = hero['здоровье макс']
            elif hero['инвентарь'][idx] == "яблоко":
                pass
            else:
                print("Никакого эффекта")
            hero['инвентарь'].pop(idx)
        else:
            print("Нет такого индекса!")
        print("")


def play_dice(hero: dict, bet: str) -> None:
    """
    Ставка от 1 монеты до количества монет героя
    Игрок и казино бросаю кости, кто больше, то забирает ставку
    TODO: Как удача влияет на кости?
    """
    try:
        bet = int(bet)
    except ValueError:
        print("Ставка должна быть числом!")
    else:
        if bet > 0:
            if hero['деньги'] >= bet:
                hero_score = randint(2, 12)
                casino_score = randint(2, 12)
                print(f"{hero['имя']} выбросил {hero_score}")
                print(f"Трактирщик выбросил {casino_score}")
                if hero_score > casino_score:
                    hero['деньги'] += bet
                    print(f"{hero['имя']} выиграл {bet} монет")
                elif hero_score < casino_score:
                    hero['деньги'] -= bet
                    print(f"{hero['имя']} проиграл {bet} монет")
                else:
                    print("Ничья!")
            else:
                print(f"У {hero['имя']} нет денег на такую ставку!")
        else:
            print("Ставки начинаются от 1 монеты")
    input("\nНажмите ENTER чтобы продолжить")


def combat_turn(attacker, defender):
    if attacker['здоровье'] > 0:
        damage = attacker['атака']
        defender['здоровье'] -= damage
        print(f"{attacker['имя']} ударил {defender['имя']} на {damage} жизней!")


def start_fight(hero: dict) -> None:
    """
    Зависит ли враг от уровня героя?
    Формула аткаи и защиты?
    """
    os.system("cls")
    enemy = make_hero(hp_now=30, xp_now=123, inventory=["вражеский меч", "вражеский конь"])

    show_hero(hero)
    show_hero(enemy)

    while hero['здоровье'] > 0 and enemy['здоровье'] > 0:
        options = [
            "Атаковать протиника",
            "Употребить предмет из инвентаря"
        ]
        show_options(hero, options)
        option = choose_option(hero, options)
        os.system("cls")
        if option == 0:
            combat_turn(hero, enemy)
            combat_turn(enemy, hero)
            print("")
            show_hero(hero)
            show_hero(enemy)
        elif option == 1:
            consume_item(hero)
            combat_turn(enemy, hero)
            print("")
            show_hero(hero)
            show_hero(enemy)
        

    count_fight_result(hero, enemy)
    input("\nНажмите ENTER чтобы продолжить")
    return visit_arena(hero)


def count_fight_result(hero, enemy):
    os.system("cls")

    if hero['здоровье'] > 0 and enemy['здоровье'] <= 0:
        print(f"{hero['имя']} победил и получает в награду:")
        hero['опыт'] += enemy['опыт']
        print(enemy['опыт'], "опыта")
        hero['деньги'] += enemy['деньги']
        print(enemy['деньги'], "монет")
        print("и предметы: ", end="")
        print("")
        for item in enemy['инвентарь']:
            print(item, end=", ")
        hero['инвентарь'] += enemy['инвентарь']
        levelup(hero)
    elif hero['здоровье'] <= 0 and enemy['здоровье'] > 0:
        print(f"{enemy['имя']} победил!")
        print("Игра должна закончиться тут!")
    else:
        print(f"{hero['имя']} и {enemy['имя']} пали в бою:(")
        print("Игра должна закончиться тут!")


def show_options(hero: dict, options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def choose_option(hero: dict, options: list) -> int:
    """
    Получает ввод пользователя
    Проверяет ввод и возвращает его, если он есть в вариантах
    """
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except ValueError:
        print("Ввод должен быть целым неотрицательным числом")
        return choose_option(hero, options)
    else:
        if option < len(options) and option > -1:
            return option
        else:
            print("Нет такого выбора")
            return choose_option(hero, options)


def visit_hub(hero: dict) -> None:
    text = f"{hero['имя']} приехал в Хаб, здесь есть чем заняться."
    options = [
        "Заглянуть в лавку алхимика",
        "Поехать в трактир",
        "Отправиться на арену",
        "Выйти в главное меню"
    ]
    os.system("cls")
    show_hero(hero)
    print(text)
    show_options(hero, options)
    option = choose_option(hero, options)
    os.system("cls")
    if option == 0:
        return visit_shop(hero)
    elif option == 1:
        return visit_casino(hero)
    elif option == 2:
        return visit_arena(hero)
    elif option == 3:
        print("Типа, ушли в меню")
    input("\nНажмите ENTER чтобы продолжить от Хаба")


def visit_shop(hero: dict) -> None:
    text = f"{hero['имя']} приехал в лавку алхимка. Здесь странно пахнет и продаются зелья."
    options = [
        "Купить зелье лечения за 10 монет",
        "Купить зелье опыта за за 30 монет",
        "Выйти из лавки в Хаб"
    ]
    os.system("cls")
    show_hero(hero)
    print(text)
    show_options(hero, options)
    option = choose_option(hero, options)
    if option == 0:
        buy_item(hero, 10, "зелье лечения")
        return visit_shop(hero)
    elif option == 1:
        buy_item(hero, 30, "зелье опыта")
        return visit_shop(hero)
    elif option == 2:
        return visit_hub(hero)


def visit_casino(hero: dict) -> None:
    text = f"{hero['имя']} приехал в трактир, трактирщик предлагает сыграть в кости на деньги"
    options = [
        "Сыграть в кости",
        "Выйти из лавки в Хаб"
    ]
    os.system("cls")
    show_hero(hero)
    print(text)
    show_options(hero, options)
    option = choose_option(hero, options)
    if option == 0:
        bet = input("\nВведитье, сколько поставить монет и нажмите ENTER: ")
        play_dice(hero, bet)
        return visit_casino(hero)
    elif option == 1:
        return visit_hub(hero)


def visit_arena(hero: dict) -> None:
    text = f"{hero['имя']} приехал на арену. Здесь гладиаторы сражаются друг с другом."
    options = [
        "Сражаться",
        "Съесть предмет из инвентаря",
        "Выйти в Хаб"
    ]
    os.system("cls")
    show_hero(hero)
    print(text)
    show_options(hero, options)
    option = choose_option(hero, options)
    os.system("cls")
    if option == 0:
        start_fight(hero)
    elif option == 1:
        consume_item(hero)
    elif option == 2:
        return visit_hub(hero)
