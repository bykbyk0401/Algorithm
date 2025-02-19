import sys
input = sys.stdin.readline

N = int(input().strip())

if N==1:
    print(1)
else:
    num=1
    for i in range(1, N):
        num+=6*i
        if N<=num:
            print(i+1)
            break
