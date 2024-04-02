from random import randint
from time import sleep
from pyfiglet import Figlet
from termcolor import colored

f = Figlet(font='slant')
print(f.renderText('Ghost_Game'))
print("Welcome to Ghost Game!")
feelingbrave = True
score = 0

while feelingbrave:
    ghostdoor = randint(1, 3)
    print("Three doors are ahead...")
    sleep(1)
    print("One has a ghost in it!!!")
    sleep(0.5)
    print("You have to open one, which one?")
    door = input('1, 2, or 3? ')
    doornum = int(door)

    if doornum == ghostdoor:
        print(colored("GHOST!!!", 'red'))
        feelingbrave = False
    else:
        print("No ghost")
        sleep(0.5)
        print(colored("Go to the next level!", 'green'))
        score += 1

print("You ran away!")
sleep(1)
print('Game over! You scored', score, "!")
print('Made by Ro706')
