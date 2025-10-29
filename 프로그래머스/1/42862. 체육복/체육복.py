def solution(n, lost, reserve):
    status = [1]*(n+2)
    for i in lost :
        status[i] -= 1
    for j in reserve :
        status[j] += 1
    for k in range(n) :
        if status[k+1] == 0 :
            if status[k] == 2 and status[k+2] == 2 :
                status[k+1] += 1
                status[k] -= 1
            elif status[k] == 2 :
                status[k+1] += 1
                status[k] -= 1
            elif status[k+2] == 2 :
                status[k+1] += 1
                status[k+2] -= 1
    answer = -2
    for i in status :
        if i > 0 :
            answer += 1
    return answer