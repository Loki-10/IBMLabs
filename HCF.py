a = int(input())
b = int(input())
smaller = a if a < b else b
for i in range(1, smaller + 1):
    if (a % i == 0) and (b % i == 0):
        hcf = i
print(hcf)
