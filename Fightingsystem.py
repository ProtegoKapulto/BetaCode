import random
import time
from MusikBoy import *
import pygame

player_health = 100
monster_hp = 20
player_mana = 10
frozen = 0
fire = 0
monster = "Placeholder"
pronouns = "He"
pygame.init()
pygame.mixer.init()
mana_absorption_shield = False


def fight_start():
    if monster == "Monika":
        print(animated_text(f"{monster} is challenging you to a fight!!!"))
        player_turn()
    else:
        regular_fight_sound()
        print(animated_text(f"{monster} is challenging you to a fight!!!"))
        player_turn()


def player_turn():
    global monster_hp
    global damage
    fight_answer = input(animated_text(f"""
    What do you want to do?
        Sword
        Magic
        Absorbing Mana Shield
        Run

        You have {player_health} HP and {player_mana} Mana

        """))
    if fight_answer.lower() == "sword" or fight_answer.lower() == "s":
        damage = sword_hit()
        sword_sound()
        monster_health()
    elif fight_answer.lower() == "magic" or fight_answer.lower() == "m":
        magic()
    elif fight_answer.lower() == "absorbing mana shield" or fight_answer.lower() == "a" or fight_answer.lower() == "shield":
        shield()
    elif fight_answer.lower() == "run" or fight_answer.lower() == "r":
        run = random.choice([1, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        if run == 1:
            return True  # Escaped Funktion dafür mache ich im Verlauf des Spiels

        else:
            damage = 0
            print("You tried to run away but failed!!!")
            monster_attack()
    else:
        nochmal()


def nochmal():
    player_turn()


def monster_attack():
    global player_damage
    global frozen
    attack = random.choice([1, 1, 1, 1, 2, 2, 2, 3])
    if frozen > 0:
        frozen_effect()
    else:
        if attack == 1:
            player_damage = random.choice(
                [10, 11, 12, 13, 14, 10, 11, 12, 13, 14, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
            print(animated_text(f"{monster} uses Tail Whip!!!"))
            player()
        elif attack == 2:
            player_damage = random.choice([15, 16, 17])
            print(animated_text(f"{monster} uses Shadow Strike!!!"))
            player()
        elif attack == 3:
            player_damage = random.choice([18, 19, 20])
            print(animated_text(f"{monster} uses Thunder Spear!!!"))
            player()


def change_monster(new_name):
    global monster
    monster = new_name


def monster_health():
    global monster_hp
    monster_hp -= damage
    if fire > 0:
        print(animated_text(f"You´ve dealt {monster} {damage} damage and the fire made him loose 3 HP!!!"))
        monster_hp -= 3
    else:
        print(animated_text(f"You´ve dealt {monster} {damage} damage!!!"))
    if monster_hp <= 0:
        print(animated_text(f"""{monster} Health dropped to zero.
You Win!!!"""))  # man könnte da maybe Spielername einfügen
    else:
        if monster == "Monika":
            print(animated_text(f"{monster} has {monster_hp} HP"))
            monika_attack()

        else:
            print(animated_text(f"{monster} has {monster_hp} HP"))
            monster_attack()


def monika():
    global monster_hp
    global pronouns
    pronouns = "She"
    monster_hp = 40
    change_monster("Monika")
    egg_sound()
    fight_start()


def monika_attack():
    global player_damage
    frozen_effect()
    player_damage = random.choice([20, 20, 20, 50, 50, 100])
    print(animated_text(
        "J̷̝͉͍̜̿̂̏̅̍͐̃͆̚͠u̶̹̪͈̭̽̈̄̑͑̇̂͜͝͝s̸̢̥͓̺͚̝͖͓̟͗̾̍͑̍̇̀̐̎t̸͕̭͆̏ ̶̨͖̣̌̄̈̀̂M̴͙͙̘̲͚̲̑̾̋͘ͅo̵̥͓̓́̔͂͠n̶̡͓̰̘̣̮͎̙̣̈̂͋̚͠͠ͅi̷̛̘̬̙̭̲͉̙͊͌́̋͛̏̏̎̕k̴̲͚̼̯̩̩͙̀͊̐̌ȁ̶̹̹̻̞̅̽̽̂̿͝͝"))
    player()


def player():
    global player_health
    global player_damage
    global player_mana
    global mana_absorption_shield
    if mana_absorption_shield == True:
        shield_sound()
        print(animated_text(
            f"{monster} tried to attack you, but due to your Absorbing Mana Shield, the damage was reduced and you refilled your Mana!!! "))
        player_damage -= 11
        player_health -= player_damage
        if player_damage > 0:
            print(animated_text(f"{monster} gave you {player_damage} damage"))
            player_mana = 10
            mana_absorption_shield = False

        elif player_damage == 0:
            print(animated_text(f"You blocked {monster} attack!!!"))
            player_mana = 10
            mana_absorption_shield = False

        elif player_damage < 0:
            print(animated_text(f"Wow you blocked {monster} attack and regained 1 HP!! How is this even possible???"))
            player_mana = 10
            mana_absorption_shield = False

    else:
        print(animated_text(f"{monster} gave you {player_damage} damage"))
        player_health -= player_damage
    if player_health <= 0:

        game_over()
    # Hier Game Over Funktion
    else:
        player_turn()


def game_over():
    print("Your HP dropped to Zero... You failed us all!!! ")
    game_over_sound()
    exit()


def animated_text(text):  # Animation von ChatGPT erstellt
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.01)  # Zeit für nächsten Buchstaben hier konfigurierbar
    return ("")


def sword_hit():
    return random.choice([1, 2, 3, 4, 5, 6])


def shield():
    global mana_absorption_shield
    mana_absorption_shield = True
    monster_attack()


def fire_magic():
    global damage
    global fire
    damage = random.choice([3, 4, 5])
    fire = random.choice([1, 1, 2, 2, 2, 2, 2, 3])
    print(animated_text(f"You made {monster} go up in Flames!!!"))
    fireball_sound()
    monster_health()


def ice_magic():
    global frozen
    global damage
    global IceMagic
    damage = random.choice([2, 3])
    frozen = 2
    monster_health()


def frozen_effect():
    global frozen
    if frozen == 1:
        print(animated_text(f"{monster} was frozen!!! {pronouns} won´t be able to attack this round!!! "))
        frozen -= 1
        player_turn()
    elif frozen == 2:
        ice_sound()
        print(animated_text(f"{monster} was frozen!!! {pronouns} won´t be able to attack for {frozen} rounds!!! "))
        frozen -= 1
        player_turn()


def shadow_magic():
    return random.choice([4, 5, 6])


def light_magic():
    return random.choice([5, 6])


def magic():
    global damage
    global player_mana
    magicAnswer = input(animated_text("""Which Magic do you want to use?
    Fire Magic (4 Mana)
    Ice Magic (4 Mana)
    Shadow Magic (6 Mana)
    Light Magic (7 Mana)

    back
    """))
    if magicAnswer.lower() == "fire magic" or magicAnswer.lower() == "f":  # Brauche zwei unterschiedliche Fälle für einmal kein Mana und einmal falsche Eingabe
        if player_mana >= 4:
            player_mana -= 4
            damage = fire_magic()
        else:
            print(animated_text("Not enough Mana for Fire Magic"))
            magic_return()

    elif (magicAnswer.lower() == "ice magic" or magicAnswer.lower() == "i"):
        if player_mana >= 4:
            player_mana -= 4
            ice_magic()
        else:
            print(animated_text("Not enough Mana for Ice Magic"))
            magic_return()

    elif magicAnswer.lower() == "shadow magic" or magicAnswer.lower() == "s":
        if player_mana >= 6:
            player_mana -= 6
            damage = shadow_magic()
            monster_health()
        else:
            print(animated_text("Not enough Mana for Shadow Magic"))
            magic_return()
    elif magicAnswer.lower() == "light magic" or magicAnswer.lower() == "l":
        if player_mana >= 7:
            player_mana -= 7
            damage = light_magic()
            monster_health()
        else:
            print(animated_text("Not enough Mana for Light Magic"))
            magic_return()
    else:

        player_turn()


stop_event = False


def magic_return():
    magic()
