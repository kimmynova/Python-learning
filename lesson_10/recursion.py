def add_one(num):
    
    if (num >= 9):
        return num +1
    total= num + 1
    print(total)

    return add_one(total)
    # add_one(total) #!because no return keyword the last number gonna turn to [None]

# add_one(0) #!
myNew_valueTotal = add_one(0)
print(myNew_valueTotal)

    