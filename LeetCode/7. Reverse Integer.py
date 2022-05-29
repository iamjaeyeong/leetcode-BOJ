class Solution(object):
    def reverse(self, x):
        is_negative = True if x<0 else False
        x = abs(x)
        limit = pow(2, 31)-1
        str_x = str(x)
        str_x_rev = reversed(str_x)
        str_x_rev = ''.join(str_x_rev)
        int_x_rev = int(str_x_rev)
        
        if is_negative:
            limit += 1        
        
        if int_x_rev >= limit:
            return 0
        else:
            return -1*int_x_rev if is_negative else int_x_rev
        
            
        