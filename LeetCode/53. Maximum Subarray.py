class Solution:
    def maxSubArray(self, nums) -> int:
        ret, s = 0, 0
        all_negative = True
        for n in nums:
            if n>0:
                all_negative = False
            s += n
            ret = max(ret, s)
            if s<0:
                s = 0
        return ret if all_negative==False else max(nums)