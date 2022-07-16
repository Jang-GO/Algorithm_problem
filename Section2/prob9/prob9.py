'''
규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
'''
import sys
sys.stdin = open('input.txt','rt')

res=0
n=int(input())
for i in range(n):
    noon = input().split()
    noon.sort()
    a,b,c = map(int,noon)
    if a==b and b==c:
        price = 10000 + (a * 1000)
    elif a==b or a==c :
        price = 1000 + (a * 100)
    elif b==c:
        price = 1000 + (b * 100)
    else:
        price = 100*c

    if price>res:
        res = price

print(res)
