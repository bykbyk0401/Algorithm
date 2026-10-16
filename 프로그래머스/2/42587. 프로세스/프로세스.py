from collections import deque

def solution(priorities, location):
    answer = []
    q=deque()
    pq=deque(priorities)
    
    for i, p in enumerate(priorities):
        q.append((i,p))
    
    while(q):
        i, p = q.popleft()
        if p != max(pq):
            q.append((i,p))
            index = pq.popleft()
            pq.append(index)
        else:
            answer.append(i)
            pq.popleft()
            if i == location:
                break
    
    for i, a in enumerate(answer):
        if a == location:
            return i+1