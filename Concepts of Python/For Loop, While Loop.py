
name = "PARAS"
for i in name:
    print(i)

colors = ["RED","GREEN","BLUE","YELLOW","GOLD"]
for i in colors:
    print(i)

for k in range(5): # By default range initial value is [0] and condition here seen as k < 5 so, goes till [4];
    print(k)

for k in range(10,101): # So, range(initial,final) goes till [final-1];
    print(k)

for k in range(1,10,3): # So, range(initial,final,step) step omits the no. of steps after each execute step;
    print(k)

for k in range(1,10,2):
    print(k)

i = 0
while(i<=10):
    print(i)
    i=i+1

# ========================================================================
# If While condition not satisfied then else condition executed :
i = int(input("Enter PassKey : "))
while(i == 101):
    print("You Have Entered Inside While Loop")
    k = 0
    while(k < 100):
        k = int(input('Enter the numbers : '))
        print(k)
    i = int(input("Want To Exit From Loop Enter Another PassKey : "))
    if(i == 101):
        break
else:
    print("You Are Outside While Loop")
#-------------------------------------------------------------------------
# break : loop ko chord kar nikal jao;
# continue : itration ko chord kar nikal jao;
j = 0
while(j<=200):
    j = j+1
    if(j == 6):
        continue # Continue will skip the below code after it in its block
    if(j == 11):
        break
    print("5 x",j,"=",j*5)
else: # This will also not gets execicuted as break will get out of loop 
    print("Table Ends")
# ========================================================================
# Do-While is not present in python;