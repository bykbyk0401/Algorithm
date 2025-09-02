def solution(ingredient):
    array = []
    answer = 0
    
    for i in ingredient :
        array.append(i)
        if array[-4:] == [1,2,3,1] :
            array.pop()
            array.pop()
            array.pop()
            array.pop()
            answer += 1

    return answer