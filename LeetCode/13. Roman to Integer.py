class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        ret = 0
        p = -1
        
        for idx in range(len(s)):
            if idx==p:
                continue
            if idx+1<len(s) and roman_dict[s[idx]]<roman_dict[s[idx+1]]:
                ret += roman_dict[s[idx+1]]-roman_dict[s[idx]]
                p = idx+1
            else:
                ret += roman_dict[s[idx]]
                
        return ret
                