age = int(input("Enter Your Age : "))
# Conditional Operators : < , > , <= , >= , == , != :
print(age > 18)
print(age < 18)
print(age <= 18)
print(age >= 18)
print(age == 18)
print(age != 18)

if (age < 18):  # print statement is inside if block
    print("Can't Apply for Licence")
    print("This is inside if block")
elif (age == 18):
    print("You Can Apply for non gear")
    print("This is inside elif block")
else:  # Both if else statements are inside else block
    if (age > 18 & age < 30):
        print("You Can Apply")
    else:
        print("You Already have Licence")
    print("This is inside else block")
print("This isn't inside any block")
'''
Here take care of indentation i.e. instead of using {curly braces} the 
block of each function is decided by the indentation spacing as we can 
see above after if statement whatever is inside if block is type after 
the tab spacing this indentation denotes that line of code is inside 
if statements.
'''
