users = ['kim','nova','kimmy']

data = ['kim',24,True]

empty_list =[]

print("kim" in empty_list)
print(users[0])
print(users[-1])
print(users.index('nova'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])
print(len(data))

users.append('leng')
print(users)

users += ['jason'] #!make have braket
print(users)

users.extend(['Robert','jimmy'])
print(users)
# users.extend(data)
# print(users)
users.insert(0,'Alex') #?add in first value
print(users)
users[2:2] =['Alex','eddie']
print(users)
users[1:3]=['Bob','jp']
print(users)

users.remove('Bob')
print(users)
print(users.pop())
print(users)

del users[0]
print(users)

# del data #!errors
data.clear()
print(data)
users[1:2] =['kimleng']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums =[4,42,78,1,5,6]
nums.reverse()
print(nums)
nums.sort(reverse=True)
print(nums)

print(sorted(nums,reverse=True))
print(nums)


nums_copy = nums.copy() #!create a copy of list
mynum =list(nums)
nums_copy = nums[:]

print(nums_copy)
print(mynum)
nums_copy.sort()
print(nums_copy)
print(nums)

print(type(nums))
mylist= list([1,'Elysia',True])
print(mylist)

