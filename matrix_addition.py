row=int(input())
col=int(input())
first=[]
second=[]
for i in range(row):
  a=[]
  for j in range(col):
    a.append(int(input()))
  first.append(a)
for i in range(row):
  a=[]
  for j in range(col):
    a.append(int(input()))
  second.append(a)
for i in range(row):
  for j in range(col):
    print(first[i][j]+second[i][j],end=" ")
  print()
