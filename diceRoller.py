#Coin flip program
#Describe the purpose of this program here.

import random,time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def roll():
    print("rolling.....")
    global DiceRoll
    DiceRoll = random.randint(1,6)


def show_dice():
    if DiceRoll == 1:
        print(s1)
    elif DiceRoll == 2:
        print(s2)
    elif DiceRoll == 3:
        print(s3)
    elif DiceRoll == 4:
        print(s4)
    elif DiceRoll == 5:
        print(s5)
    elif DiceRoll == 6:
        print(s6)
        
        

while DiceRoll !=6:
    input(":")
    roll()
    time.sleep(1)
    show_dice()
