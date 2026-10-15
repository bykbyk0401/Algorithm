def solution(clothes):
    count = {}
    answer = 1
    
    for name, category in clothes:
        count[category] = count.get(category, 0) + 1
    
    for category in count:
        answer *= (count.get(category) + 1)
    
    return answer - 1