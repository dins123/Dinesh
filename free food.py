lis = []
for i in range(int(input())):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        lis.append(i)
print(len(set(lis)))