a,b,c = map(int,input().split())
order = input()
sum = a+b+c
for i in order:
    if(i=='A'):
        print(min(a,b,c),end = ' ')
    elif(i=='C'):
        print(max(a,b,c),end = ' ')
    else:
        print(sum-(min(a,b,c))-(max(a,b,c)), end = ' ')
        