import sys, random
from lib.battle import Battle
from lib.enemy import Enemy
from utils.print_util import sprint, fprint, reset_console

battle = Battle()
enemy = Enemy("Suami Emak2")


def main(player):
    enemy_attack = random.choice([True, False])
    enemy_attack = True
    item_find = random.choice([True, False])
    #
    print(f"Health: {player.health}")
    #
    if item_find == True:
        player.add_item("medkit")
    #
    fprint("Kamu mengambil jalan lain dan sampai di depan rumah penerima.", 2)
    print("Kamu pun berteriak, 'punten paket~' dan ibu - ibu pun keluar dari rumah.")
    print("Apakah kamu ingin menyerahkan paketnya?")
    while True:
        action = input("\n> ")
        if action == "ya":
            fprint("Ibu itu pun membuka paket dan ternyata tidak sesuai.", 2)
            if enemy_attack == True:
                sprint("Sambil bilang 'goblok' Ibu pun memarahi mu.", 2)
                sprint("Suaminya keluar dan kamu pun kena bogem mentah.")
                while enemy.health > 0:
                    battle.enemy_attack(player, enemy)
                    if player.health <= 0:
                        player.die()
                    #
                    battle.player_attack(enemy)
                    if enemy.health < 0:
                        enemy_attack = False
                        break
                print(f"\nKamu berhasil mengalahkan {enemy.name} tersbut.")
            fprint("Dengan kesal, ibu itu pun mengajukan pengembalian barang.", 2)
            print("Semua paket telah dikirim. Hari ini kamu selamat!")
            print("GOOD ENDING")
            sys.exit()
        elif action == "tidak":
            sprint("Ibu itu semakin mendekatimu.")
        elif action == "1":
            player.use_item("medkit")
            player.increase_health()
        else:
            sprint("Kamu dan ibu - ibu itu pun saling bertatap mata.")
