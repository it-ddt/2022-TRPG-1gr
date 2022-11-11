from random import randint, choice


first_names = ("Жран", "Дрын", "Брысь", "Жлыг")
last_names = ("Зловонный", "Борзый", "Дикий", "Ужасный")


def make_hero(name=None, hp=None, xp=None, attack=None, defence=None, money=None, potions=None) -> tuple:
    if not name:
        name = f"{choice(first_names)} {choice(last_names)}"
    if not hp:
        hp = randint(1, 100)
    if not xp:
        xp = randint(0, 100)
    if not attack:
        attack = randint(1, 5)
    if not defence:
        defence = randint(0, 3)
    if not money:
        money = randint(0, 100)
    if not potions:
        potions = randint(0, 3)

    return (name, hp, xp, attack, defence, money, potions)
