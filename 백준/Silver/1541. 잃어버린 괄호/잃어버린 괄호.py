import sys
input = sys.stdin.readline

expression = input().strip().split('-')

answer = 0
for num in expression[0].split('+'):
    answer += int(num)

for chunk in expression[1:]:
    temp_sum = 0
    for num in chunk.split('+'):
        temp_sum += int(num)

    answer -= temp_sum

print(answer)