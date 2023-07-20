"""

"""

# String Slicing :
name = "!!![Paras.Krishna]!!!"
print(name[0:5])            #\
print(name[:5])             #-\                  here, it by default take (0) i.e. interprits as [0:5].
print(name[:])              #--\                 here, by default it takes len(name) i.e. interprits as [0:len(name)].
print(name[6:13])           #---} String Slicing
print(name[:-3])            #--/                 here, interprits as [0:len(name)-3].
print(name[:len(name)-3])   #-/
print(name[-3:-1])          #/                   i.e. for any negative number lets [-x] interprits as [len(name) - x].
print(len(name))

'''
>> Strings are immutable i.e. we can't change the content of the string directly.
>> Here, [name.upper()] or [name.lower()] has created a new string not changed the content of the original string [name].
'''
print(name.upper()) # [.upper()] is used to convert string characters to uppercase.
print(name.lower()) # [.lower()] is used to convert string characters to lowercase.
print(name.rstrip("!")) # [.rstrip("x")] removes the input character like here [x] from the last part of the string not from begining.
print(name.replace("Paras","Ram")) # [.replace("wx","yz")] replaces all occurences of a string with another string like here [wx] with [yz].

you = "Ram,Krishna,Vishnu,Paras"
print(you.split(",")) # [.split("x")] it splits the string at [x] into a list form.

blogHeading = "introduction tO mY BlOg fOr pyThoN"
print(blogHeading.capitalize()) # [.capitalize()] it converts first character of a string to upper case rest all after it to lower case.
b1 = blogHeading.capitalize()
print(b1.center(50,".")) # [.center(parameterz)] it aligns the string to the center as per the parameterz given by the user.
print(len(b1))
print(len(b1.center(50,"."))) # It shows that [.center()] function maintains the string size to [50].
print(you.count("a")) # It counts the number of given substring occur in the string.

print(name.endswith("!!!")) 
''' 
> [.endswith()] chks if the string ends with the given value and return true or false. 
> It can also chk weather a substring present between the string is ends on the given value by providing start and end index positions.
> [.startswith()] same as [.endswith()] just chks the starting value.
'''
print(name.endswith("as", 4,9)) # Here, from [4,9] = ["Paras"] which ends with ["as"] so, TRUE.
print(name.startswith("Pa", 4,9)) # Here, from [4,9] = ["Paras"] which ends with ["as"] so, TRUE.

print(you.find("a")) # [.find()] method gives the first index value of the first occurance of the given substring in the string if not present then returns -1. 
print(you.find("Ram"))
print(you.find("z"))
print(you.find("Rzm"))

# [.index()] it's similar to [.find()] but on failure instead of [-1] it return an error message.
# print(you.index("Rzm")) 

# [.isalnum()] returns TRUE if all characters present in the string are from these sets A-Z,a-z,0-9 if any other character present like puncuation marks etc then it will return FALSE.
b1 = "Hello110"
print(b1.isalnum())

# [.isalfa()] returns TRUE if all characters present in the string are from these sets A-Z,a-z if any other character present like numbers etc then it will return FALSE.
print(b1.isalpha())

# [islower()] returns TRUE if all the characters present in the string are lower characters else FALSE.
s1 = "hello world"
print(s1.islower())

s1 = "Hello World"
print(s1.islower())

# [.isprintable()] returns TRUE if all the characters present in the string are printable else return FALSE.
print(s1.isprintable())
s1 = "Hello World\n"
print(s1.isprintable())

# [.isspace()] returns TRUE if white spaces present in the string weather with the help of the space bar or tab. 
print(s1.isspace())
s1 = "      "
print(s1.isspace())

# [.istitle()] returns true if all the first letters of all the words in the sentence in the string is capital else false.
s1 = "Hello World"
print(s1.istitle())
s1 = "Hello world How are You"
print(s1.istitle())

# [.swapcase()] converts upper case to lower and vice versa in a string.
print(s1.swapcase())

# [.title()] converts all the first letters of words in a sentence of a string in capital letters.
s1 = "hello world how are you"
print(s1.title())


