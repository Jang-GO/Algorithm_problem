import sys
import re
sys.stdin = open('input.txt','r')

def yacksu(x):
    cnt = 0
    for i in range(1,x+1):
        if x%i==0:
            cnt+=1
    return cnt

st = input()

res = re.sub(r'[^0-9]','',st)
res=int(res)

print(res)
print(yacksu(res))
