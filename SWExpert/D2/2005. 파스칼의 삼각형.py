import sys
sys.stdin = open('2005. 파스칼의 삼각형.txt')



t = int(input())
for tc in range(1, t+1):
    num = int(input())
    array = []
    for i in range(1, num+1):
        array.append([0] * i)
    
    for idx1, val1 in enumerate(array):
        for idx2, val2 in enumerate(val1):
            if idx2 == 0 or idx1 == idx2:
                array[idx1] = 1
            else:
                print(val1)
        print()