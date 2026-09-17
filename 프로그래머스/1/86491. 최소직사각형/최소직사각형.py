def solution(sizes):
    fir = []
    sec = []
    for i in sizes:
        fir.append(max(i))
        sec.append(min(i))
    wid = max(fir)
    col = max(sec)
    answer = wid*col
    return answer