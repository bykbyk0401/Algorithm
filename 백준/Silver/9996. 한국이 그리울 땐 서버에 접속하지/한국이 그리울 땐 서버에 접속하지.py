n = int(input())
pattern = input().split("*")
length = len(pattern[0]) + len(pattern[1])

for _ in range(n):
	file = input()
	# 패턴이 한글자씩이 아닐 수도 있음
	if length > len(file):
		print("NE")
		
	else:
		if pattern[0] == file[:len(pattern[0])] and pattern[1] == file[-len(pattern[1]):]:
			# file[-a : ]는 뒤에 a번째 문자부터 끝까지 가져옴
			print("DA")
		else:
			print("NE")