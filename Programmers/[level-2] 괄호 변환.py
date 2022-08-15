def solution(p):
    answer = ''
    def is_right(parentheses):
        stack = 0
        for p in parentheses:
            if p=="(":
                stack += 1
            else:
                if stack<=0:
                    return 0
                else:
                    stack -= 1
        return 0 if stack else 1
    
    def flip(parentheses):
        ret = ""
        for i in range(1, len(parentheses)-1):
            if parentheses[i]=="(":
                ret += ")"
            else:
                ret += "("
        return ret
    
    def split_parentheses(parentheses):
        count = [0, 0]
        if parentheses[0]=='(':
            count[0] += 1
        else:
            count[1] += 1
        for i in range(1, len(parentheses)):
            if parentheses[i]=='(':
                count[0] += 1
            else:
                count[1] += 1
            if count[0]==count[1]:
                break
        return parentheses[:i+1], parentheses[i+1:]
    
    def transform(p):
        if is_right(p) or len(p)==0:
            return p
        else:
            u, v = split_parentheses(p)
            if is_right(u):
                return u + transform(v)
            else:
                return "(" + transform(v) + ")" + flip(u)
    answer = transform(p)
    return answer