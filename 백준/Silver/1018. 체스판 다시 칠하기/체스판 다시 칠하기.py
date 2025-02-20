N, M = map(int, input().split())
chess = []
count = []

for _ in range(N) :
    chess.append(input())

for n in range(N-7) :
    for m in range(M-7) :
        startW = 0
        startB = 0
        for i in range(n, n+8) :
            for j in range(m, m+8) :
                if((i+j)%2 == 0) :
                    if chess[i][j] == 'B' :
                        startW += 1
                    elif chess[i][j] == 'W' :
                        startB += 1
                else :
                    if chess[i][j] == 'W' :
                        startW += 1
                    elif chess[i][j] == 'B' :
                        startB += 1
        count.append(min(startW, startB))

print(min(count))