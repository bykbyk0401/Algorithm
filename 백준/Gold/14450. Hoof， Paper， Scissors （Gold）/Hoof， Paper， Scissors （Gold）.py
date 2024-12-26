import sys

input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())
gestures = [0] * (N + 1)
for i in range(1, N + 1):
    gesture = input().strip()
    if gesture == "H":
        gestures[i] = 0  # Hoof
    elif gesture == "P":
        gestures[i] = 1  # Paper
    elif gesture == "S":
        gestures[i] = 2  # Scissors

# 이기는 규칙
# H > S, S > P, P > H
def win(gest1, gest2):
    return (gest1 + 1) % 3 == gest2

# DP 테이블 초기화
dp = [[[0] * 3 for _ in range(K + 1)] for _ in range(N + 1)]

# DP 계산
for i in range(1, N + 1):
    for k in range(K + 1):
        for current in range(3):
            # 이전 게임에서 같은 제스처를 선택
            dp[i][k][current] = dp[i - 1][k][current] + win(current, gestures[i])
            
            # 이전 게임에서 제스처를 변경
            if k > 0:
                for prev in range(3):
                    if prev != current:
                        dp[i][k][current] = max(
                            dp[i][k][current],
                            dp[i - 1][k - 1][prev] + win(current, gestures[i])
                        )

# 결과 계산
result = 0
for k in range(K + 1):
    for gesture in range(3):
        result = max(result, dp[N][k][gesture])

print(result)