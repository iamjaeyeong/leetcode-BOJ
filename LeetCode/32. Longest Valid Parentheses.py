class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s=="":
            return 0
        
        # return value
        bucket1 = 0
        # value of sequence of tokens
        bucket2 = 0
        # tokens
        bucket3 = 0
        
        stack = 0
        temp = 0
        
        for i in s:
            if i=='(':
                stack += 1
            else:
                stack -= 1
                bucket3 += 2
            
            if stack==0:
                bucket2 += bucket3
                bucket3 = 0
                bucket1 = max(bucket1, bucket2)
            elif stack<0:
                stack, bucket2, bucket3 = 0, 0, 0
        ret1 = max(bucket1, bucket2)
        
        # return value
        bucket1 = 0
        # value of sequence of tokens
        bucket2 = 0
        # tokens
        bucket3 = 0
        
        stack = 0
        temp = 0
        s = s[::-1]
        for i in s:
            if i==')':
                stack += 1
            else:
                stack -= 1
                bucket3 += 2
            
            if stack==0:
                bucket2 += bucket3
                bucket3 = 0
                bucket1 = max(bucket1, bucket2)
            elif stack<0:
                stack, bucket2, bucket3 = 0, 0, 0
        ret2 = max(bucket1, bucket2)
        
        return max(ret1, ret2)