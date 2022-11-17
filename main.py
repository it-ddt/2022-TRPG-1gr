from random import choice, randint

first_names = ("Жран", "Дрын", "Жлыг")
last_name = ("Кривой", "Злопамятный", "Дикий")


def make_hero(
        name=None,
        hp_now=None,
        lvl=1,
        xp_next=1000,
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

    if money is None:
        hp_now = randint(1, 100)

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


def show_hero(hero):
    pass


p1 = make_hero()
p2 = make_hero()
p3 = make_hero()
