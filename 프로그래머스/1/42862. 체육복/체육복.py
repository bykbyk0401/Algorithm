def solution(n, lost, reserve):
    # 1. (n+2) 크기의 학생 상태 배열 생성 (0번과 n+1번 인덱스는 패딩)
    #    모든 학생이 1벌씩 가졌다고 초기화
    status = [1] * (n + 2)
    
    # 2. 여벌 체육복이 있는 학생은 +1
    for r in reserve:
        status[r] += 1
        
    # 3. 도난당한 학생은 -1
    for l in lost:
        status[l] -= 1
    
    # [핵심 로직]
    # 3-1. A학생이 잃어버리고(status=0), 여분도 있으면(status=2)
    #      (1 - 1 + 1) = 1이 됩니다.
    #      이는 "자신이 입어야 해서 빌려줄 수 없는 학생"이 되어 
    #      자동으로 예외 처리가 완료됩니다.

    # 4. 1번 학생부터 n번 학생까지 순회
    for i in range(1, n + 1):
        # 4-1. 현재 학생(i)이 체육복이 없다면 (status == 0)
        if status[i] == 0:
            # 4-2. (그리디) 앞 번호 학생(i-1)이 2벌 가졌는지 확인
            if status[i - 1] == 2:
                status[i - 1] -= 1 # 앞 학생 1벌 차감
                status[i] += 1   # 현재 학생 1벌 추가
                
            # 4-3. (그리디) 뒷 번호 학생(i+1)이 2벌 가졌는지 확인
            # (앞에서 빌렸다면 이 코드는 실행되지 않음)
            elif status[i + 1] == 2:
                status[i + 1] -= 1 # 뒷 학생 1벌 차감
                status[i] += 1   # 현재 학생 1벌 추가

    # 5. 최종적으로 체육복이 1벌 이상(>0)인 학생 수 계산
    answer = 0
    for i in range(1, n + 1):
        if status[i] > 0:
            answer += 1
            
    return answer