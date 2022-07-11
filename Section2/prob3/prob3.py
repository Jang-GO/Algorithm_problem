import sys
sys.stdin = open("input.txt",'rt')

n,k = map(int,input().split())
a = list(map(int,input().split()))

y = set()
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for z in range(j+1,len(a)):
            s = a[i]+a[j]+a[z]
            y.add(s)
y = list(y)
y.sort(reverse = True)

print(y[k-1])
