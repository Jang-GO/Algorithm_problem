import sys
sys.stdin = open("input.txt",'r')
def column(l):
    max=0
    for i in range(len(l)):
        sum=0
        for j in range(len(l)):
            sum+=l[i][j]
            if sum > max:
                max = sum
    return max

def row(l):
    max=0
    for i in range(len(l)):
        sum = 0
        for j in range(len(l)):
            sum += l[j][i]
            if sum> max:
                max = sum
    return max

def diagonal(l):
    max=0
    sum_l=0
    sum_r=0
    for i in range(len(l)):
        sum_l+=a[i][i]
    for i in range(len(l)):
        sum_r+=a[i][len(l)-i-1]
    if sum_l > sum_r:
        max = sum_l
    else:
        max = sum_r
    return max

n = int(input())
a = []*5

for i in range(n):
    m = list(map(int,input().split()))
    a.append(m)
if column(a)>row(a) and column(a)>diagonal(a):
    print(column(a))
if row(a)>column(a) and row(a)>diagonal(a):
    print(row(a))
if diagonal(a)>column(a) and diagonal(a)>row(a):
    print(diagonal(a))
