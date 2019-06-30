import random
import math

change_choice = True



def monty_hall(iterations):
    won = 0
    lost = 0
    for i in range(0, iterations):
        car = random.randint(0,3)
        firstChoice = random.randint(0, 3)
        opened = random.randint(0,3)
        while opened == car or opened == firstChoice:
            opened = random.randint(0,3)
        if change_choice:
            tmp = firstChoice
            while firstChoice == tmp or firstChoice == opened:
                firstChoice = random.randint(0, 3)
        if car == firstChoice:
            won += 1
        else:
            lost += 1

    print(won, lost)


monty_hall(10000)

change_choice = False
monty_hall(10000)

