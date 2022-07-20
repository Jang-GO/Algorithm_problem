import sys
sys.stdin = open('input.txt','r')

n = int(input())
a=[list(map(int,input().split())) for _ in range(n)]
sum=0

r = l = n//2

for i in range(n):
    for j in range(r,l+1):
        sum += a[i][j]
    if i < n//2:
        r-=1
        l+=1
    else:
        r+=1
        l-=1
print(sum)
