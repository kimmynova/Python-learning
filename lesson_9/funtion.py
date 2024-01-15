# def hello():
#     print ("Hello World")
# hello()

# def sum(n1,n2):
#     print (n1+n2)    
# sum(3,4)
# sum(3,5)
# sum(3,100)

# def sum(n1,n2):
#     if(type(n1) is not int or type(n2) is not int):
#         return  #! it call early return
#     return n1+n2
# # total = sum( "A" , 5)
# total = sum(9 , 5)
# print (total)


# def sum(n1=0,n2=0):
#     if(type(n1) is not int or type(n2) is not int):
#         return 0  #! it call early return
#     return n1+n2
# # total = sum( "A" , 5)
# total = sum(7,6)
# print (total)


def multiple_items(*args):
    print (args)
    print(type(args))
    
multiple_items('kim','kimmy','nova')


def multiple_name_items(**kwargs):
    print (kwargs)
    print(type(kwargs))
multiple_name_items(frist='kim',last="leng")
    
    