import random
import math

def monty_hall(iterations, change_choice):
  won = 0
  lost = 0
  for i in range(0, iterations):
    doors = [1,2,3]
    prize = random.choice(doors)
    choice = random.choice(doors)
    opened = random.choice(list(set(doors) - set([choice, prize])))
    if change_choice:
      choice = random.choice(list(set(doors) - set([opened, choice])))

    if choice == prize:
      won += 1
    else:
      lost += 1
  
  print("Win Percentage: {0}".format(won/iterations))
    

monty_hall(10000, True)
monty_hall(10000, False)



