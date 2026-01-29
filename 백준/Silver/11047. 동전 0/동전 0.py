a, b = map(int, input().split())
arr = []
cnt=0

for i in range(a):
    arr.append(int(input()))

while(b>0):
    k = arr.pop(len(arr)-1)
    if k <= b :
        c=b//k
        b%=k
        cnt+=c

print(cnt)