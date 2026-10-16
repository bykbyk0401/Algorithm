def solution(progresses, speeds):
    left = []
    work = []
    answer = []
    
    for p in progresses:
        left.append(100-p)
    
    for i, s in enumerate(speeds):
        if left[i]%s == 0:
            work.append(left[i]//s)
        else:
            work.append(left[i]//s + 1)
    
    print(work)
    now = 0
    cnt = 1
    for i in range(1, len(work)):
        if work[now]>=work[i]:
            cnt+=1
        else:
            answer.append(cnt)
            now=i
            cnt=1
    
    answer.append(cnt)
        
    return answer