a = input("Enter your Name : ")
print("Welcome", a)

# By default input() takes data as a string :
x = input("Enter First Number : ") # Input taken as a string;
y = input("Enter Second Number : ") # Input taken as a string;
print(x+y) # Concatination gets performed "x"+"y" = "xy" <- Output;

c =int(input("Enter the 1st number : ")) # Here, we have typecasted the input as integer.
d =int(input("Enter the 2nd number : "))
print(c+d)

# print("The First Letter : ",a[0])
# If you go beyond the indexing number let say 20 which is not present give indexing error;

print("Lets Use A For Loop :\n")
for character in a:
    print(character)
    # instead of [character] we can use [i], [j] or any other variable

alphabets = "ABCDE"
for i in alphabets:
    print(i)