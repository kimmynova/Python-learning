#The difference list and tuples such us: 
#list can change values
#Tuples cannot change values

mytuples = tuple(('kim',24,True))

another_tuples =(1,4,8,9)

print (mytuples)
print (type(mytuples))
print (type(another_tuples))


newlistCostructer = list(mytuples)

newlistCostructer.append('Neli')
newtuple =tuple(newlistCostructer)
print (newtuple)

#?unpackage tuples
(one,*two, hey) =another_tuples
print (one)
print (two)
print (hey)
print(another_tuples.count(4)) #!count list
