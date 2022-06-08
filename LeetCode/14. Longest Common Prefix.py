class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""
        min_len = min([len(s) for s in strs])
        
        for i in range(min_len):
            ch = None
            is_common = True
            for s in strs:
                if ch==None:
                    ch = s[i]
                elif ch==s[i]:
                    continue
                else:
                    is_common = False
                    break
            if is_common==False:
                break
            else:
                ret += ch
        return ret
                