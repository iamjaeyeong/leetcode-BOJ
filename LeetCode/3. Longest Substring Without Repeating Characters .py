class Solution(object):
    def lengthOfLongestSubstring(self, s):
        count=[]
        check=[-1 for i in range(200)]
        anchor=0
        for idx, c in enumerate(s):
            if check[ord(c)]!=-1:
                if anchor<check[ord(c)]+1:
                    count.append(idx-anchor)
                    anchor=check[ord(c)]+1
            check[ord(c)]=idx
        count.append(len(s)-anchor)
        return max(count)
    
