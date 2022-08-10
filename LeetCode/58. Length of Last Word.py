class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = None
        end = -1
        for i in range(len(s)-1, -1, -1):
            if start==None:
                if s[i]==" ":
                    continue
                else:
                    start = i
            else:
                if s[i]==" ":
                    end = i
                    break
                else:
                    continue
        
        return start - end