class Solution:
    def letterCombinations(self, digits: str):
        alphabet = [chr(i) for i in range(97, 123)]
        
        def alphabet_combination(digits, ret, combinations, alphabet=alphabet, depth=0):
            if depth == len(digits):
                ret.append(combinations)
            else:   
                digit = int(digits[depth])
                s = (digit-2)*3
                if digit<7:
                    e = s+3
                elif digit==7:
                    e = s+4
                elif digit==8:
                    s += 1
                    e = s+3
                else:
                    s +=1
                    e = s+4
                    

                for i in range(s, e):
                    alphabet_combination(digits, ret, combinations+alphabet[i], depth=depth+1)
        
        ret = []
        alphabet_combination(digits, ret, "")
        
        if ret[0]=="":
            ret = []
        return ret
            
