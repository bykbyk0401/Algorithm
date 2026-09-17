def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if ans == a[i % len(a)]:
            cnt[0]+=1
        if ans == b[i % len(b)]:
            cnt[1]+=1
        if ans == c[i % len(c)]:
            cnt[2]+=1
    
    answer = []
    
    big = max(cnt)
    for idx, c in enumerate(cnt):
        if c == big:
            if idx == 0:
                answer.append(1)
            elif idx == 1:
                answer.append(2)
            else:
                answer.append(3)
    
    answer.sort()
    return answer