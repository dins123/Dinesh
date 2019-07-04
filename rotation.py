lis = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
for i in range(int(input())):
    rot,string = map(str,input().split())
    st = ' ' 
    for j in string:
        if((lis.index(j)+int(rot))>27):
            y = (lis.index(j)+int(rot)) - 28
        else:
            y = (lis.index(j)+int(rot))
        st = st + lis[y]
    new_st = st[::-1]
    print(new_st)
end = int(input())