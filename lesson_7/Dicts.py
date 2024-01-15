#dictionary
band ={
    "vocal": "plant",
    "guitar": "page"
}

band2= dict(vocals="plant",guitar = "page")
# print (band)
# print (band2)
# print (type(band2))
# print (len(band2))

#?Access items
print(band["vocal"])
print(band.get("guitar"))

#?list items
print(band.keys())

#?list all value
print(band.values())

#?list pair key/value as tuple
print(band.items())

#? verify key of existing value 
#!(boolean)
print("guitar" in band)
print("triangle of"in band)

#?change value
band["vocal"] = "coverdale"
band.update({"bass":"jp"})
print(band)

#?remove item
print(band.pop("bass"))
print(band)


band["drum"] ="kimdrum" #! [key] and value
print(band)
print(band.popitem()) #? tuple
print(band)

#?delete and clear item

band["drum"] ="kimdrum"
del band["drum"]
print(band)
band2.clear()
print(band2)

del band2 #! delete all


#?copy dictionary
 #! the same dictionary in memoryview
band2 = band #?create reference
# print("bad copy")
# print(band2)
# print(band)

# band2["drum"] ="kimmy"
# print(band)

print("good copy")
band2 = band.copy()
band2["drum"] ="kimmy"
print(band)
print(band2)
#? or use the dict() constructor function

band3 = dict(band)
print("good copy!")
print(band3)

#?nested dictionary
print("nested dictionary")
member1 = {
    "name":"plant",
    "instruments":"vocal"
}
member2 = {
    "name":"vocal",
    "instruments":"guitar"
}

band ={
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])
