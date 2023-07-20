"""
Numeric Data type : int,float,complex;
Syntax : complex(real_part, imaginary_part);

Text Data : str;
Boolean Data : bool;

Sequenced Data : list,tuple;
tuple : same as list but it's immutable;

Mapped Data : dict;
dict : It can store the key value pairs;
"""

list1 = [8, 2.3, [-4, 5], "apple", "banana"]
tuple1 = (("parrot", "sparrow"), ("lion", "tiger"))
dict1 = {"name": "sakshi", "age": 20, "canVote": True}

print(list1)
print(tuple1)
print(dict1)

print("------------")

print(type(list1))
print(type(tuple1))
print(type(dict1))