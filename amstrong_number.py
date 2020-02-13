n=int(input())
s=0;a=n
size=len(str(n))
while(a>0):
    r=a%10
    s+=r**size
    a=a//10
print ("Amstrong Number" if n==s else "Not Amstrong Number")