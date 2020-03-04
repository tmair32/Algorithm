import sys
from datetime import datetime, timedelta
sys.stdin = open("1948.날짜 계산기.txt")

T = int(input())
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    res = datetime(1900, m2, d2) - datetime(1900, m1, d1)
    print("#{} {}".format(tc, res.days+1))
