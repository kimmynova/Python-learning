#closer is function having access to the scope of its parent scope
#function after the parent function has returned
#
#
print ("")
print ("First method")
def parent_func(person):
    coin = 3
    def play_game():
        nonlocal coin
        coin -= 1
        if coin > 1:
            print ("\n"+person +" has " +str(coin)+" coin left.")
        elif coin == 1:
            print ("\n"+person+" has " +str(coin) +" coin left.")
        else:
            print ("\n" + person +" is out of coin.")
    return play_game #!I make mistakes [return play_game()]
kim = parent_func("kim")
Nova = parent_func("Nova")
kim()
kim()
kim()
Nova()

print ("")
print ("Second method")
def parent_func(person,coin):
    def play_game():
        nonlocal coin
        coin -= 1
        if coin > 1:
            print ("\n"+person +" has " +str(coin)+" coin left.")
        elif coin == 1:
            print ("\n"+person+" has " +str(coin) +" coin left.")
        else:
            print ("\n" + person +" is out of coin.")
    return play_game #!I make mistakes [return play_game()]
kim = parent_func("kim",5)
Nova = parent_func("Nova",6)
kim()
kim()
kim()
Nova()