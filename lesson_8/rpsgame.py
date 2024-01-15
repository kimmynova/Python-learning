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
    
play_again = True

while play_again:

   
    play_chooser = input("\nEnter....\n1 for Rock,\n2 or paper,\n3 or scricsor:\n\n")
    players =int(play_chooser)

    if players < 1 or players > 3:
        sys.exit("player must be input 1,2,3")
    computer_random = random.choice("123")
    computer = int(computer_random)

      # print("Your chose " +str(RPS(players)).replace('RPS.','') )
    # print("Your computer chose " +str(RPS(computer)).replace('RPS.',''))
    # print ("")
    print ("\nYour chose "+ play_chooser+".")
    print ("Your computer chose "+ computer_random+".\n")
    
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
        
    play_again = input("\nplay again? \nY for yes or \n Q for no \n\n")
    if (play_again.lower()== "y"):
        continue
    else:
        print("\n🎉💃🎉💃")
        print("Thanks for playing!\n")
        #break
        play_again = False
    sys.exit("Bye!👋")