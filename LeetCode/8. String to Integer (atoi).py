class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = -1
        end = len(s)
        is_positive = True
        limit = pow(2, 31)
        
        for i in range(len(s)):
            if s[i]==' ':
                continue
            else:
                start = i
                break
                
        if start==-1:
            return 0
                
        if s[start]=='-':
            is_positive = False
            start += 1
        elif s[start]=='+':
            start += 1
            
        for i in range(start, len(s)):
            if 48<=ord(s[i])<=57:
                continue
            else:
                end = i
                break
                        
        if start==end:
            return 0
        
        ret = int(s[start:end])
        
        if is_positive:
            return limit-1 if ret>=limit else ret
        else:
            return limit*(-1) if ret>limit else ret*(-1)
        
        
        
        