import sys
sys.stdin = open('1204.최빈수 구하기.txt')

t = int(input())
for tc in range(1, t+1):
    p = int(input())
    inp = list(map(int, input().split()))
    cnt = [0 for i in range(101)]
    for i in inp:
        cnt[i] += 1
    
    maxN = 0
    maxIdx = 0
    for idx, val in enumerate(cnt):
        if val >= maxN:
            maxN = val
            maxIdx = idx
    print('#{} {}'.format(tc, maxIdx))

    