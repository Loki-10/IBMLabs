n1=int(input())
n2=int(input())
great = n if n < n2 else  n2
while True:
    if (great % n == 0 and great % n2 == 0): 
        print(great);
        break;
    great=great+1
