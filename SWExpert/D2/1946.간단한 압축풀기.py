import sys
sys.stdin = open("1946.간단한 압축풀기.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    res = ""
    print("#{}".format(tc))
    for i in range(N):
        Ci, Ki = map(str, input().split())
        res += (Ci * int(Ki))
        while len(res) >= 10:
            print(res[0:10])
            res = res[10:]
    print(res)