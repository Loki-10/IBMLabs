for a in range(2,101):
    flag=0
    for i in range(2,a):
        if(a%i==0):
            flag=1
            break
    print(" {} is Prime".format(a) if flag!=1 else "{} is Not Prime".format(a))
