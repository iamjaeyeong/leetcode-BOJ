class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=-1
        ret=None
        for idx, c in enumerate(s):
            cnt=1
            while 1:
                if idx-cnt<0 or (idx+cnt)>=len(s) or s[idx-cnt]!=s[idx+cnt]:
                    break
                else:
                    cnt+=1
            if ans<cnt*2-1:
                ret=idx
                ans=cnt*2-1
            cnt=0
            while 1:
                if idx-cnt<0 or (idx+1+cnt)>=len(s) or s[idx-cnt]!=s[idx+1+cnt]:
                    break
                else:
                    cnt+=1
            if ans<cnt*2:
                ret=idx
                ans=cnt*2
        if ans%2:
            return s[ret-ans//2:ret+ans//2+1]
        else:
            return s[ret-ans//2+1:ret+ans//2+1]