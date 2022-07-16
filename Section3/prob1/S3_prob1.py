import sys
sys.stdin = open("input.txt",'r')

def letter_reverse(x):
    x = x[::-1]
    return x

n=int(input())
for i in range(n):
    s = input()
    s = s.lower()

    rs = letter_reverse(s)

    if s == rs:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO'
