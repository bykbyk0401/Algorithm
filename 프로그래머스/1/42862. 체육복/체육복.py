def solution(n, lost, reserve):
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    
    answer = n - len(real_lost)
    
    for i in sorted(real_lost):
        if int(i)-1 in real_reserve:
            real_reserve.remove(i-1)
            answer+=1
        elif int(i)+1 in real_reserve:
            real_reserve.remove(i+1)
            answer+=1
    return answer