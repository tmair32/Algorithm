import sys
sys.stdin = open("1954.달팽이 숫자.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    NN = N**2

    snail = [[0 for _ in range(N)] for _ in range(N)]
    y, x = 0, 0
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    num = 1
    flag = 0

    snail[y][x] = num
    while flag == 0:
        for i in range(4):
            while True:
                if snail[y][x] == NN:
                    flag = 1
                    break
                y += dy[i]
                x += dx[i]
                if x < 0 or x >= N:
                    x -= dx[i]
                    break
                if y < 0 or y >= N:
                    y -= dy[i]
                    break
                if snail[y][x] != 0:
                    y -= dy[i]
                    x -= dx[i]
                    break
                snail[y][x] = num + 1
                num += 1
    print("#{}".format(tc))
    for i in range(N):
        print(" ".join(map(str, snail[i])))