#String data

#literals assigment

frist = 'kim'
last= 'leng'
pizza =str('pizza is round')

#?constructer funtion
# print (type(last))
# print ('first name is',type(frist)==str) 
# print ('lastname is',type(last)==int) 
# print ('pizza round is',isinstance(pizza,int)) 

#?concatenatin

fullname = frist + "" + last
print(fullname)

fullname += "!"
print(fullname)

#?casting a number to string
decade = str(2024)
print(type(decade))
print(decade)

statement ="kim love coding in " + decade + 's'

print (statement)

#?multiple line
multiline = '''
I love coding 
                 create something new
                                            and love group                                                        
''' 
print(multiline)


#?Escaping specail characters

setense = 'I \'m back at work\tHey!\n\n where \'s this coming from\\located'
print(setense)

#?string Methold

print(frist)
print(frist+last.lower())
print(frist.upper())

print(multiline.title())

print(multiline.replace("and love group","Ok dude")) #!replace with key and change value

print(len(multiline))

multiline +="        "
multiline = "              "+ multiline
print('Total lenght',len(multiline))

#?remove speace

print('remove space',len(multiline.strip()))
print('Right lenght',len(multiline.rstrip()))
print('left lenght',len(multiline.lstrip()))


#!build menu
title= 'menu'.upper()
print(title.center(20,"="))
print("coffee".ljust(16,".")+ "$1".rjust((4)))
print("milk tea".ljust(16,".")+ "$2".rjust((4)))
print("friut tea".ljust(16,".")+ "$5".rjust((4)))
print("machiato".ljust(16,".")+ "$6".rjust((4)))
print("=".ljust(20,"="))

#string index value
#!note: python start index from zero 
print("count kim name index = ",frist[1])
print("count kim name index = ",frist[-1])
print("count kim name index = ",frist[1:-1])
print("count kim name index = ",frist[1:])

#?some methods return boolean values
print("My frist start",frist.startswith("k"))
print("My frist start",frist.endswith("i"))
print("")
#?boolean methods datatype 
myvalue = True
x = bool(False)
print("My value",type(x))
print(isinstance,myvalue,bool)

#?numberies datatype
price = 100
bestprice =int(80)

#?integer types
print(type(price))
print(isinstance(price,int))
#?float types
gpa=3.85
y=float(1.14)

print(type(gpa))
print(isinstance(y,float))

#?complex types

com_values = 5+3.j

print(type(com_values))
print(com_values.real)
print(com_values.imag)

#! Built-in funtion for number
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa,1))

import math

print("pi is",math.pi)
print("sqartur",math.sqrt(64))
print("ceil",math.ceil(gpa))
print("mathFloor is",math.floor(gpa))

#!casting string  to number
zipcode = "1001"
zip_value =int(zipcode)
print(type(zip_value))

#!!error if u atempted to cast innorect data
#! zip_value = int("cambodia")