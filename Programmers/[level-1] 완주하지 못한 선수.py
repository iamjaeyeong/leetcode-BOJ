def solution(participant, completion):
    d = {i:0 for i in participant}
    for p in participant:
        d[p] += 1
    for c in completion:
        d[c] -= 1
    
    for name, cnt in d.items():
        if cnt:
            return name