import sys
sys.stdin = open('1288.새로운 불면증 치료법.txt')

t = int(input())
for tc in range(1, t+1):
    num = int(input())
    n = 0
    result = []
    while len(result) < 10:
        n += 1
        numb = num * n
        for i in str(numb):
            if int(i) not in result:
                result.append(int(i))
    print(f'#{tc} {numb}')