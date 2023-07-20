'''
============================================================
TypeCasting Functions Possible Are :
------------------------------------
1.> int()
2.> float()
3.> str()
4.> ord()
5.> hex()
6.> oct()
7.> tuple()
8.> set()
9.> list()
10.> dict()
------------------------------------
There are two types of typecasting takes place in python :
> Explicit Conversion : Which is performed by the user.
> Implicit Conversion : Which python automatically performs.
============================================================
'''
# Explicit :
a = "1"
b = "2"
print (a+b) # Concatinated as both [a] & [b] are strings so, {"1"+"2" = "12"};
print (int(a) + int(b)) # TypeCasted both string variables as int and added as int gives {1+2 = 3};

# Implicit :
c = 6.907
d = 8
print(c+d) # Here, [c] is a float & [d] is int but python automatically typecated both of them as float and give output as float; 