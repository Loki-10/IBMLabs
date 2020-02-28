import cmath
a=int(input())
b=int(input())
c=int(input())
an=(b**2)-(4*a*c)
s1=(-b-cmath.sqrt(an))/(2*a)
s2=(-b+cmath.sqrt(an))/(2*a)
print("{0} and {1}".format(s1,s2))
