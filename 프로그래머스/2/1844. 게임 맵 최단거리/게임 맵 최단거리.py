from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    answer = 0
    
    queue.append((0,0,1))
    visited[0][0] = 1
    
    while(queue):
        x,y,p = queue.popleft()
        
        if x == n-1 and y == m-1 :
            answer = p
            break
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny, p+1))
                visited[nx][ny] = 1
        
    if answer == 0:
        return -1
    else:
        return answer
