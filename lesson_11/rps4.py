import sys
import random
from enum import Enum
#! global scope
game_count = 0

def play_rps(): #?create new function
    
    class RPS(Enum):
        rock = 1
        paper = 2
        scissor = 3
        
   
    play_chooser = input("\nEnter....\n1 for Rock,\n2 or paper,\n3 or scissor:\n\n")
    players =int(play_chooser)
    
    if players not in [1,2,3]:
        print("Please select 1,2 or 3")
        return play_rps()
        
   
    computer_random = random.choice("123")
    computer = int(computer_random)

    print("Your chose " +str(RPS(players)).replace('RPS.','') )
    print("Your computer chose " +str(RPS(computer)).replace('RPS.','').title()+".\n")
    def decide_winner(players,computer): #!nested scope function
        if players == 1 and computer == 3:
            return "You Win!😎"
        elif players == 2 and computer == 1:
            return "You Win!😜"
        elif players == 3 and computer == 1:
            return "You Win!😜"
        elif players == computer:
            return "Is a Tie! No one wins!😎"
        else :
            return "You Lose!🤣"
    gameResult = decide_winner(players,computer)
    print(gameResult)
    global game_count#!here the store in global
    game_count +=1
    print("\nGame Count: "+ str(game_count))
           
    print("\nplay again?")    
    while True:
        play_again = input("\nplay again? \ny for yes or \nq for no \n")
        if play_again.lower() not in ["y", "q"]:
            continue
        else:
            break

    if play_again.lower() == "y":
        return play_rps()  #!Recursion function
    else:
        print("\n🎉💃🎉💃")
        print("Thanks for playing!\n")
        print("Bye!👋")
        sys.exit()     
play_rps()