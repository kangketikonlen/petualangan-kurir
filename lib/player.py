import sys
from utils.print_util import fprint, sprint


class Player(object):
    def __init__(self):
        self.location = ""
        self.health = 100
        self.items = []

    def increase_health(self):
        self.health = 100

    def reduce_health(self, value):
        self.health -= value

    def add_item(self, value):
        fprint("Di tengah jalan, kamu menemukan cendol dawet!", 1)
        sprint("Ketik '1' untuk meminum cendol dawet!", 1)
        self.items.append(value)

    def use_item(self, value):
        if value in self.items:
            self.items.remove(value)
            print(f"Kamu menggunakan {value}")
        print(f"Tidak ada item {value} di inventori")

    def die(self):
        fprint("Kamu tidak sadarkan diri!")
        print("GAME OVER")
        sys.exit()
