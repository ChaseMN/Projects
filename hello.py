import random
import time


class Lulu:
    blood = 0
    organs = 0

    def __init__(self):
        lives = 3


def sPrint(text, delay):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay / 100)
    print("")


def sInput(text, delay):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(delay / 100)
    print("")
    return input("")


print("")
sPrint("Lulu Simulator 0.w.0\n", 5)
sPrint("Start        Settings        Exit\n", 4)
time.sleep(1.2)
sPrint("...Just kidding, there's not enough content here to warrant a settings menu, and if you want to exit you can just hit the X button\n", 3)
input = sInput("Would you like a tutorial? (Type Y or N)", 4)
if input == 'Y':
    sPrint("Haha very funny, I don't even know what systems are going to be in this game and you want me to make a tutorial?", 3)
print('Gang')