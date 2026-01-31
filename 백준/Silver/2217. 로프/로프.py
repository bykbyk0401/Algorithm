import sys
input = sys.stdin.readline

n = int(input())
arr = []
possible = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
k = len(arr)
for i in arr:
    possible.append(i*k)
    k-=1
print(max(possible))