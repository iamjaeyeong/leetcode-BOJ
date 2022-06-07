class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ['F', 'M', 'D', 'C', 'L', 'X', 'V', 'I']
        romans_num = [5000, 1000, 500, 100, 50, 10, 5, 1]
        
        num_digits = []
        ret = ""

        for i in [1000, 100, 10, 1]:
            num_digits.append(num//i)
            num %= i
        
        for idx, i in enumerate(num_digits):
            if i>=5:
                if i==9:
                    ret += romans[idx*2+1]
                    ret += romans[(idx-1)*2+1]
                    i = 0
                else:
                    ret += romans[idx*2]
                    i -= 5
            if i!=4:
                ret += romans[idx*2+1]*i
            else:
                ret += romans[idx*2+1]
                ret += romans[idx*2]
                
        return ret