# value =1
# while value <= 10: #!< =
#     print (value)
#     if value == 5:
#         break
#     value += 1  

# value =1
# while value <= 10: #!< =
#     value += 1  
#     if value == 5:
#         continue
#     print (value)
# else:
#     print ("value is now equal to " + str(value))

name = ['kimleng','nova','kimmynova']
# for x in name:
#     print (x)
    
# for x in "kimleng":
#     print (x)

# for x in name:
#     if x == "nova":
#         break
#     print (x)

# for x in name:
#     if x == "nova":
#         continue
#     print (x)

# for x in range(4): #? start from 0 to 3
#     print (x)

# for x in range(2,4): #? start from 2 to 3
#     print (x)

# for x in range(0,101,5): #? increment by 5  
#     print (x)
# else: 
#     print ("it\'s over!")
#! nesting loop
name = ['kimleng','nova','kimmynova']
actions = ['code','eats','sleep']

# for name in name:
#     for action in actions:
#         print (name+" "+action+".")

for action in actions:
    for names in name:
        print (names+" "+action+".")