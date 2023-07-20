# To Create A Function we use [def] = define-function keyword :
def tocalculateGmean(a, b):
    return (a*b)/(a+b)


def compare(a, b):
    if (a > b):
        print("First no. is greater")
    elif (a == b):
        print("Both are equal")
    else:
        print("Second no. is greater")


# It depends on us how much indentation space we have to give:
c = 9
b = 8
print(tocalculateGmean(c, b))
compare(c, b)


def greater(a, b):  # Here, [a] & [b] are required arguments;
    pass  # we can't leave empty so if we dont have to put inside it then we can use pass;


def function(a=10, b=1):  # Here, [a] & [b] is a default arguments;
    pass


function()  # Execute on the basis of default arguments present;
# This a Key Word agument passing where, [key=value] in this position doesn't matter;
function(b=3, a=3)
# Here, according to the order [a=3] whereas, default value of [b] is taken;
function(3)

'''
Keyword Arbitary Arguments : In this we use a refrence operator [*] variable as an argument;

Case 1 : Here, Functions process the arguments as Touple;
'''


def average(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum = sum + i
    print("Average is :", (sum/len(number)))


average(5, 6, 7, 8, 9, 4, 5)

'''
Case 2 : Here, Functions process the arguments as dict;
'''


def name(**name):
    print(type(name))
    print("Hello", name['fname'], name["mname"], name["lname"])

name(mname="Paras", fname="Smita", lname="Saxena")