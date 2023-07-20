'''
String Formatting :
 >> String Interpolation commanly known as F-Strings;
 >> Primary focus to make interpolation easier;
 >> It offers a convenint way to embed python expressions inside string literals;
 >> F-string can be formatted same as str.format() method;
 >> This method is introduced after python 3.6 onwards;
'''

letter = "1.] My name is {} and I am from {}"
name = "Paras Saxena"
country = "India"
print(letter.format(name,country))

letter = "2.] My name is {1} and I am from {0}"
print(letter.format(country,name))

# [.2f] will allow to print only two decimal values, {but it give a round off value};
txt = "3.] For only ${price:.2f}!" 
print(txt.format(price = 49.99789))
print()

# Syntax F-String is like : f"sentence{argument}sentence" :
print("--------------[Using F-String]----------------")
print(f"4.] My name is {name} and I am from {country}")

price = 49.99789
txt = f"5.] For only ${price:.2f}!" 
print(txt)

print(f"6.] {2*30}") # Now, the output value is a string data_type [60];
print("7.]",type(f"{2*30}")) 
print()

# If we want to print literal way : if you want to show curly brackets in output then use them twice : [ {{, }} ] :
print("-----------[Printing Literal Way]-------------")
print("8.] We use f-strings like this",f": My name is {{name}} and I am from {{country}}")