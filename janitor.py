import math
s1,s2,s3,s4 = map(int,input().split())
semi = (s1+s2+s3+s4)/2
res = math.sqrt((semi-s1)*(semi-s2)*(semi-s3)*(semi-s4))
if (res % 1 == 0):
    print(int(res))
else:
    print(res)