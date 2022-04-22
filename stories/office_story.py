from utils.print_util import sprint, fprint, reset_console
from stories import road_story


def main(player):
    print(f"Health: {player.health}")
    fprint("Kamu lagi nyantai dan ngobrol bareng temen kerjamu di warung.")
    print("Truk beres loading. Mau mulai nganter paket?")
    while True:
        action = input("\n> ")
        if action == "ya":
            fprint("-- LOADING --", 1)
            road_story.main(player)
        elif action == "tidak":
            sprint("Kamu masih duduk ngabisin kopi.")
        else:
            sprint("Temen kerjamu udah mulai nyiapin paket.")
