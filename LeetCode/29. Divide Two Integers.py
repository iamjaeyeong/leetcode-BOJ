class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend<0)^(divisor<0):
            is_negative = True
        else:
            is_negative = False
        
        diviend = abs(dividend)
        divisor = abs(divisor)
        ret = 0
        cnt = 10000
        divisor2 = 0
        
        for i in range(cnt):
            divisor2 += divisor
                    
        while 1:
            diviend -= divisor2
            if diviend>0:
                ret += cnt
            elif diviend==0:
                ret += cnt
                break
            else:
                diviend += divisor2
                break
        
        while 1:
            diviend -= divisor
            if diviend>0:
                ret += 1
            elif diviend==0:
                ret += 1
                break
            else:
                break
                
        if not(is_negative) and ret>2147483647:
            ret = 2147483647
            
        return -1*ret if is_negative else ret