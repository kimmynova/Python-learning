person ="kim"
coins=3

print("\n"+person +" has "+ str(coins )+" coins left")

#!new way
message="\n%s has %s coins left"%(person,coins)
print(message)
#!second way
message="\n{} has {} coins left".format(person,coins)
print(message)

message="\n{1} has {0} coins left".format(coins,person)  #!index
print(message)

message="\n{person} has {coins} coins left.".format(
        coins=coins,person=person
)  #!call with variable
print(message)

#!dictionary
items={'person':'not kim','coins':3}
message="\n{person} has {coins} coins left.".format( **items
) 
print(message)



#? f-strings

message=f"\n{person} has {coins} coins left."
print(message)

message=f"\n{person} has {3*5} coins left."
print(message)

message=f"\n{person.lower()} has {3*5} coins left."
print(message)

message=f"\n{items['person']} has {3*8} coins left."
print(message)

#?You can pass formatting options
num =12
print(f"\n 2.25 times {num} is {2.25 *num:.2f}")


for num in range(1,11):
    print(f"\n 2 times {num} is {2 * num:.2f}")
    
for num in range(1,11):
    print(f"{num}divided by 4.52  is {num/ 4.52:.2%}")