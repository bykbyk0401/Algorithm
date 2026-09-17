def solution(name):
    answer = 0
    updown = []
    
    for i in name:
        updown.append(min(ord(i)-ord('A'), ord('Z')-ord(i)+1))
    updown = sum(updown)
    
    min_lr = len(name)-1
    
    for i in range(len(name)):
        next = i+1
        while(next<len(name) and name[next]=='A'):
            next+=1
        d1 = 2*i + len(name)-next
        d2 = i + 2*(len(name)-next)
        
        min_lr = min(min_lr, d1, d2)
    
    answer = updown + min_lr
    return answer