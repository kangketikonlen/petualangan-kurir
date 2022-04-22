import time, random
from utils.print_util import fprint


class Battle(object):
    def __init__(self):
        self.jutsu = [
            "Kamehameha",
            "Rasengan",
            "Cepirit",
            "Balaraja",
            "Chidori",
            "Muka Lucu",
            "Boker",
            "DeezNutz",
            "Ketawa terbahak bahak",
        ]

    def enemy_attack(self, player, enemy):
        # Show attack info
        enemy_damage = random.randint(20, 30)
        enemy_jutsu = random.choice(self.jutsu)
        print(f"\n{enemy.name} melempar {enemy_jutsu.lower()} padamu")
        print(f"Kamu kehilangan {enemy_damage} HP.")
        time.sleep(2)
        # Show player health info
        player.reduce_health(enemy_damage)
        print(f"Sisa HP mu {player.health}")
        time.sleep(2)

    def player_attack(self, enemy):
        # Show attack info
        player_damage = random.randint(1, 100)
        player_jutsu = random.choice(self.jutsu)
        print(f"\nKamu membalas lempar {player_jutsu.lower()}.")
        print(f"{enemy.name} tersebut kehilangan {player_damage} HP.")
        time.sleep(2)
        # Show player health info
        enemy.reduce_health(player_damage)
        print(f"Sisa HP {enemy.name} tersebut {enemy.health}")
        time.sleep(2)
