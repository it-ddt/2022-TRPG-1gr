import os
from random import choice, randint

first_names = ("Жран", "Дрын", "Жлыг")
last_name = ("Кривой", "Злопамятный", "Дикий")


def make_hero(
        name=None,
        hp_now=None,
        lvl=1,
        xp_next=None,
        xp_now=0,
        attack=1,
        defence=0,
        weapon=None,
        shield=None,
        money=None,
        luck=1,
        inventory=None,
) -> list:
    """
    Герой - это список
    [0] name - имя персонажа
    [1] hp_max - максимальное число жизней
    [2] hp_now - текущее число жизней, контролирует игру
    [3] lvl - уровень персонажа
    [4] xp_next - опыта для следующего уровня
    [5] xp_now - текущий опыт
    [6] attack - сила атаки
    [7] defence - защита
    [8] weapon - оружие
    [9] shield - щит
    [10] money - деньги
    [11] luck - удача
    [12] inventory - инвентарь, список
    """
    if not name:
        name = choice(first_names) + " " + choice(last_name)
    
    if not hp_now:
        hp_now = randint(1, 100)
    
    hp_max = hp_now

    xp_next = lvl * 1000

    if money is None:
        money = randint(1, 100)

    if not inventory:
        inventory = []

    return [
            name,
            hp_max,
            hp_now,
            lvl,
            xp_next,
            xp_now,
            attack,
            defence,
            weapon,
            shield,
            money,
            luck,
            inventory,
        ]


def show_hero(hero: list) -> None:
    """
    Герой - это список
    [0] name - имя персонажа
    [1] hp_max - максимальное число жизней
    [2] hp_now - текущее число жизней, контролирует игру
    [3] lvl - уровень персонажа
    [4] xp_next - опыта для следующего уровня
    [5] xp_now - текущий опыт
    [6] attack - сила атаки
    [7] defence - защита
    [8] weapon - оружие
    [9] shield - щит
    [10] money - деньги
    [11] luck - удача
    [12] inventory - инвентарь, список
    """
    print("имя:", hero[0])
    print("жизни:", hero[2], "/", hero[1])
    print("уровень:", hero[3])
    print("опыт:", hero[5], "/", hero[4])
    print("атака:", hero[6])
    print("защита:", hero[7])
    print("оружие:", hero[8])
    print("щит:", hero[9])
    print("деньги:", hero[10])
    print("удача:", hero[11])
    print("инвентарь:", hero[12])
    print("")


def levelup(hero: list) -> None:
    """TODO: Выбрать, какие повышать статы"""
    while hero[5] >= hero[4]:
        hero[3] += 1
        hero[4] = hero[3] * 1000
        print(f"{hero[0]} получил {hero[3]} уровень\n")


def buy_item(hero: list, item: str, price: int) -> None:
    """
    Проверяет, есть ли price денег у героя,
    если есть, отнимает из денег героя price
    и добавляет в инвентарь героя item
    """
    if hero[10] >= price:
        hero[10] -= price
        hero[12].append(item)
        print(f"{hero[0]} купил {item} за {price} монет!\n")
    else:
        print(f"{hero[0]} не хватило {price - hero[10]} монет!\n") 


def consume_item(hero: list, idx: int) -> None:
    """
    TODO: выпить зелье лечения так, чтобы hp_now не стало больше hp_max
    """
    if idx <= len(hero[12]) - 1 and idx > -1:
        print(f"{hero[0]} употребил {hero[12][idx]}")
        if hero[12][idx] == "зелье":
            hero[2] += 10
            if hero[2] > hero[1]:
                hero[2] = hero[1]
        elif hero[12][idx] == "яблоко":
            pass
        else:
            print("Употребил что-то неизвестное")
        hero[12].pop(idx)
    else:
        print("Нет такого предмета")


def play_dice(hero: list, bet: int) -> None:
    if bet > 0:
        if bet <= hero[10]:
            hero_score = randint(2, 12)
            casino_score = randint(2, 12)
            print(f"{hero[0]} выбросил {hero_score}")
            print(f"Трактирщик выбросил {casino_score}")
            if hero_score > casino_score:
                hero[10] += bet
                print(f"{hero[0]} победил и забирает {bet} монет!")
            elif hero_score < casino_score:
                hero[10] -= bet
                print(f"{hero[0]} проиграл {bet} монет!")
            else:
                print("Ничья!")
        else:
            print(f"У {hero[0]} нет столько монет!")
    else:
        print("Такая ставка невозможна! Ставки начинаются от 1 монеты!")


def start_fight(hero: list) -> None:
    """
    TODO:
        Нужен противник
        Обмен ударами с противником, пока игрок и противник живы
        Итог боя: проигрыш или победа
        Победа: добавить опыта от врага, забрать предметы врага в инвентарь героя
        Проигрыш: закончить игру
    """
    pass
