import sys
sys.stdin = open('1284.수도 요금 경쟁.txt')

t = int(input())
for tc in range(1, t+1):
    li = list(map(int, input().split()))
    A = li[0] * li[4]
    if li[2] >= li[4]:
        B = li[1]
    else:
        B = li[1] + li[3] * (li[4] - li[2])

    if A > B:
        print('#{} {}'.format(tc, B))
    else:
        print('#{} {}'.format(tc, A))