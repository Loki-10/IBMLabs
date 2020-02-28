a=int(input())
flag=0
for i in range(2,a//2):
    if(a%i==0):
        flag=1
        break
print("Prime" if flag!=1 else "Not Prime")
