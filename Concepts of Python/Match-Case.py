x = int(input("Enter Value of x : "))
'''
Match-Case statements just like Switch-Case just the difference is it works 
like if-else type also so no need to put [break] after every statement like
in switch case because if condition satisfies it only execute the upper one 
only at a time.
'''
match x:
    case 0:
        print(x, "is 0")
    case 4:
        print(x, "is 4")
    case _ if x < 5:
        print(x, "is less than 5")
    case _ if x < 10:
        print(x, "is less than 10")
    case _ if x < 20:
        print(x, "is less than 20")
    case _ if x < 30:
        print(x, "is less than 30")
    case _ if x < 40:
        print(x, "is less than 40")
    case _:
        print(x, "Default Case Executed")
