def solution(s):
    answer = -1
    stack = []
    
    for c in s:
        if len(stack)==0:
            stack.append(c)
        else:
            if stack[-1]==c:
                stack.pop()
            else:
                stack.append(c)
                
    return 0 if stack else 1
        