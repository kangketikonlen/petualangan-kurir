from utils.print_util import sprint, fprint, reset_console
from stories import police_story, thief_story


def main(player):
    print(f"Health: {player.health}")
    fprint("Kamu ngambil beberapa paket, dan memulai untuk mengantar paket pertama mu.")
    print("Di jalan, kamu liat ada polisi sedang razia. Apakah kamu mau melewatinya?")
    while True:
        action = input("\n> ")
        if action == "ya":
            fprint("-- LOADING --", 1)
            police_story.main(player)
        elif action == "tidak":
            fprint("-- LOADING --", 1)
            thief_story.main(player)
        else:
            sprint("Mobil di belakang ngelakson. Jangan hambat arus lalu lintas!")
