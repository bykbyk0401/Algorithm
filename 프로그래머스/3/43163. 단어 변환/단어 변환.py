from collections import deque

def solution(begin, target, words):
    q=deque()
    q.append((begin, 0))
    n = len(words)
    visited = [False] * n
    
    if target not in words:
        return 0
    
    while(q):
        now, cnt = q.popleft()
        if now == target:
            return cnt
        for i, next in enumerate(words):
            diff = 0
            for j in range(len(next)):
                if now[j] != next[j]:
                    diff += 1
            if not visited[i] and diff == 1:
                visited[i] = True
                q.append((next, cnt+1))
