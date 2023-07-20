# Tuple is just like list but its content can't be changed;
# It's defined as [variable_name = ()];

t1 = (1,2,3,"green",True)
print(type(t1), t1)
# t1[0] = 90 : here, it will give an error since tuple is immutable;

t2 = [1,2,3,"green",True] # here, t2 is a list;
print(type(t2), t2)
t2[0] = 89
print(t2)

print(t1[0])
print(t1[-3])
print(len(t1))
print(len(t2))

if "green" in t1:
    print("Yes (green) is present")

# Tuple indexing, negative indexing, slicing & all functions are same as list accept its immutable so contents can't be changed;
# If you want to perform any operations then first copy it into other varaible by typecasting it in list form then perform operations on it and again typecaste it into a tuple;
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)      #typecasted as list;
temp.append("Russia")       #add item;
temp.pop(3)                 #remove item;
temp[2] = "Finland"         #change item;
countries = tuple(temp)     #typecasted as tuple;
print(countries)

# We can directly concatenate two tuples without converting them to list.
countries = ("Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

# It supports same methods as a list :
# count() & index() methods;
# index() syntax :-> tuple.index(element, start, end);
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3,4,8)    #(element, start, end);
print('First occurrence of 3 from index 4 to 3 is', res)