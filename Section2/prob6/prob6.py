import sys
sys.stdin = open('input.txt','rt')

def digit_sum(x):
    sum=0
    while x>0:
        sum += x%10 #맨 아래 자릿수부터 더함
        x = x//10 #한자리 위로 올라감
    return sum
        
n = int(input())
sp = list(map(int,input().split()))

max = 0
for b in sp:
    tot = digit_sum(b)
    if tot > max:
        max = tot
        res = b
print(res)
