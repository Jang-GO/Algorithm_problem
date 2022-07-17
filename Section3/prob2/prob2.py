import sys
sys.stdin = open('input.txt','r')

def yacksu(x):
    cnt = 0
    for i in range(1,x+1):
        if x%i==0:
            cnt+=1
    return cnt

st = input()
res=0
for i in st:
    if i.isdecimal():
        res=res*10+int(i)
        
print(res)
print(yacksu(res))
