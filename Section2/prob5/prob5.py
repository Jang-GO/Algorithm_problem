'''
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확
률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''
import sys
sys.stdin = open('input.txt','rt')

n,m = map(int,input().split())
s_list = []
cnt = []
for i in range(1,n+1):
    for j in range(1,m+1):
        sum = i+j
        s_list.append(sum)
max = 0
for i in range(sum):
    cnt.append(s_list.count(i))
    if max<cnt[i]:
        max = cnt[i]

for i in range(sum):
    if cnt[i] == max:
        print(i, end=' ') 
