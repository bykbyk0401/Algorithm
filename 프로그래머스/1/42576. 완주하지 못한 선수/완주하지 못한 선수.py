import collections

def solution(participant, completion):
    pc = collections.Counter(participant)
    cc = collections.Counter(completion)
    
    result = pc-cc
    
    answer = list(result.keys())[0]
    return answer