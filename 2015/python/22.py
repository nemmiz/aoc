#!/usr/bin/python3


def player_turn(player_hp, player_mana, shield_counter, poison_counter, recharge_counter, boss_hp, boss_dmg, mana_spent, best, hard_mode):
    if hard_mode:
        player_hp -= 1
        if player_hp <= 0:
            return

    if mana_spent >= best[0]:
        return

    if shield_counter > 0:
        armor = 7
        shield_counter -= 1
    else:
        armor = 0

    if poison_counter > 0:
        boss_hp -= 3
        poison_counter -= 1

    if recharge_counter > 0:
        player_mana += 101
        recharge_counter -= 1

    if boss_hp <= 0:
        if mana_spent < best[0]:
            best[0] = mana_spent
        return

    if player_mana < 53:
        return

    # Try casting magic missile
    if player_mana >= 53:
        boss_turn(player_hp, player_mana-53, shield_counter, poison_counter, recharge_counter, boss_hp-4, boss_dmg, mana_spent+53, best, hard_mode)

    # Try casting drain
    if player_mana >= 73:
        boss_turn(player_hp+2, player_mana-73, shield_counter, poison_counter, recharge_counter, boss_hp-2, boss_dmg, mana_spent+73, best, hard_mode)
    
    # Try casting shield
    if player_mana >= 113 and shield_counter == 0:
        boss_turn(player_hp, player_mana-113, 6, poison_counter, recharge_counter, boss_hp, boss_dmg, mana_spent+113, best, hard_mode)

    # Try casting poison
    if player_mana >= 173 and poison_counter == 0:
        boss_turn(player_hp, player_mana-173, shield_counter, 6, recharge_counter, boss_hp, boss_dmg, mana_spent+173, best, hard_mode)

    # Try casting recharge
    if player_mana >= 229 and recharge_counter == 0:
        boss_turn(player_hp, player_mana-229, shield_counter, poison_counter, 5, boss_hp, boss_dmg, mana_spent+229, best, hard_mode)


def boss_turn(player_hp, player_mana, shield_counter, poison_counter, recharge_counter, boss_hp, boss_dmg, mana_spent, best, hard_mode):
    if mana_spent >= best[0]:
        return

    if shield_counter > 0:
        armor = 7
        shield_counter -= 1
    else:
        armor = 0

    if poison_counter > 0:
        boss_hp -= 3
        poison_counter -= 1

    if recharge_counter > 0:
        player_mana += 101
        recharge_counter -= 1

    if boss_hp <= 0:
        if mana_spent < best[0]:
            best[0] = mana_spent
        return

    # Attack the player
    dmg = max(1, boss_dmg - armor)
    if dmg >= player_hp:
        return
    else:
        player_turn(player_hp - dmg, player_mana, shield_counter, poison_counter, recharge_counter, boss_hp, boss_dmg, mana_spent, best, hard_mode)


best_ever = [9999999]
player_turn(50, 500, 0, 0, 0, 55, 8, 0, best_ever, hard_mode=False)
print(best_ever[0])

best_ever = [9999999]
player_turn(50, 500, 0, 0, 0, 55, 8, 0, best_ever, hard_mode=True)
print(best_ever[0])
