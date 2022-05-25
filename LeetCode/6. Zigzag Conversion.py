class Solution(object):
    def convert(self, s, numRows):
        self.unit = numRows*2-2
        self.ret = ""
    
        if numRows == 1:
            return s
        
# top line
        for i in range(0, len(s), self.unit):
            self.ret += s[i]
            
# middle line
        for i in range(1, numRows-1):
            for j in range(0, len(s), self.unit):
                if j+i < len(s):
                    self.ret += s[j+i]
                if j+self.unit-i < len(s):
                    self.ret += s[j+self.unit-i]

# bottom line
        for i in range(numRows-1, len(s), self.unit):
            self.ret += s[i]
        
        return self.ret
            