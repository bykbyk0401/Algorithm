from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = 0
    
    for i in range(len(numbers)):
        for j in range(2**i):
            if queue:
                n = queue.popleft()
            queue.append(n + numbers[i])
            queue.append(n - numbers[i])
    
    for q in queue :
        if q == target:
            answer+=1
        
    return answer