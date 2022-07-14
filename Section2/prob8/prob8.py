import sys
sys.stdin = open('input.txt','r')

n = int(input())
n_list = list(map(int,input().split()))

def reverse(x):
    res = 0
    while x>0:
        t=x%10
        res = res*10+t
        x= x//10
    return res

def isPrime(x):
    if x ==1:
        return False
    for i in range(2,x//2+1): # 약수들의 곱으로 x를 표현하면 절반이후부턴 대칭적으로 나옴
        if x%i ==0:
            return False
    else:
        return True

for i in n_list:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp,end=' ')
