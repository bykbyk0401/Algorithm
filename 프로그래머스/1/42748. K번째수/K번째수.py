def solution(array, commands):
    answer = []
    
    for c in commands :
        i = c[0]
        j = c[1]
        k = c[2]
        
        new = list(array[q] for q in range(i-1, j))
        new.sort()
        answer.append(new[k-1])
            
    return answer