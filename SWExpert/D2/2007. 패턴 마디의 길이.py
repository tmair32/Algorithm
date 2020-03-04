import sys
sys.stdin = open('2007. 패턴 마디의 길이.txt')

t = int(input())
for tc in range(1, t+1):
    array = list(input())
    # print(array)

    minLen = 10
    for i in range(10, 0, -1):
        if array[0:i] == array[i:i*2]:
            if i < minLen: minLen = i
    
    print('#{} {}'.format(tc, minLen))