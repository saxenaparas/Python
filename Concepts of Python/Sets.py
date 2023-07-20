# Agar aap chate ho ki repeated entries na aa paye;
'''
Sets :
---------------------------------------------------------------------------------------------------------------------------------------
 >> Sets are type of a list but, sets don't maintain the order and repeated values aren't considered;
    i.e. if you print a set repeated values are ignored and sequence of input is not same as output as any elemnet can come at any position;
 >> Syntax : s = {val1,val2,...}
 >> To create an empty set [s = set()] since, [s = {}] is considered as a dictionary as both have syntax is same having curly braces; 
---------------------------------------------------------------------------------------------------------------------------------------
'''

set1 = {1, 2, 2, 1, 8, 7, 6, 3, 3, 4, 0, 7, 5, 4, 9, 8}
print(set1)  # As, you can see we have put the values in different order but we get output in different order this shows sets are unordered;
print(type(set1))

set2 = {"Rahul", "Priya", True, False, None, 1, 2, 8.98, 0.99, 'C'}
print(set2) # Output is unordered;

set3 = {} # Empty dictionary;
set4 = set() # Empty set;
print(type(set3),type(set4))

print("Accesing-using-for-loop--------------")
for value in set2:
    print(value)

# Sets Methods :
s1 = {1,2,3,5,7}
s2 = {3,6,7,4}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2) # Here, [s1] also gets values of [s2] which isn't present in [s1];
print(s1,s2)

print("------------")
s3 = {3,8,7,5,9,90,87,67,56}
s4 = {7,8,3,1,2,0,89,92,99}
s3.intersection_update(s4) # updates the intersection value in [s4];
print(s4)

s5 = {1,2,3,4,5}
s6 = {0,9,8,7,6}
print(s5.isdisjoint(s6)) # chks weather the two sets have completly different values or not;

s7 = {1,2,3,4,5,6,7,8,9,0}
s8 = {1,2,3}
s9 = {1,2,3,99}
print(s7.issuperset(s8)) # It chks like [s7] is superset of [s8];
print(s7.issuperset(s9))
print(s9.issuperset(s8))

'''
Simimlarly, we have [.issubset()];
'''

s8.add("Tokyo")
print(s8)

'''
Similarly, we have [.remove()] & [.discard()] it removes that element;
If we try to [.remove()] for an item not present then it gives an error;
Whereas, [.discard()] willn't;
'''

'''
[.pop()] : 
This method removes the last item of the set but don't know which item gets popped as sets are unordered;
However, you can access the popped item if you assign the pop() method to a variable;
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

'''
[del] : 
del is not a method, rather it is a keyword which deletes the set entirely.
'''
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities) # It will give an error as cities doesn't exit;

'''
[Check if item exists] : 
You can also check if an item exists in the set or not.
'''
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")