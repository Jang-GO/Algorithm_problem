import sys
sys.stdin = open ('input.txt','r')

card = [i for i in range(21)]
for _ in range(1,11):
    ai,bi = map(int,input().split())
    for i in range((bi-ai+1)//2):
        card[ai+i],card[bi-i] = card[bi-i],card[ai+i]

card.pop(0)      
for x in card:
    print(x,end=' ')
