# num = {0,1,2,3,4}

# num2 = set((1,2,3,4))

# print (num)
# print (num2)
# print (type(num))
# print (type(num2))
# print (len(num))

# #?No duplicates
# num = {1,2,3,4}
# print (num)

#?true is duplicate of 1 ,false is duplicate of zero
num = {1,True,2,False,3,4,0}
print (num)
#?check if value is a set
print (2 in num)
#! but you cannot refer to an element in the set with an index position or akey

#?Add a new element to set
num.add(9)
print (num)
#?add a new element to set to other
moreNum ={5,7,6}
num.update(moreNum)
print(num)
#! you can use update with lists,tuple,dictionary

#?merge two set to create a new set
one ={1,2,3}
two ={5,6,7}

mynewSet = one.union(two)
print("merge is",mynewSet)

#? keep only duplicate
one ={1,2,3}
two ={2,3,4}

one.intersection_update(two)
print("duplicate",one)


#? keep everything except the duplicate
one ={1,2,3}
two ={2,3,4}

one.symmetric_difference_update(two)
print("No duplicate and keep everything",one)