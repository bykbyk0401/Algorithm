def solution(clothes):
    count = {}
    answer = 1

    for name, category in clothes:
        count[category] = count.get(category, 0) + 1

    for cnt in count.values():
        answer *= cnt + 1

    return answer - 1