import sys
sys.stdin = open("1946.간단한 압축풀기.txt")

T = int(input())
for tc in range(1):
    N = int(input())
    res = ""
    for i in range(N):
        Ci, Ki = map(str, input().split())
        res += (Ci * int(Ki))
        if res.