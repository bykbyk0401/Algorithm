n = int(input())
money = []
cnt = 0
result = 0

for _ in range(n) :
    num = int(input())
    if num == 0 and cnt != 0 :
        money.pop()
        cnt -= 1
    elif num != 0 :
        money.append(num)
        cnt += 1

for i in range(cnt) :
    result += money[i]

print(result)