n = int(input())
vps = []


for _ in range(n) :
    vps.append(list(input()))

for i in range(n) :
    stack = []
    cnt = len(vps[i])
    for j in range(len(vps[i])) :
        if vps[i][j] == '(' :
            stack.append('(')
            cnt -= 1
        else :
            if len(stack) == 0 :
                print("NO")
                break
            stack.pop()
            cnt -= 1
    if len(stack) == 0 and cnt == 0 :
        print("YES")
    elif len(stack) != 0 :
        print("NO")
