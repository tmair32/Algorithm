import sys
sys.stdin = open("1959.두 개의 숫자열.txt")

def sol(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    n = max(N, M) - min(N, M) + 1
    res = []
    for i in range(n):
        if N >= M:
            res.append(sol(Ai[i:i+M], Bj))
        else:
            res.append(sol(Ai, Bj[i:i+N]))
    print("#{} {}".format(tc, max(res)))

