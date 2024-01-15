#?rps
# value=input('Enter your value: \n')

# print ('Your value',value)
import sys
import random
from enum import Enum

class RPS(Enum):
    rock = 1
    papper = 2
    scisor = 3
# print(RPS(2))
# print(RPS.rock)1
# print(RPS['rock'])
# print(RPS.rock.value)
# sys.exit()
print("")
playchoser = input("Enter....\n1 for Rock,\n2 or paper,\n3 or scricsor:\n\n")
players =int(playchoser)

if players < 1 or players > 3:
    sys.exit("player must be input 1,2,3")
computer_random = random.choice("123")
computer = int(computer_random)

print ("")
# print("Your chose " +playchoser + ".")
# print("Your computer chose " + computer_random + ".")

print("Your chose " +str(RPS(players)).replace('RPS.','') )
print("Your computer chose " +str(RPS(computer)).replace('RPS.',''))
print ("")

if players == 1 and computer == 3:
    print("You Win!😎")
elif players == 2 and computer == 1:
    print("You Win!😜")

elif players == 3 and computer == 1:
    print("You Win!😜")
elif players == computer:
    print("Is a Tie! No one wins!😎")
else :
    print("You Lose!🤣")