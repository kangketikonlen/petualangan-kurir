import random
from lib.battle import Battle
from lib.enemy import Enemy
from utils.print_util import sprint, fprint, reset_console
from stories import destination_story

battle = Battle()
enemy = Enemy("Begal")


def main(player):
    enemy_attack = random.choice([True, False])
    item_find = random.choice([True, False])
    #
    print(f"Health: {player.health}")
    #
    if item_find == True:
        player.add_item("medkit")
    #
    fprint("Di jalan yang sepi, kamu merasa ada motor yang selalu mengikuti.")
    sprint("Ingin mengambil jalan yang lebih ramai?")
    while True:
        action = input("\n> ")
        if action == "ya":
            destination_story.main(player)
        elif action == "tidak":
            if enemy_attack == True:
                fprint("Firasatmu benar, motor tersebut mengikutimu.", 2)
                sprint("Pengendara tersebut mengacungkan senjata tajam")
                sprint("Kamu pun berhenti dan pertarungan dimulai.", 2)
                while enemy.health > 0:
                    battle.enemy_attack(player, enemy)
                    if player.health <= 0:
                        player.die()
                    #
                    battle.player_attack(enemy)
                    if enemy.health < 0:
                        enemy_attack = False
                        break
                print(f"\nKamu berhasil membunuh {enemy.name} tersbut.")
            sprint("Perjalanan pun dilanjutkan.", 2)
            sprint("Apakah kamu ingin menuju lokasi selanjutnya?", 2)
        elif action == "1":
            player.use_item("medkit")
            player.increase_health()
        else:
            fprint("Hari sudah mulai gelap, paket harus segera dikirim!.")
