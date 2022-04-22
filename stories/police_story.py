import sys
from utils.print_util import sprint, fprint, reset_console


def main(player):
    print(f"Health: {player.health}")
    fprint("Opps, kamu kena tilang... Sialnya kamu lupa membawa dompet.")
    print("Apakah kamu ingin mencoba memohon kepada polisi?")
    while True:
        action = input("\n> ")
        if action == "ya":
            sprint("Kamu mencoba untuk memohon kepada polisi, namun gagal.", 2)
            sprint("Motormu pun disita, dan harus mengikuti sidang.", 2)
            sprint("Paket di alihkan ke kurir lain.", 2)
            print("GAME OVER")
            sys.exit()
        elif action == "tidak":
            sprint("Motormu pun disita, dan harus mengikuti sidang.", 2)
            sprint("Paket di alihkan ke kurir lain.", 2)
            print("GAME OVER")
            sys.exit()
        else:
            sprint("Polisi terlanjur memberimu surat tilang.", 2)
            sprint("Motormu pun disita.", 2)
            sprint("Paket di alihkan ke kurir lain.", 2)
            print("GAME OVER")
            sys.exit()
