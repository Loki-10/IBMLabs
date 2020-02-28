row1 = int(input("Rows of First Matrix:"))
col1 = int(input("Column of First Matrix:"))
row2 = int(input("Rows of Second Matrix:"))
col2 = int(input("Column of Second Matrix:"))
A = []
B = []
result=[]
for i in range(row1):
    a = []
    for j in range(col1):
        a.append(int(input()))
    A.append(a)
for i in range(row2):
    a = []
    for j in range(col2):
        a.append(int(input()))
    B.append(a)
for i in range(row1):
    a = []
    for j in range(col2):
        a.append(0)
    result.append(a)
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
for r in result:
    print(r)
