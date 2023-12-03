#!/usr/bin/python3

weapons = (
    ('Dagger',      8, 4, 0),
    ('Shortsword', 10, 5, 0),
    ('Warhammer',  25, 6, 0),
    ('Longsword',  40, 7, 0),
    ('Greataxe',   74, 8, 0),
)

armors = (
    ('Leather',     13, 0, 1),
    ('Chainmail',   31, 0, 2),
    ('Splintmail',  53, 0, 3),
    ('Bandedmail',  75, 0, 4),
    ('Platemail',  102, 0, 5),
)

rings = (
    ('Damage +1',   25, 1, 0),
    ('Damage +2',   50, 2, 0),
    ('Damage +3',  100, 3, 0),
    ('Defense +1',  20, 0, 1),
    ('Defense +2',  40, 0, 2),
    ('Defense +3',  80, 0, 3),
)

def equipment_total(equipment):
    weapon, armor, ring1, ring2 = equipment
    
    _, c, d, a = weapons[weapon]
    total_cost = c
    total_damage = d
    total_armor = a

    if armor is not None:
        _, c, d, a = armors[armor]
        total_cost += c
        total_damage += d
        total_armor += a

    if ring1 is not None:
        _, c, d, a = rings[ring1]
        total_cost += c
        total_damage += d
        total_armor += a

    if ring2 is not None:
        _, c, d, a = rings[ring2]
        total_cost += c
        total_damage += d
        total_armor += a

    return total_cost, total_damage, total_armor

def fight(player_damage, player_armor):
    player_hp = 100
    boss_hp = 103
    boss_damage = 9
    boss_armor = 2

    while True:
        dmg = max(1, player_damage - boss_armor)
        boss_hp -= dmg
        if boss_hp <= 0:
            return True
        dmg = max(1, boss_damage - player_armor)
        player_hp -= dmg
        if player_hp <= 0:
            return False

def inventories():
    inv = [0, None, None, None]
    yield tuple(inv)
    while True:
        inv[3] = 0 if inv[3] is None else inv[3]+1
        if inv[3] >= len(rings):
            inv[3] = None
            inv[2] = 0 if inv[2] is None else inv[2]+1
            if inv[2] >= len(rings):
                inv[2] = None
                inv[1] = 0 if inv[1] is None else inv[1]+1
                if inv[1] >= len(armors):
                    inv[1] = None
                    inv[0] = 0 if inv[0] is None else inv[0]+1
                    if inv[0] >= len(weapons):
                        break
        if inv[2] is None or inv[3] is None or inv[2] != inv[3]:
            yield tuple(inv)


lowest_cost_to_win = 99999
highest_cost_to_lose = 0

for inv in inventories():
    cost, damage, armor = equipment_total(inv)
    if fight(damage, armor):
        lowest_cost_to_win = min(lowest_cost_to_win, cost)
    else:
        highest_cost_to_lose = max(highest_cost_to_lose, cost)

print(lowest_cost_to_win)
print(highest_cost_to_lose)
