import sys
N = int(sys.stdin.readline())
st = sys.stdin.readline().strip()
stack = [] # 괄호검사 하기위한 스택
cnt = [0] * N # 제데로 된 스택인 것들을 담을 배열
ans = 0
max_ans = 0
for i in range(N):
    if st[i] == "(": # "(" 면 스택에 i 번째라는 숫자 추가
        stack.append(i)
    else:
        if stack:
            cnt[i] = cnt[stack[-1]] = 1 # 스택에 "("이 있고 ")"가 들어오면 ")" 이 괄호가 들어온 순서랑 스택에 "(" 괄호 들어갔을때 순서를 cnt 리스트에 1로 체킹 
            stack.pop() # 그리고 "(" 빼주기
for c in cnt: # 연속적인 1이 얼마나 있는지 체크
    if c == 1: 
        ans += 1 # 1일경우 ans + 1 해주고
        max_ans = max(max_ans, ans) # 최대 cnt를 max_ans에 초기화 해주기
    else: # 1이 아닐경우 ans 0으로 초기화 
        ans = 0
print(max_ans)