'''
-------------------------------------------------
Some basic operators : (+,-,*,/,%);
Some advance : {floor division operator} (//,**);
(//) : From the float/decimal value it gives the 
       int part like : 15/6 = 2.5 but, 15//6 = 2;
(**) : It works like [a**b] then a^b, eg : 
       [5**3] = [5*5*5] = [5^3] = 125;
-------------------------------------------------
'''
# function to convert to superscript
def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
  
# display superscipt
print(get_super('GeeksforGeeks')) #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ

# Calculator :
print("Enter Two Numbers : ")
a = int(input("Enter First number :"))
b = int(input("Enter Second number :"))


print("Sum :",a+b)
print("Difference :",a-b)
print("Product :",a*b)
print("Division :",a/b)
print("Quotient (Floor Division Value) :",a//b)
print("Remainder :",a%b)
print("a" + get_super('b'),":" ,a**b)
