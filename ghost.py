# Cades ghost game, created by python_games and DK community
#Just paste this into a python IDLE window, and tweak if you are professinal!
from random import randint
from time import sleep

print("Cades ghost game!")
feelingbrave = True
score = 0
while feelingbrave:
    ghostdoor = randint(1, 3)
    print("Three doors are ahead...")
    sleep(1)
    print("One has a ghost in it!!!")
    sleep(0.5)
    print("You have to open one, which one?")
    door = input('1, 2, or 3?')
    doornum = int(door)
    if doornum == ghostdoor:
        print("GHOST!!!")
        feelingbrave = False
    else:
        print("No ghost")
        sleep(0.5)
        print("Go to next level!")
        score = score + 1
print("You ran away!")
sleep(1)
print('Game over! you scored', score, "!")
