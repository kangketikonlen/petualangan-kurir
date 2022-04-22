import sys
import os
import time


def print_slow(str, delay=0.1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")


def reset_console():
    os.system("cls||clear")
    print("Petualangan Kurir")
    print("v1.0.0")


def fprint(str, delay=0):
    print("\n" + str)
    time.sleep(delay)


def sprint(str, delay=0):
    print(str)
    time.sleep(delay)
