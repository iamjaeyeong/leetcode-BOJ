def solution(s):
    def sqrt(a, b):
        ret = 0
        while a:
            a = a//b
            ret += 1
        return ret
    answer = []
    for unit in range(len(s)//2, 0, -1):
        length = len(s)
        idx = unit
        prev = 0
        rep = 0
        while idx+unit<=len(s):
            if s[prev:prev+unit]==s[idx:idx+unit]:
                rep += 1
            else:
                if rep:
                    length -= (rep+1)*unit
                    length += unit+(sqrt(rep+1, 10))
                rep = 0
                prev = idx
            idx += unit
            
        if rep:
            length -= (rep+1)*unit
            length += unit+(sqrt(rep+1, 10))
            
        answer.append(length)
    return min(answer) if answer else 1