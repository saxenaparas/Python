def Decide(a):
        if (a[0] == a[1] == a[2] or a[3] == a[4] == a[5] or a[6] == a[7] == a[8] or a[0] == a[3] == a[6] or a[1] == a[4] == a[7] or a[2] == a[5] == a[8] or a[0] == a[4] == a[8] or a[2] == a[4] == a[6]):
            return 1
        else :
            return 0

a = [1,2,3,4,5,6,7,8,9]

print(f''' 
 {a[0]} | {a[1]} | {a[2]}
-----------
 {a[3]} | {a[4]} | {a[5]}
-----------
 {a[6]} | {a[7]} | {a[8]}
''')

c = int(input("Choose either O[means 0] or X[means 1] : "))

check = True
chk = [0,0,0,0,0,0,0,0,0]

while(check):

    if c :
        v = 'X'
    else :
        v = 'O'
    
    print(f"It's {v}'s turn : ")
    x = int(input(f"Choose your position of [{v}] : "))
    

    match x:
        case 1 : 
            if(not chk[0]):
                a[0] = v
                chk[0] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 2 :
            if(not chk[1]):
                a[1] = v
                chk[1] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 3 :
            if(not chk[2]):
                a[2] = v
                chk[2] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 4 :
            if(not chk[3]):
                a[3] = v
                chk[3] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 5 :
            if(not chk[4]):
                a[4] = v
                chk[4] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 6 :
            if(not chk[5]):
                a[5] = v
                chk[5] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 7 :
            if(not chk[6]):
                a[6] = v
                chk[6] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 8 :
            if(not chk[7]):
                a[7] = v
                chk[7] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case 9 :
            if(not chk[8]):
                a[8] = v
                chk[8] = 1
            else:
                print("Already Placed; Choose Another : ")
                continue
        case _:
            print('Invalid Option : ')
            continue
    
    print(f''' 
    {a[0]} | {a[1]} | {a[2]}
    -----------
    {a[3]} | {a[4]} | {a[5]}
    -----------
    {a[6]} | {a[7]} | {a[8]}
    ''')

    win = Decide(a)

    if win :
        check = False
        print(f"---------[{v}] is the Winner---------")
        continue

    # for i in chk :
    if(chk[0] == 1 and chk[1] == 1 and chk[2] == 1 and chk[3] == 1 and chk[4] == 1 and chk[5] == 1 and chk[6] == 1 and chk[7] == 1 and chk[8] == 1):
            check  = False
            print("---------It's a DRAW---------")
    
    '''
    itr = 1
    for i in chk :
        itr = itr*chk[i]

    if itr :
        check = False
        print("---------It's a DRAW---------")
    '''

    if c == 1:
        c = 0
    else :
        c = 1




