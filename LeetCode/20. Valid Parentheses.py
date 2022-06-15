class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        is_neg = False
        
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                stack.append(ch) 
            else:
                if stack:
                    p = stack.pop()
                else:
                    is_neg = True
                    break
                if abs(ord(p)-ord(ch))<3:
                    continue
                else:
                    is_neg = True
                    break
        
        if is_neg or stack:
            return False
        return True