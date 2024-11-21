N, K = map(int, input().split())
temp = list(map(int, input().split()))

prefix_sum = [0]*(N+1) 

# 온도의 최소값이 -100이므로 초기값을 (N+1)*-100으로 설정한다.
answer = (N+1) * -100

# 누적 합 구하기
for i in range(1, N+1):
    prefix_sum[i] += prefix_sum[i-1]+temp[i-1]

# K 구간 합 구하기
for i in range(1, N-K+2):
    temp_sum = prefix_sum[i+K-1] - prefix_sum[i-1]

    # 최댓값 구하기
    if temp_sum > answer:
        answer = temp_sum

print(answer)