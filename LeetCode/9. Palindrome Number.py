class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        
        digits = []
        while x>0:
            digits.append(x%10)
            x /= 10
        
        for i in range(len(digits)//2):
            if digits[len(digits)-i-1]!=digits[i]:
                return False
        
        return True
        