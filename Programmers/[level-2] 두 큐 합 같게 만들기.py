def solution(q1, q2):
    s = sum(q1)
    answer = 0
    q1.extend(q2)
    q = q1
    p1, p2 = 0, len(q2)
    target = sum(q)/2
    while 1:
        if p2==len(q):
            if s>target:
                s -= q[p1]
                answer += 1
                p1 += 1
            elif s==target:
                break
            else:
                answer = -1
                break
        else:
            if s>target:
                s -= q[p1]
                p1 += 1
                answer += 1
            elif s==target:
                break
            else:
                s += q[p2]
                p2 += 1
                answer += 1
    return answer
            
    