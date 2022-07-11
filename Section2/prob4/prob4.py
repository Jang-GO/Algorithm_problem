''' 
주의사항: 파이썬의 round 함수는 소수점이 5이면 가까운 짝수쪽으로 숫자를 반환하는 round-half-even 방식을 사용
1.n명의 학생의 평균을 구하고
2. n명의 학생중 평균애 가까운 학생은 몇번쨰 학생인지
(여러명 우선순위: 1.점수가 높은학생 2.학생번호가 빠른 학생의 번호)
'''
import sys
sys.stdin = open("input.txt",'rt')

n = int(input())
k = list(map(int,input().split()))

total = 0
average = 0
for i in k:
    total +=i
average = round(total / n)

score = 0
min = k[0]
for idx,x in enumerate(k):
    if abs(x-average) < min:
        min = abs(x-average)
        score = x
        res = idx +1
    elif abs(x-average)==min:
        if x>score: 
            score = x
            res = idx+1
print(average,res)
