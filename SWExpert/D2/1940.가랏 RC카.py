import sys
sys.stdin = open("1940.가랏! RC카!.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    v, s = 0, 0
    for i in range(N):
        Command = list(map(str, input().split()))
        if Command[0] == '1':
            v += int(Command[1])
        elif Command[0] == '2':
            if v <= int(Command[1]):
                v = 0
            else:
                v -= int(Command[1])
        s += v
    print("#{} {}".format(tc, s))