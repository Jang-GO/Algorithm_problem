import sys
sys.stdin = open('input.txt','rt')

n = int(input())
arr = [0]*(n+1)
cnt=0
for i in range(2,n+1):
    if arr[i] == 0:
        cnt+=1
        for j in range(i,n+1,i):
            arr[j] = 1

print(cnt)
