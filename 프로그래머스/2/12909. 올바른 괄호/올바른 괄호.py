def solution(s):
    answer = 0
    
    for i in s:
        if i == '(':
            answer+=1
        elif i == ')':
            answer-=1
        if answer<0:
            return False
    
    if answer == 0:
        return True
    return False
