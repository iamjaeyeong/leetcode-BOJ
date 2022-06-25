class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cnt = 0
        idx = -1
        pos = []
        
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                pos.append(i)
        
        for i in pos:
            is_true = True
            for j in range(len(needle)):
                if i+j>=len(haystack) or haystack[i+j]!=needle[j]:
                    is_true = False
                    break
            if is_true:
                idx = i
                break
        
        return idx