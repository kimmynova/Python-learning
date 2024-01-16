name ="Nova" #? global scope
count =1
def greeting(firstName):
#!local scope
    color ="Neon"
    print (name)  
    print (color)  
    print (firstName)  
    print()
greeting("kimmy")

def another():
    greeting("Ayumi Veda") #!because the (greeting() function) on top also call global scope to other function
another()


#! It call parent scope  (Nested scope function)
def another():
    color ="Blue"
    def greeting(name): 
        print (color)  
        print (name)  
        print()
    greeting("Ayumi Veda") 
another()
# greeting() #!note u cannot call global scope because the function is local scope

print()
def another():
    color ="red"
    # count+=1 #!because don't have value it gonna error
    global count #? but u can use global scope using keyword(global) (╯°□°）╯︵ ┻━┻)
    count +=1 #?
    print(count)

    def greeting(name): 
        nonlocal color #! this one u don't want use global scope inside parent scope
        color = "green" #
        print (color)  
        print (name)  
        print()
    greeting("Ayumi Veda") 
another()
