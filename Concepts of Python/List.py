# LIST : are enclosed in square brackets '[]' and 
l = [3,4,5,"PARAS",True] 
print(type(l))
print(l)

# Positive Indexing :
print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

# Negative Indexing : if [-x] = [len(l) - x] :
print(l[-3])
print(l[len(l) - 3])
print(l[2])

# To find that element exist in a list or not :
if 7 in l:
    print("Yes")
else:
    print("No")

if "PARAS" in l:
    print("Yes")
else:
    print("No")

if "5" in l: # Here, 5 is searched as a string but in list it is present as a integer;
    print("Yes")
else:
    print("No")

# Finding a part of string exist in a string or not :
if "ARA" in "PARAS":
    print("Yes")
else:
    print("No")

# Range Index :
print(l)
print(l[:])
print(l[1:-1])

# List Slicing : [initial:final:step], step = jump (same concept like string slicing)
print(l[1:4:2])

list1 = [2,3,"Red",'S',90,[8,9,90,"PARAS"],"blue",True]
print(list1)
print(list1[::2])

# List Comprehention :
list2 = [i for i in range(4)]
print(list2)

list2 = [i*i for i in range(10) if i%2 == 0]
print(list2)

# List Methods/Operations :
# 1.] append() : it adds the element in the end of the list;
lst = [11,10,78,87,1,2,3]
lst.append(7)
print(lst)

# 2.] sort() : it sort the list in the accending order, for decending we use (reverse = True); 
# Accending order :
lst.sort()
print(lst)

# Decending order :
lst.sort(reverse = True)
print(lst)

# 3.] reverse() : it reverse the order of the list;
list = [1,4,6,7,2,3]
list.reverse()
print(list)

# 4.] index(x) : gives the index value of the element (x) present on the list, if element isn't present it gives an error;
print(list.index(6))

# 5.] insert(x,y) : Inserts an element (y) in a list at (x) index position;
lst.insert(1,899) # Here, 899 is inserted at 2nd position and at 1st index position;
print(lst)

