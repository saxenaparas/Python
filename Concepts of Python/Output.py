# It's a fantastic language which 
# automatically identifies the 
# type of data which is coded like 
# it's a (string)(integer)(float/
# decimal) and with many more smart 
# features

# Variables 
# Other than underscore no number nothing 
# can be the starting of variable
_a='''here, 
c=45.90 
b=234'''
a1='It is a string'
a2="It's also a a string"
a3='''"It's also a string"'''
b= 234
c= 45.90

# BOOLEAN
d=True    
e=False
f=None

# Printing Specialities
print("Hello World",1,2,3,sep="~",end="ok end 009\n")

# printing the variables
print(_a)
print(a1)
print(a2)
print(a3)
print(b)
print(c)
print(d)
print(e)
print(f)
print(d+e)
print(d*e)

# printing the types of variables
print(type(_a))
print(type(a1))
print(type(a2))
print(type(a3))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# To print the length of the string
print(len(_a))
print(len(a1))
print(len(a2))
print(len(a3))

# You can't find length of numbers and boolean expressions
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))