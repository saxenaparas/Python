'''
Dictionary : is used to store key value pairs;
'''

dic1 = {
    "Paras": "GOD OF GOLD",
    "Saxena": "KAYASTH"
}
print(dic1["Paras"])
print(dic1["Saxena"])

dic2 = {
    108 : "NARAYAN",
    7 : "BHRAMA",
    3 : "SHIV",
}
print(dic2[108])
print(dic2[7])
print(dic2[3])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info["name"]) 
# print(info["name2"]) # You use it if you want to through an error for non-existing key;
print(info.get("name"))
print(info.get("name2"))

# For accessing multiple values :
print(info.values())
# For accessing multiple keys only :
print(info.keys())
# For accessing key-value pairs: :
print(info.items())

for key in info.keys():
    print(info[key])

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")

for key, values in info.items():
    print(f"The value corresponding to the key {key} is {values}")

'''
# Dictionary Methods : 
 > update
 > clear
 > popitem
 > del
'''
# Dictionary Methods :
# 1.] [.update()] ->
ep1 = {"Paras":1000, "Rohan":100, "Yiuo":198, "James":34}
ep2 = {"Lio":98, "Kio":78, "Li":87, "Zio":74}
ep1.update(ep2) # Update [ep1] with [ep2]; 
print(ep1)
ep1.update({"Hio":88})
print(ep1)

# 2.] [.clear()] -> Clear all the items from list and create a empty dictionary;
ep1.clear() 
print(ep1)

# 3.] [.pop()] -> The pop() method removes the key-value pair whose key is passed as a parameter;
ep2.pop("Kio")
print(ep2)

# 4.] [.popitem()] -> The popitem() method removes the last key-value pair from the dictionary.
ep2.popitem()
print(ep2)

# 5.] [del] : -> We can also use the del keyword to remove a dictionary item or delete the whole dictionary;
del ep2["Zio"] # Only the given key value pair got deleted from the dictionary;
print(ep2)
del ep2 # Deletes the whole dictionary and when we try to call it will give an error;
print(ep2)