'''
Want to know more about Recursion chk [Factorial.cpp/c];
--------------------------------------------------------
Here we have used three concepts :
 >> n! = n*(n-1)! ;
 >> 1! = 1 ;
 >> 0! = 1 ;
--------------------------------------------------------
'''

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return(num*factorial(num - 1))

print(factorial(5))
print(type(factorial))

'''
Febonacci Series :
---------------------------
 >> f(0) = 0;
 >> f(1) = 1;
 >> f(n) = f(n-1) + f(n-2);
---------------------------
'''

def febonacci1(num):
    sum = 0
    count = num
    current = 1
    while(count > 0):
        temp = sum
        print(1,":",sum)
        sum = sum + current
        current = temp
        count = count - 1

num = int(input("Enter The Number Of Terms : "))
febonacci1(num)

def febonacci2(num):
    sum = 0
    count = num
    current = 1
    while(count > 1):
        temp = sum
        sum = sum + current
        current = temp
        count = count - 1
    print(2,":",sum)

febonacci2(num)