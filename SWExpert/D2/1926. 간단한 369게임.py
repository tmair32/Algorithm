import sys
sys.stdin = open('1926. 간단한 369게임.txt')

t = int(input())

for i in range(1, t+1):
    string = str(i)
    clap = string.count('3') + string.count('6') + string.count('9')
    if clap > 0:
        print('-'*clap, end=' ')
    else:
        print(i, end=' ')

    
    

    