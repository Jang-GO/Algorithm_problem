"""
리스트 합치기 sort() = O(nlogn) 퀵정렬이 사용되기 때문
*더욱 빠른 시간복잡도로 합치기
"""
import sys
sys.stdin = open('input.txt','r')

n = int(input())
n_li = list(map(int,input().split()))
m = int(input())
m_li = list(map(int,input().split()))

p1=p2 = 0
res_li = []

while p1 < n and p2 < m:
    if n_li[p1]<=m_li[p2]:
        res_li.append(n_li[p1])
        p1+=1
    else:
        res_li.append(m_li[p2])
        p2+=1
if p1<n:
    res_li+= n_li[p1:]
if p2<m:
    res_li+= m_li[p2:]

for x in res_li:
    print(x,end=' ')
