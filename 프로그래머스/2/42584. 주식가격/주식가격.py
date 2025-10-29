def solution(prices):
    answer = []
    
    for i in range(len(prices)) :
        for j in range(i, len(prices)) :
            if prices[i] > prices[j] :
                answer.append(j-i)
                break
            if j == len(prices)-1 :
                    answer.append(len(prices)-1-i)
    return answer